from pathlib import Path
import textwrap, json

V=Path('D:/PerfectLife/LifeVault')
S=Path('C:/Users/ethan/.codex/skills')

def write(p,s):
    if p.exists(): raise RuntimeError(f'Already exists: {p}')
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(textwrap.dedent(s).strip()+'\n',encoding='utf-8')

def skill(name, description, title, summary, body):
    write(S/name/'SKILL.md', '---\nname: '+name+'\ndescription: '+json.dumps(description)+'\n---\n\n'+textwrap.dedent(body).strip())
    write(S/name/'agents/openai.yaml', 'interface:\n  display_name: '+json.dumps(title)+'\n  short_description: '+json.dumps(summary)+'\n  default_prompt: '+json.dumps('Use $'+name+' to '+summary.lower()+'.')+'\n')

common='''
LifeVault is at `D:\\PerfectLife\\LifeVault`. Read `00 System/Start.md` and `00 System/Memory rules.md` before personal-memory work. Read relevant current notes, not the whole vault. If unavailable, disclose that limitation; never create a replacement vault silently. Save ordinary important information automatically with provenance and briefly report the save. Sensitive information requires specific permission before collection/use/storage. No passwords, tokens, recovery codes, full payment details, or identity documents.
'''

skill('getting-started', 'Conduct or resume Ethan’s thorough LifeVault onboarding interview; establish personal context, priorities, permissions, and real project handoffs.', 'Getting started', 'Build your context through a guided interview', '''
# Getting started

'''+common+'''

## Intended experience
Run a thoughtful, roughly hour-long conversation, not a questionnaire dump. Aim for 55–75 minutes of user participation across as many sessions as needed. The question bank has core prompts plus optional depth; answering every prompt can take much longer. Time estimates are planning assumptions. Never claim an hour passed without checking time.

Read `00 System/Onboarding.md`, `02 Profile/Preferences.md`, and [references/interview.md](references/interview.md). Begin at the recorded resume point. Do not import old vaults or other chats to prefill personal answers. Existing global working agreements are behavior rules, not evidence for new biographical facts.

## Conversation loop
1. Explain briefly that answers can be short, skipped, revisited, or kept out of memory. Use the current user’s explicit saving permissions; don't repeatedly request blanket permission already given.
2. Select one to three related unanswered prompts. Ask one at a time when the answer needs reflection or the user seems overloaded. Start with open questions and ask for a recent concrete example before offering categories. Adapt phrasing and follow-ups; IDs are for continuity, not something Ethan must manage.
3. Reflect back only what matters. Distinguish goals from current behavior, facts from uncertainty, and Ethan's words from your interpretation. Don't infer diagnoses, age, personality types, income, family structure, or learning style.
4. Save useful non-sensitive answers immediately into the right canonical notes and a concise session source. Record question ID, answered/skipped/later/not-applicable, destination, evidence date, and next follow-up in Onboarding. Do not save sensitive payloads while awaiting consent. Do not create empty profile files for skipped domains.
5. Every 10–15 minutes or at a topic boundary, offer a short recap and an opportunity to correct or pause. Ask a focused question if an important missing fact would otherwise be lost. Avoid asking again what was already answered; mark existing evidence against the matching question ID.
6. At a pause, save the precise resume question, unresolved assumptions, and next action. A stopped interview is paused, not failed or complete.

## A useful finish
Produce a brief profile of confirmed essentials, one actionable project handoff if applicable, a realistic learning starting point if requested, and a short list of deferred topics. Run a retrieval demonstration from saved files: answer “What matters now, where did we stop, and what comes next?” Cite actual notes and invite correction.

Mark core-complete only when completion criteria in Onboarding are met or specific items were explicitly deferred. Mark expanded-complete only when the chosen deeper modules are handled; never imply every question was answered. Preserve unknowns. Update Context and Projects with links, not transcript copies. Ask Ethan what the interview missed.

## Quality standard
The bank is a custom operational interview, not a validated psychological assessment. Its question-writing principles are adapted from Pew's survey guidance; motivation/learning prompts are informed by educational research. See `00 System/Research basis.md` for sources and limits. Do not treat collected self-reports as independent proof of performance.
''')

