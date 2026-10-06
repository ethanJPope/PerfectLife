---
type: audit
status: active
created: 2026-09-20
updated: 2026-09-20
schema: 1
---

# Initial setup verification

Scope: files created for LifeVault and its six skills, plus the current setup conversation. No prior-day history or older vaults was inspected. This is an initial structural and manual instruction review, not a longitudinal audit or independent model evaluation.

## Verified
- Six skill entry points passed the skill-creator validator. The first validation invocation encountered Windows' default text encoding; rerunning Python in UTF-8 mode passed. Saved files remain UTF-8.
- The interview bank contains 120 unique question IDs and 36 core candidates.
- The initial 25 Markdown notes had valid expected metadata and no unresolved internal note links. Obsidian configuration files parsed successfully.
- Startup files totaled 793 words at the initial check, below the local 1,500-word design budget.
- A recovery package containing 48 files passed ZIP integrity checks. All 48 restored files matched their recorded SHA-256 hashes in an isolated temporary directory. It included the vault, skills, and global/project instruction copies.
- The backup utility correctly rejected a destination inside the vault.

## Retrieval checks from saved evidence
| Question | Answer found | Evidence |
|---|---|---|
| Where does the new vault belong? | D:\PerfectLife\LifeVault | [[07 Journal/2026/09/2026-09-20 Setup preferences]] |
| Should ordinary useful facts be saved automatically? | Yes, with a brief save report. | [[02 Profile/Preferences]] F006 |
| What failed in earlier attempts? | Poor initial planning/setup and missing key personal information. | [[02 Profile/Preferences]] F007 |
| Which life domains come first? | Unknown; not answered yet. | [[00 System/Onboarding]] |
| Has the hour-long interview happened? | No; the skill and question bank are ready. | [[00 System/Onboarding]] |

These were checked against the notes in this task. They are not proof of fresh-task automatic loading.

## Instruction review
Reviewed the rules for changed preferences, newer mentions of older events, tentative goals, inaccessible sources, unsolicited sensitive information, interrupted interviews, assisted versus independent learning, forgetting requests, and concurrent edits. The written procedures preserve the intended distinctions. Actual model adherence needs testing during use; this review does not certify future behavior.

## Remaining live checks
- Open this folder as an Obsidian vault and confirm Home, templates, and daily notes behave correctly.
- Start a new local Codex task and test one retrieval question without restating the answer.
- Choose an independent backup destination. The current recovery package is on the same drive.
- Begin the interview. No learning baseline or priority domains have been invented.

## First experiment
Use one real project for a week, then run `$lifevault-audit`. Compare every important statement in the available sampled sessions against a canonical saved note, and test whether the next action is retrievable. Report the sample and missing coverage rather than claiming perfect capture across inaccessible chats.
