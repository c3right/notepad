#!/usr/bin/env python3
"""2026-08 historical iPhone-friendly ZgoCloud traffic report.

Archive of the final Shortcuts-facing implementation, not a live snapshot.
Reads vnStat v2 JSON via SSH-invoked local process; no HTTP server.
Limitations: fixed historical first-cycle offset, approximate provider billing,
and day-history retention / partial-day projection caveats noted in companion note.
"""
import json
import subprocess
from datetime import date, timedelta

ALLOWANCE_GB = 1024
BILLING_DAY = 21
FIRST_PERIOD_START = date(2026, 8, 21)
FIRST_PERIOD_OFFSET_GB = 1.28
MIN_FULL_TRACKED_DAYS_FOR_PROJECTION = 3


def billing_period(today):
    if today.day >= BILLING_DAY:
        start = date(today.year, today.month, BILLING_DAY)
        if today.month == 12:
            next_start = date(today.year + 1, 1, BILLING_DAY)
        else:
            next_start = date(today.year, today.month + 1, BILLING_DAY)
    else:
        if today.month == 1:
            start = date(today.year - 1, 12, BILLING_DAY)
        else:
            start = date(today.year, today.month - 1, BILLING_DAY)
        next_start = date(today.year, today.month, BILLING_DAY)
    return start, next_start - timedelta(days=1)


data = json.loads(subprocess.check_output(["vnstat", "--json"], text=True))
days = data["interfaces"][0]["traffic"]["day"]

today = date.today()
start, end = billing_period(today)

rx_bytes = 0
tx_bytes = 0
tracked_dates = []

for item in days:
    d = item["date"]
    item_date = date(d["year"], d["month"], d["day"])
    if start <= item_date <= today:
        rx_bytes += item["rx"]
        tx_bytes += item["tx"]
        tracked_dates.append(item_date)

# vnStat 2.10 JSON v2 values are bytes, NOT KiB.
# This historical script labels the binary GiB calculation as GB.
rx_gb = rx_bytes / (1024 ** 3)
tx_gb = tx_bytes / (1024 ** 3)
offset = FIRST_PERIOD_OFFSET_GB if start == FIRST_PERIOD_START else 0.0
used_gb = rx_gb + tx_gb + offset
remaining_gb = max(ALLOWANCE_GB - used_gb, 0.0)
percent = used_gb / ALLOWANCE_GB * 100

period_days = (end - start).days + 1
cycle_day = (today - start).days + 1
full_tracked_days = len({d for d in tracked_dates if d < today})
status = "🟢 正常" if percent < 70 else ("🟡 注意" if percent < 90 else "🔴 警告")

print("ZGO-LA 流量")
print()
print(status)
print()
print("📅 计费周期")
print(f"{start.strftime('%m/%d')} ～ {end.strftime('%m/%d')}")
print(f"第 {cycle_day} / {period_days} 天")
print()
print("📊 本周期已用")
print(f"{used_gb:.2f} GB / {ALLOWANCE_GB} GB")
print(f"{percent:.2f}%")
print()
print("📥 接收")
print(f"{rx_gb:.3f} GB")
print()
print("📤 发送")
print(f"{tx_gb:.3f} GB")
print()
print("💾 剩余")
print(f"{remaining_gb:.2f} GB")
print()
print("📈 周期预测")

if full_tracked_days >= MIN_FULL_TRACKED_DAYS_FOR_PROJECTION:
    completed_rx = 0
    completed_tx = 0
    for item in days:
        d = item["date"]
        item_date = date(d["year"], d["month"], d["day"])
        if start <= item_date < today:
            completed_rx += item["rx"]
            completed_tx += item["tx"]

    tracked_full_gb = (completed_rx + completed_tx) / (1024 ** 3)
    avg = tracked_full_gb / full_tracked_days
    projected = offset + avg * period_days

    print(f"完整采样 {full_tracked_days} 天")
    print(f"近期日均 {avg:.2f} GB/天")
    print(f"预计 {projected:.2f} GB")

    if projected > ALLOWANCE_GB:
        print()
        print("⚠️ 按当前速度预计将超过套餐流量")
else:
    print("采样不足")
    print(f"满 {MIN_FULL_TRACKED_DAYS_FOR_PROJECTION} 个完整统计日后开始预测")