skill('lifevault-remember', 'Save, update, correct, or forget important LifeVault personal context and project handoffs using provenance, freshness, and privacy rules.', 'LifeVault remember', 'Save important context in the right place', '''
# Remember reliably

'''+common+'''

Read the full Memory rules contract and relevant template under `00 System/Templates`. Identify what will actually matter in a future session. The current user authorized automatic useful non-sensitive saving; do not ask for each ordinary fact.

## Capture
- Extract concise facts, decisions and reasons, real commitments, constraints, completed outcomes, unresolved blockers, and next actions. Keep guesses and proposed plans distinct.
- Search existing notes for the same concept. Prefer updating one authoritative home. Preserve sources and evidence dates; don't replace them with today's edit date.
- Keep a short source note for new information, using actual message content and known task metadata only. Save no fabricated quotations or task IDs.
- Update project state after meaningful milestones even before the conversation ends. Add a journal handoff, then refresh index/current summary only when needed.
- Read back the result. Report the useful saved change in one sentence with a link; don't recite sensitive contents unnecessarily.

## Corrections and forgetting
For an ordinary correction, retain the prior fact as corrected/superseded history and point to the replacement. When instructed to forget, remove the targeted content from canonical notes and derived summaries rather than re-saving it in history; follow the backup limits in Memory rules. Do not erase unrelated data. For conflicting assertions, preserve uncertainty and ask only the question needed to resolve it.

## Completion
The fact can be found from a relevant index, includes a source and evidence date, and is not duplicated as independently authoritative content elsewhere. Failed writes are reported as failed. An unsaved chat is never described as remembered.
''')

skill('lifevault-resume', 'Recover relevant LifeVault context at the start of a task or when continuing a project, lesson, decision, or interrupted conversation.', 'LifeVault resume', 'Pick up exactly where useful work stopped', '''
# Resume from evidence

'''+common+'''

1. Read `00 System/Context.md` and `03 Projects/Projects.md`. For a lesson, also read `06 Learning/Learning.md`. Select the note that matches the current request.
2. Read the selected canonical note, latest linked handoff, and only the relevant profile constraints. Check actual completion evidence and dates. Verify external files or repository state when needed; a prior plan isn't proof an action occurred.
3. Respond briefly: last verified result; unresolved issue; next concrete action. Mention outdated or uncertain context only when it matters. Use a file citation for consequential remembered context.
4. If multiple projects fit, ask a specific choice. If the handoff is missing, search targeted journal terms/date ranges, then ask for the missing detail. Do not load all chat history or archived notes as a substitute for a missing fact.
5. Continue the user's authorized work. At a milestone update the handoff following Memory rules. Record any retrieval failure as a non-sensitive friction item for audit.

Do not confuse “file last modified” with “user last confirmed.” Do not promote a speculative future event to current reality because its planned date passed. Ask proactively when missing context could cause repeated work. If the user requests no memory use, follow that instruction for the session.
''')

skill('lifevault-research', 'Research questions with traceable sources, verification matched to stakes, and clear explanations; includes strict evidence work and checked math homework.', 'LifeVault research', 'Research with evidence and clear uncertainty', '''
# Research without fabricated certainty

'''+common+'''

Read [references/research-method.md](references/research-method.md) for the selected mode. The non-negotiable rule is zero fabricated claims, sources, citations, quotations, calculations, or tool outcomes. This is an acceptance standard, not a guarantee of model infallibility. If evidence is insufficient, narrow the claim, mark it unverified, or say the answer is unknown.

## Route the request
| Mode | Trigger | Required outcome |
|---|---|---|
| Homework / teaching | Explain or practice a mathematical or school concept | Correctly checked steps, preserved student attempt, one teaching step at a time. |
| Strict evidence | User requests high reliability, publication-quality research, consequential/current advice, contested factual claims | Claim-to-source ledger, direct source inspection, independent corroboration where feasible, explicit gaps and limitations. |
| General | Low-stakes orientation or everyday curiosity | Concise supported answer; still verify unstable, uncertain, specific, or requested factual claims. |

Choose the strictest mode justified by the request. Mode changes depth, never honesty. A math problem for consequential engineering is strict evidence as well as calculation. If the research objective, jurisdiction, timeframe, source restrictions, or school rubric would change the answer, ask a concise question and continue independent gathering.

## Execute
Define the question and what evidence would settle it. Search with neutral terms, then actively seek counterevidence. Inspect sources directly; don't cite search snippets as if the page was read. Prefer original evidence and authoritative documentation matched to the exact claim. Track dates, versions, populations, methods, interests, and actual support.

Check each material claim and numerical result. Cite immediately beside the claim. Explain what the evidence means for Ethan, separate inference and recommendation, and disclose relevant limitations. Never pad with source count or claim multiple syndicated copies are independent confirmation.

Save durable findings to `05 Knowledge` using the Research template, including the actual question, mode, date, claim ledger, source links, limitations, and reuse conditions. Task-specific findings may live with their project instead. Don't save every casual answer. Do not store private research subjects or send their data to external search without required permission.

## Finish
Lead with the answer in plain English. Include decisive evidence, limitations that could change the conclusion, and useful next steps only. Before delivery verify citation support, quotation accuracy, arithmetic, dates, and that no unverified statement is presented as established. If a conclusion remains unsupported, do not certify it.
''')

