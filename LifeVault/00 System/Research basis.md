---
type: system
status: active
created: 2026-09-20
updated: 2026-09-20
schema: 1
---

# Research basis and design decisions

Researched: 2026-09-20. Scope: a durable personal Obsidian vault, reliable context across local Codex tasks, onboarding, source verification, and teaching. This is a source-informed design review, not a systematic review or a scientifically established “best vault.”

## Recommendation
Use ordinary Markdown, a compact home page, one authoritative note for each domain/project, and dated session evidence. Add explicit capture rules and a small weekly audit. Favor reliable retrieval and low maintenance over a large plugin stack. The custom architecture and review intervals are hypotheses to test in Ethan's real use.

| Approach | Useful for | Failure risk for this goal | Decision |
|---|---|---|---|
| Dates and daily notes alone | Reconstructing what happened | Current facts become scattered; newest mention may describe an older event | Keep as evidence and handoffs. |
| PARA-style grouping | Organizing by projects, responsibilities, reference, and inactivity | Does not by itself specify provenance, current truth, or AI retrieval | Adapt these distinctions. |
| Topic/linked-note collections | Reusable ideas and research | Easy to overbuild links without saving practical project state | Use selectively in Knowledge. |
| A single giant personal profile | One place to read | Contradictions, bloated context, and hard-to-track changes | Use a short derived Context with domain links. |
| Databases and many plugins | Powerful dashboards and custom automation | More dependencies and maintenance before the basic workflow is proven | Begin with core Obsidian features. |

These tradeoffs are design judgments, not measured rankings. The user's reported earlier failure was missing key facts after an inadequately planned setup. That makes explicit capture and retrieval checks more important than visual complexity.

## Source-to-decision ledger

