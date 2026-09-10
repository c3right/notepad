# Repository capture rules

This repository is a durable notepad for small discoveries, research fragments, conversation syntheses, reading lists, decision notes, and other compact outputs worth keeping.

These rules apply to AI assistants and humans adding material to this repository.

## 1. Storage model

Use chronology as the canonical storage key and metadata for topical retrieval.

- Canonical notes: `notes/YYYY/YYYY-MM-DD-<ascii-kebab-slug>.md`
- Reusable note template: `_templates/note.md`
- Human-facing catalog: `INDEX.md`
- Repository purpose and navigation: `README.md`

Do **not** create top-level folders per topic unless the repository later grows enough to justify a migration. Many notes span several topics; forcing them into one topical folder creates ambiguous placement.

## 2. What to save

Save a distilled, reusable artifact rather than a raw chat transcript unless the user explicitly asks for the transcript.

A good saved note should preserve:

1. the core question or trigger;
2. the strongest conclusions;
3. the framework/model produced;
4. useful tables, checklists, book lists, links, or other concrete outputs;
5. important caveats and unresolved items;
6. next steps only when they materially help future reuse.

Remove conversational filler, repeated turns, and obsolete intermediate formulations. If the conversation evolved, save the latest coherent model and briefly note major earlier alternatives only when useful.

## 3. Required front matter

Every canonical note must begin with YAML front matter:

```yaml
---
title: "..."
date: YYYY-MM-DD
updated: YYYY-MM-DD
status: evergreen | working | archived
type: synthesis | research-note | reading-list | decision-note | checklist | reference
topics:
  - topic-a
  - topic-b
keywords:
  - keyword-a
  - keyword-b
source: "ChatGPT conversation | web research | personal note | mixed"
language: zh-CN
---
```

Guidance:

- `title`: human-readable Chinese is fine.
- filename slug: use concise ASCII kebab-case for stable links/tool compatibility.
- `topics`: 2–6 broad, reusable categories.
- `keywords`: concrete concepts, book names, people, or techniques useful for search.
- `status=evergreen`: distilled note expected to remain useful.
- `status=working`: incomplete, tentative, or still being developed.

## 4. Recommended note structure

Use only sections that add value, but prefer this order:

1. `# Title`
2. `## 一句话结论` / executive summary
3. `## 核心框架`
4. `## 关键内容` or domain-specific sections
5. `## 可直接使用的工具/清单`
6. `## 书目与参考`
7. `## 限制与待核验`
8. `## Revision log` when materially updated later

## 5. Evidence and uncertainty

- Distinguish facts, interpretations, recommendations, and hypotheses.
- For current or externally verified facts, retain useful source links and dates when available.
- Never make a speculative claim look verified merely because it appeared earlier in a conversation.
- Bibliographic metadata gathered from the web should be marked as needing publisher/copyright-page verification when exact edition details matter.
- Preserve meaningful disagreements between models instead of forcing a false single answer.

## 6. Updating existing notes

Before creating a new note, search for a clearly overlapping existing note.

- If the new material is a continuation or refinement of the same artifact, update the existing note.
- If it is independently useful or substantially different in scope, create a new note and cross-link it.
- On material updates, change `updated:` and add a short `Revision log` entry.
- Do not silently erase an earlier conclusion when the change itself is informative; note the revision briefly.

## 7. Maintain the index

Every new canonical note must be added to `INDEX.md` with:

- date;
- title/link;
- one-line description;
- 2–5 topic tags.

Keep the index compact. It is a catalog, not a duplicate of the note.

## 8. Privacy and safety

This repository is public. Do not store:

- passwords, tokens, API keys, private URLs, or credentials;
- personally identifying private information;
- sensitive personal records;
- proprietary/confidential material unless the user explicitly confirms it is appropriate for a public repository.

When in doubt, omit sensitive details and save only the reusable abstraction.

## 9. Commit style

Prefer small descriptive commits:

- `notes: add <topic> synthesis`
- `notes: update <topic> synthesis`
- `docs: update repository capture rules`
- `index: add <note title>`

Direct commits to the default branch are acceptable for ordinary note capture unless the user asks for a pull-request workflow.