skill('lifevault-teach', 'Tutor Ethan through a skill or body of knowledge using small steps, preserved attempts, feedback, retrieval practice, and saved learning evidence.', 'LifeVault teach', 'Learn through practice and lasting recall', '''
# Teach for independent performance

'''+common+'''

Read [references/teaching-method.md](references/teaching-method.md) and the relevant learning note. Ask what Ethan wants to be able to do, available time, and what he has already tried if not known. Respect course instructions and requested help level.

## One loop at a time
1. Start with one small diagnostic or a request to explain the current understanding. Use the result to choose the next step; self-rated confidence alone isn't mastery.
2. Give one concise explanation or worked step connected to a concrete example. State the expected visible result for an action. Verify the explanation or exercise solution before presenting it.
3. Let Ethan attempt a similar step, predict an output, retrieve an idea without notes, or explain why. Wait for the attempt; don't answer your own question or silently complete the learning-critical work.
4. Give specific feedback on the reasoning. If wrong, find the first mismatch, offer a small hint, and retry. If lost, stop and restore the last understood state. Avoid an endless Socratic interrogation when a direct explanation would help.
5. When successful, fade hints and introduce a new example that requires the same idea. Check delayed recall and transfer before describing the skill as mastered.

## Continuity
Save the objective, actual attempt/result, help level, misconception and correction, next exercise, and a modest review queue in `06 Learning/<topic>.md`. Use evidence labels: introduced, successful-with-help, independent-on-this-task, retained-after-delay, transferred-to-new-task. These are observations, not a permanent intelligence or ability label.

At the end ask for a short teach-back or one unassisted retrieval item, if time permits. Suggest review around 1, 3, 7, and 14 days as a starting scheduling heuristic, adjusted to errors and deadlines. Record dates in Learning; dates alone don't create notifications. Schedule reminders only when asked using supported automation tools.

## Personalization
Begin with concise explanations, concrete examples, one step, and immediate feedback, based on current working agreements. Test what helps in practice. Do not label Ethan a visual/auditory/kinesthetic learner or claim instruction should be matched to an unverified learning-style category. A preference can inform comfort without proving retention.

If Ethan explicitly asks to switch to execution, clarify only if necessary and honor the change. Do not grade AI-generated work as Ethan's own demonstrated ability. Preserve user attempts and label model examples clearly.
''')

skill('lifevault-audit', 'Audit recent LifeVault sessions for missed important context, stale or conflicting facts, retrieval failures, and small evidence-backed system improvements.', 'LifeVault audit', 'Improve the system from recent real use', '''
# Audit how the system actually worked

'''+common+'''

Default scope: the last seven calendar days in the current timezone, or the user's requested period. Read `00 System/Changes.md`, recent review notes, relevant journal files, and the canonical notes they changed. Start with paths and dates, then content. Do not load the full archive. Do not inspect old vaults to fill gaps.

## Checks
1. **Missed capture:** Compare meaningful statements, decisions, constraints, commitments, outcomes, and blockers in available sessions to their canonical notes. This is the highest-priority check because earlier systems missed key facts. Label the coverage denominator; inaccessible or unsaved conversations cannot be audited.
2. **Truth and freshness:** Confirm provenance; identify inferences presented as facts, edits mistaken for confirmations, contradictions, and facts beyond review dates. An overdue review does not prove falsehood.
3. **Continuity:** Can the current priority, last verified project result, blocker, next action, and latest learning attempt be found from the startup links? Check three to five real retrieval questions if enough evidence exists; cite answers and count failures. With no history, report insufficient data rather than inventing a trend.
4. **Structure:** Look for duplicate authoritative facts, broken links, oversized startup notes, unprocessed inbox items, and notes with no useful retrieval route. Don't demand every note link to every other note.
5. **Learning:** Compare assisted and independent attempts, delayed recall, and repeated misconceptions. Do not confuse notes written or exercises generated with learning.
6. **Privacy and durability:** Check permission metadata when relevant without exposing payloads. Check latest backup and restore evidence; a plan isn't a completed backup. Confirm whether installed skills and global startup instructions are included in recovery material.

## Improve proportionally
Write `08 Reviews/YYYY-MM-DD <scope>.md` using the Audit template. Each finding needs an exact note/section, evidence, consequence, and proposed change. Separate defects from optional preferences. Recommend at most one to three changes unless serious issues require more.

Fix reversible, unambiguous link/metadata/routing errors within the authorized audit; record before/after and verify. Do not silently decide disputed facts, change privacy permissions, perform broad restructuring, delete history, or install plugins. Stage a concrete proposal for consequential or ambiguous changes, explain why a decision is needed, and continue independent work. No ritual approval for ordinary repairs.

Record changes in `00 System/Changes.md`. Choose a short experiment, a measurable success criterion, and a rollback path. Default evaluation over the next week of use; do not create a recurring automation unless requested. Ask one high-value follow-up about observed friction. See `00 System/Research basis.md` for design assumptions.
''')