### Storage, organization, and durability
1. [Obsidian: How data is stored](https://help.obsidian.md/Files+and+folders/How+Obsidian+stores+data). Official help page inspected. Notes are local Markdown and a vault is a folder; external editors can work with those files. **Decision:** portable text and relative internal links. **Limit:** a file format does not guarantee six years of maintenance or correct AI memory.
2. [Obsidian: Properties](https://help.obsidian.md/properties). Official help page inspected. Properties support structured metadata and consistent types; nested properties have UI limitations. **Decision:** flat dates/status fields, with richer provenance tables in the body. The exact schema is our design.
3. [Obsidian: Daily notes](https://help.obsidian.md/plugins/daily-notes) and [Templates](https://help.obsidian.md/plugins/templates). Official pages inspected. Core features support dated subfolders and reusable note structures. **Decision:** dated journal entries and eight standard templates, without community-plugin dependence.
4. [Obsidian: Backups](https://help.obsidian.md/backup). Official page inspected. Sync and backup serve different purposes; file recovery has limits. **Decision:** preserve separate recovery copies and test restoration. **Limit:** the initial copy on the same drive is only a recovery convenience; an approved independent destination is still needed.
5. [Tiago Forte: The PARA Method](https://fortelabs.com/blog/para/). Originator's practitioner article inspected. It distinguishes projects, areas, resources, and archives. **Decision:** borrow actionable grouping while adding Profile, Learning, and session provenance for this use. **Limit:** practitioner guidance and commercial claims are not controlled evidence that this arrangement is best for Ethan.

### Codex continuity
6. [OpenAI: Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md). Official discovery guidance inspected. Global and project instructions are loaded according to location and precedence; overrides matter. **Decision:** a small global pointer to the vault, with local entry instructions. **Limit:** files must be available on the executing host; other products and hosts need their own setup.
7. [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills). Official guidance inspected. Skills separate discoverable metadata from detailed instructions and references. **Decision:** six focused skills, with long interview/method references loaded on demand. **Limit:** static file validity cannot prove a new session's actual discovery; test a fresh task.

### Interview design
8. [Pew Research Center: Writing survey questions](https://www.pewresearch.org/writing-survey-questions/). Methodology page inspected. Question wording, ordering, clarity, and asking one concept at a time affect responses. **Decision:** open prompts, small batches, concrete examples, and clarification without leading answers. **Limit:** this onboarding interview is not a validated survey instrument.
9. [Pew: Cognitive interviewing](https://www.pewresearch.org/decoded/2021/08/23/using-cognitive-interviewing-to-design-survey-questions-about-democracy/). Method overview surfaced during research; only the accessible description was used. **Decision:** ask what a vague answer means and revise confusing prompts during the first weeks. No claim of conducting a formal cognitive-interviewing study.
10. [Self-Determination Theory: Basic psychological needs](https://selfdeterminationtheory.org/topics/application-basic-psychological-needs/). Research program's overview inspected through search text. **Decision:** include optional questions about chosen goals, felt capability, and support. **Limit:** those prompts are a design adaptation, not a diagnosis or need-satisfaction score.

The 120-question bank was written for this workflow. Its 36 core candidates cover desired outcomes, memory boundaries, current roles, goals, project state, commitments, schedule, learning, research, tools, communication, and verification. The remaining questions are optional depth. Do not claim research has established that these exact questions or a 60-minute interview are optimal.

### Reliable research
11. [Digital Inquiry Group: Teaching lateral reading](https://cor.inquirygroup.org/curriculum/collections/teaching-lateral-reading/). Public curriculum overview inspected; gated lesson downloads were not accessed. **Decision:** investigate unfamiliar sources outside their own sites and trace claims to original evidence. Site appearance is not authority.
12. [NIST: Generative AI Profile, NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence). Publication page and indexed discussion of confabulation inspected. **Decision:** prohibit fabricated evidence, require direct support, and allow “unknown.” **Limit:** a prompt or checklist cannot honestly guarantee zero model errors.

The homework/general/strict modes, claim ledger, independent calculation checks, and acceptance gates are local operating policies. They reduce opportunities for unsupported assertions but are not an error-free certification system. In strict mode, an unsupported load-bearing claim blocks an unqualified conclusion.

### Teaching and retention
13. [IES: Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/wwc/PracticeGuide/1), 2007. Recommendations page inspected. Its evidence ratings vary by recommendation. **Decision:** use spaced review, worked examples with attempts, retrieval, and explanatory questions. Application to a one-person AI tutor remains an adaptation.
14. [Roediger & Karpicke: Test-enhanced learning](https://pubmed.ncbi.nlm.nih.gov/16507066/), 2006, DOI 10.1111/j.1467-9280.2006.01693.x. Abstract inspected. Their prose-learning experiments distinguish immediate performance from delayed retention. **Decision:** check recall later, not just whether an explanation feels clear now. Do not generalize a numerical effect to Ethan.
15. [Cepeda et al.: Distributed practice](https://pubmed.ncbi.nlm.nih.gov/16719566/), 2006, DOI 10.1037/0033-2909.132.3.354. Abstract inspected. Spacing effectiveness depends on retention timing. **Decision:** a flexible review queue. The proposed 1/3/7/14-day starter schedule is a heuristic, not a directly validated universal schedule.
16. [Pashler et al.: Learning Styles—Concepts and Evidence](https://pubmed.ncbi.nlm.nih.gov/26162104/), 2008. Indexed abstract/review summary inspected; the direct page did not return readable text in one fetch. **Decision:** avoid fixed learning-style labels; adapt using preferences and demonstrated outcomes. No claim that people have identical needs or preferences.

### How people use AI tutors
17. [Kazemitabaar et al.: AI code generators and novice learners](https://arxiv.org/abs/2302.07427), 2023. Abstract and publication metadata inspected, not a full-paper methodological appraisal. In its controlled introductory-Python setting, AI access improved authoring outcomes without the reported decrease in manual modification performance; the one-week overall post-test difference was not statistically significant. **Decision:** avoid simplistic “AI always harms learning” claims; evaluate independent performance.
18. [Kazemitabaar et al.: How novices use code generators](https://arxiv.org/abs/2309.14049), 2023. Abstract and metadata inspected. Its analysis describes different approaches and a task-performance tradeoff for single-prompt use. **Decision:** preserve attempts and use modification/transfer tasks. **Limit:** related authors, earlier tools, small specific setting; not independent proof about modern Codex or this learner.
19. [Codex community: Should I get Codex as a CS student?](https://www.reddit.com/r/codex/comments/1w281qx/should_i_get_codex_cs_student/). Selected post/comments inspected. Users discuss explanations and tutoring alongside concerns about outsourcing practice. **Decision:** distinguish tutoring from delegated execution. **Limit:** anecdotal, self-selected reports; product/pricing claims in comments were not adopted.
20. [Learning-programming community: AI without coding for you](https://www.reddit.com/r/learnprogramming/comments/1pd49aw/best_way_to_learn_with_ai_without_it_coding_for/). Post and available comments inspected. One practical suggestion is to build quizzes around the learner's supplied material. **Decision:** source-grounded practice questions and feedback. **Limit:** a workflow idea, not experimental evidence.

## What we still need to learn
Ethan's actual priority domains, learning baseline, time budget, preferred capture workflow, and independent backup destination. No old biography was imported to fill these gaps. The setup must earn its complexity through use.

## Three-week evaluation
- Week 1: measure whether important facts and project handoffs are captured and retrievable.
- Week 2: test a fresh-chat continuation and delayed recall from one real lesson; fix repeated friction.
- Week 3: simplify unused structure, test recovery, and decide what becomes the stable baseline.

Use actual samples and denominators. Suggested targets—finding a handoff in under a minute, keeping daily maintenance near five minutes, and capturing all important items in sampled sessions—are starting goals to confirm with Ethan, not established personal preferences.