templates={
'Profile': ('profile', '''# {{title}}
| ID | Statement | Basis | Source | Recorded | Last confirmed | Valid from | Review after | State |
|---|---|---|---|---|---|---|---|---|

## History
## Open questions
'''),
'Project': ('project', '''# {{title}}
## Outcome and definition of done
## Why this matters
## Current state
Last verified result and evidence date:
Latest session:
## Next action
One concrete action:
## Blockers and open questions
## Decisions
| Date | Decision | Why | Evidence | State |
|---|---|---|---|---|
## Resources and artifacts
## History
'''),
'Area': ('area', '''# {{title}}
## Responsibility and desired standard
## Current constraints
Record each with source and confirmation date.
## Related projects
## Next review
## History
'''),
'Session': ('session', '''# {{title}}
Recorded at: {{date:YYYY-MM-DD}}T{{time:HH:mm:ssZ}}
Source/task identifier: record only if known.
## Intent
## Important user statements
Faithful summary; distinguish exact quotations and paraphrases.
## Work and verified results
## Decisions and reasons
## Attempts worth preserving
## Saved to
Link actual canonical notes; do not duplicate their entire contents.
## Handoff
Last verified result:
Blocker or open question:
Next concrete action:
'''),
'Daily': ('daily', '''# {{date:YYYY-MM-DD}}
## What matters today
## Capture
## Sessions
## Next time
'''),
'Research': ('research', '''# {{title}}
## Question and scope
Mode:
Research date:
Jurisdiction/version/population if relevant:
## Answer
## Claim ledger
| Claim | Direct source and locator | Support | Checked on | Limits |
|---|---|---|---|---|
Support: verified, supported-with-limits, inference, disputed, or unverified.
## Evidence and reasoning
## Counterevidence and gaps
## Calculations or reproducible checks
## Sources
Title, author/organization, date when known, direct URL/DOI, inspected scope (abstract/full text/etc.).
## Reuse and recheck conditions
'''),
'Learning': ('learning', '''# {{title}}
## Target independent performance
## Baseline and prerequisites
## Attempts
| Date | Task | User attempt/result | Help level | Evidence | Next step |
|---|---|---|---|---|---|
## Misconceptions and corrections
## Resume here
## Retrieval queue
| Due | Prompt without answer | Outcome | Next review |
|---|---|---|---|
## Source-checked explanations
'''),
'Audit': ('audit', '''# {{title}}
## Scope and available evidence
Period:
Files sampled:
Inaccessible/unsaved context:
## Findings
| Severity | Exact evidence | Consequence | Repair or proposal | Verification |
|---|---|---|---|---|
## Retrieval checks
| Question | Expected evidence | Actual result | Pass or fail |
|---|---|---|---|
## Metrics
Report actual counts and denominators; unknown when not measurable.
## Changes made
## Next experiment
One hypothesis, measure, review date, and rollback.
''')}
for name,(kind,body) in templates.items():
    write(V/'00 System/Templates'/f'{name}.md', '---\ntype: '+kind+'\nstatus: active\ncreated: "{{date:YYYY-MM-DD}}"\nupdated: "{{date:YYYY-MM-DD}}"\nschema: 1\n---\n\n'+body)
print('Created six skills and eight note templates.')
