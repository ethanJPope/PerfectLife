import json, hashlib, sys
from pathlib import Path
from collections import Counter

OUT = Path(__file__).parent
inv = json.loads((OUT/'inventory.json').read_text(encoding='utf-8'))
skills = {s['name']: s for s in inv['skills']}
findings = []
reviewed = set()
def evidence(name, line):
    s = skills[name]
    reviewed.add(s['path'])
    return {'path': s['path'], 'line': line, 'excerpt': Path(s['path']).read_text(encoding='utf-8-sig').splitlines()[line-1]}
def finding(name, recommendation, strength, text, refs, preserve):
    findings.append(dict(skill=name, recommendation=recommendation, strength=strength, finding=text, evidence=[evidence(n,l) for n,l in refs], preserve=preserve))
def action(skill, reason, task=None, success=None, prerequisite=None):
    d=dict(skill=skill, reason=reason)
    if task: d['task']=task
    if success: d['success_criteria']=success
    if prerequisite: d['prerequisite']=prerequisite
    return d

finding('unity-editor','revise','observed defect',
 'The Pause On Error cross-reference points to /E:/CodeSpace/... rather than this installation. The corresponding E: target does not exist here; ../console/SKILL.md exists and documents the named operation. Proposed repair: replace only the link target with ../console/SKILL.md. No repair has been applied.',
 [('unity-editor',191),('unity-console',91)], 'The console ownership of pause-on-error, operating-mode restrictions, and the documented operation name.')
finding('ai-prompt-orchestrator','insufficient evidence','inspection hypothesis',
 'The installed package contains SKILL.md and plugin/MCP configuration, but no package.json or evidence validator. Three required pnpm validate:evidence gates provide no working directory or helper-resolution instructions. The prepare_review tool is advertised, but its server-controlled plan was deliberately not requested. The validator may live elsewhere; this is an unresolved dependency, not proof that the workflow cannot run. Resolve the helper before comparing the mandatory ten-reviewer process.',
 [('ai-prompt-orchestrator',3),('ai-prompt-orchestrator',19),('ai-prompt-orchestrator',21),('ai-prompt-orchestrator',24)],
 'Single writer, bounded repair pass, screenshot freshness, short evidence-backed findings, and restrictions on sending source or sensitive content to the server.')
finding('unity-skills + unity-mcp-workflow','evaluate','inspection hypothesis',
 'Both can attract Unity automation requests. UnitySkills explicitly supports an existing REST bridge and manual guidance; the workbench flow frames editor access around MCP detection. Its instruction to reuse existing providers helps, but a REST-only project could still get unnecessary MCP setup guidance. This routing risk needs a representative fixture, not automatic consolidation.',
 [('unity-skills',13),('unity-skills',14),('unity-mcp-workflow',39),('unity-mcp-workflow',41)],
 'Discover the existing bridge, validate live state, respect surface profiles, and preserve the learning-versus-automation distinction.')
finding('stripe-directory','evaluate','inspection hypothesis',
 'The trigger covers essentially any vendor or software search, including requests that never mention Stripe. Ranking also favors Stripe-related trust signals. This may narrow general recommendations unnecessarily, although it can be useful for Stripe-specific discovery. Test routing and shortlist relevance before deciding whether to narrow the trigger.',
 [('stripe-directory',18),('stripe-directory',39),('stripe-directory',65)],
 'Exact search-query disclosure, honest handling of weak results, explicit purchase approval, and no-charge options. Ethan’s purchase and guardian checkpoints remain controlling.')
finding('canva-edit-design + canva-implement-feedback','keep','contextually inspected strength',
 'The approval flags are not a demonstrated double-approval defect: the edit skill explicitly lets a composing skill’s prior batch approval cover commit. Feedback editing uses that exception. Preserve it. The feedback workflow also replies to reviewers; any future test must include those external messages in the approved scope or use a mock, rather than treating them as silent bookkeeping.',
 [('canva-edit-design',46),('canva-edit-design',53),('canva-implement-feedback',71),('canva-implement-feedback',100)],
 'Transaction identifiers, preview-before-save, responsive-page restrictions, clear distinction between drafts and saved changes, and one approval for the approved scope.')
finding('unity-sample','investigate overlap','inspection hypothesis',
 'This is an explicit demo/connectivity module. It tells callers to use the production GameObject module and the Python health helper for actual work. Ethan can decide whether first-call demos are still useful. If not, consider removing it from the advertised set while preserving package examples and updating the module index; do not delete a managed package component in isolation.',
 [('unity-sample',30),('unity-sample',35),('unity-sample',36),('unity-skills',75)],
 'Connectivity examples and restrictions against using demos for production or bypassing surface profiles.')
finding('Unity design specialists','keep','contextually inspected strength',
 'The six flagged lexical pairs in this family reflect common source-anchored wording across different libraries. Addressables/YooAsset manage assets, DOTween/PrimeTween manage tweens, Netcode addresses multiplayer, UniTask addresses async work, and Shader Graph addresses rendering. Shared vocabulary is not duplicate behavior. Keep version scopes and source anchors, but do not treat the cited underlying API claims as revalidated by this audit.',
 [(n,3) for n in ['unity-addressables-design','unity-dotween-design','unity-primetween-design','unity-yooasset-design','unity-netcode-design','unity-unitask-design','unity-shadergraph-design']],
 'Library-specific terminology, version boundaries, lifecycle pitfalls, and source references.')
finding('Security phase skills','keep','contextually inspected strength',
 'Nine lexical-overlap pairs have distinct purposes: threat modeling, discovery, validation, attack-path analysis, and fixing findings. Their descriptions exclude primary full-scan routing. The phase boundaries explain the similar text; this first pass does not justify merging or retiring them.',
 [(n,3) for n in ['attack-path-analysis','finding-discovery','threat-model','validation','fix-finding']],
 'Explicit phase boundaries, evidence versus hypothesis, source-to-sink reasoning, and verification of legitimate behavior after repairs.')
finding('convert-to-doc + convert-to-slides','keep','contextually inspected strength',
 'These two disk-discovered helpers are not advertised in the supplied session catalog. Their lexical overlap is expected: they preserve an existing Data app but produce different artifact types using different canonical authoring skills. Their presence does not establish standalone activation or precedence.',
 [('convert-to-doc',26),('convert-to-slides',26)],
 'Source-data and chart preservation, native artifact formats, and explicit read-back verification.')
finding('comfy','keep','contextually inspected strength',
 'The trigger is explicitly limited to local ComfyUI work. Workspace discovery, workflow validation, and consent for large downloads are useful boundaries. Tool names for discovery are advertised in this session; no service availability or workflow execution was tested.',
 [('comfy',3),('comfy',12),('comfy',14),('comfy',16)],
 'Local-versus-cloud separation, reuse of the selected workspace, validation before long generation, and protection of unrelated running work.')
finding('unity-manual-scene','keep','contextually inspected strength',
 'Manual scene guidance has a distinct teaching role and should not be retired as a duplicate of automation. It matches Ethan’s preference to preserve learning attempts. The parent router explicitly distinguishes guide versus automate.',
 [('unity-manual-scene',14),('unity-manual-scene',18),('unity-skills',14)],
 'Visible UI steps and manual guidance; deliver one step at a time under Ethan’s working agreements.')
finding('stripe-best-practices','insufficient evidence','inspection hypothesis',
 'The file labels pinned API and SDK values as latest and says to use the latest version by default. This audit does not assert that those values are stale. A later compatibility test should check whether an existing pinned integration is preserved unless an upgrade is actually required, using current official documentation at that time.',
 [('stripe-best-practices',17),('stripe-best-practices',19)],
 'Integration-specific guidance and security controls; do not turn a static audit into a payment or account action.')

plan={
 'fix_now':[action('unity-editor — one verified repair, unapplied','Replace the developer-drive console link at line 191 with ../console/SKILL.md. The installed destination and operation were verified. No benchmark is needed for this link repair.')],
 'review_retirement':[action('unity-sample — user relevance decision','Do you still need first-call REST demos? If yes, retain. If no, consider hiding the demo entry from discovery while preserving examples and updating callers. Usage is unknown; this is not an obsolescence verdict.')],
 'test_next':[
  action('1. Unity routing: unity-skills + unity-mcp-workflow','Question: can both coexist without recommending a second bridge or taking over a learning task? Decision: keep both unchanged or clarify their entry conditions.', 'Use a disposable UnitySkills REST-only fixture: ask to inspect a scene hierarchy, then separately ask to learn how to frame and save a scene manually. Compare current routing with a narrower router and a no-skill baseline.', 'Recognize the existing REST bridge; propose no unnecessary install; keep the tutorial to one visible action at a time; make no editor writes for the teaching task.'),
  action('2. stripe-directory','Question: does its broad trigger improve ordinary software discovery or bias it toward the Stripe ecosystem? Decision: retain the broad trigger or narrow it.', 'Use two supplied, non-sensitive briefs: compare offline-first note tools with no payment needs, and find a Stripe-compatible billing provider. Compare current, Stripe-only trigger, and baseline under equal research budgets.', 'Meet all brief constraints; cite relevant sources; label coverage limits; avoid unnecessary Stripe routing in the general case; no purchases, sign-ins, or account changes.'),
  action('3. Canva edit/feedback composition','Question: does the explicit approval exception work in practice while preserving previews and message authorization? Decision: retain current composition or simplify duplicated procedure text.', 'Use mocked Canva responses for one typo fix and one approved batch of comments, including an unsupported font-family request and a responsive page. Compare current, simplified, and baseline workflows.', 'Exactly the approved edit scope; no unsupported operations; no repeated commit approval after a valid batch approval; no claim of saving before commit success; no reviewer replies without approved message scope.')],
 'test_later':[
  action('ai-prompt-orchestrator','Question: does the ten-reviewer process find consequential defects beyond a smaller review or baseline at acceptable cost?', 'After dependency resolution, use a synthetic small code repair and a responsive UI change with seeded functional and visual defects; compare original, simplified review, and baseline in isolated contexts.', 'Find seeded defects without regressions; validate evidence freshness; record actual timing and unknown telemetry honestly; preserve the single writer and privacy limits.', 'Locate and inspect the validator, resolve its working directory and plan contract, and approve any non-sensitive server submission required for a separate evaluation. Do not benchmark a missing helper.'),
  action('Unity version-specific design modules','Question: do the source-anchored constraints prevent library-specific mistakes for the versions Ethan actually uses?', 'Use a disposable fixture pinned to the relevant package: review tween cleanup during object disable or an Addressables handle-release path against known expected behavior.', 'Compile against the pinned version, pass the lifecycle checks, avoid mixing DOTween and PrimeTween APIs, and preserve package-specific constraints.', 'A concrete project/package version is selected and source anchors can be resolved. No project manifests were inspected for this audit.'),
  action('stripe-best-practices','Question: does the latest-version default cause an unnecessary migration during a small maintenance change?', 'Use a synthetic integration pinned to a known supported version and request a narrow webhook-handler repair; compare current instructions, compatibility-first wording, and baseline.', 'Make the requested repair without unrelated version changes; validate against current official docs and a local test fixture; use no live account or payment data.', 'An authorized Stripe maintenance task and pinned fixture exist; verify version facts then. The listed versions were not checked against live releases here.')],
 'keep':[
  action('Unity specialists and manual guidance','Keep version scopes, API pitfalls, discovery/dry-run conventions, and the distinction between teaching and automation.'),
  action('Security phases','Keep their distinct evidence and phase contracts; lexical similarity alone does not support consolidation.'),
  action('Canva transaction protocol','Keep previews, saved-versus-draft honesty, supported-operation checks, and the explicit single-approval composition exception.'),
  action('comfy and Data export helpers','Keep narrow local-workspace routing and source-preserving export workflows; disk discovery is not evidence of invocation.')]
}
extra=[s['path'] for s in inv['skills'] if s['activation_status']!='advertised in session']
report=dict(title='Ethan’s skill library — first-pass audit',
 coverage='2026-09-20. 163 SKILL.md files scanned: all 157 advertised paths plus 6 disk-discovered files. 0 read/parse errors; 0 exact duplicate groups; 16 lexical-overlap pairs; 717 instruction signals; 469 prose local-reference occurrences. One reference required manual resolution and is verified broken. Usage unknown.',
 summary='One verified link repair is proposed, not applied. One demo-skill relevance decision is yours to review. Three test groups are ranked next and three are deferred. No installed skills were changed, no conversation history was read, and no benchmarks or target workflows were run.',
 findings=findings, action_plan=plan,
 limitations=[
  'Static discovery is not exhaustive semantic review or proof of runtime health. Contextual evidence was inspected for '+str(len(reviewed))+' distinct skills; the remaining skills received automated scanning only. The 717 instruction signals were not all adjudicated individually.',
  'All 16 lexical pairs were reviewed at trigger/purpose level; deeper implementation equivalence was not tested. Fixed-step and approval language is a lead, not a defect.',
  'Advertised paths were reconciled with this session’s catalog. Additional disk files: '+ '; '.join(extra),
  'Only the advertised plugin versions were included, plus the local .codex/skills and .agents/skills roots and five sibling Data helper skills. Other cached versions, other user accounts, Claude directories, remote hosts, and custom roots outside this scope were not scanned. No cache ordering or runtime precedence was inferred.',
  'The scanner skips linked directories and uses conservative prose Markdown reference detection. Fenced code paths, tool dependencies, indirect references, remote URLs, and source-code citations are not comprehensively validated. Header validity does not guarantee host compatibility.',
  'No conversation logs, usage records, private personal-context capsules, project manifests, credentials, or account data were inspected. No skill invocation frequency or abandonment claim is available.',
  'No target scripts, services, benchmarks, external messages, payment operations, or live editor/design changes were executed. Only the audit scanner, report renderer, and local report validation ran.',
  'The orchestrator’s advertised tool was checked by metadata only; no server request was sent. Its helper could exist outside the inspected package, so the dependency concern remains unresolved.',
  'Underlying Unity, Canva, and Stripe API claims and current version tables were not independently revalidated; descriptions here characterize installed instructions, not guaranteed current platform behavior.',
  'Audit method: cth9191/skill-audit, commit c6e7079c822043ff0b67444dbed477dacc83ae77, retrieved from https://github.com/cth9191/skill-audit into a separate review workspace, not installed. The repository copy is excluded from library counts. Exact running model identifier and effort were not exposed reliably; no model comparison is claimed.',
  'Recommendations authorize no changes. Managed plugin caches should be repaired through an appropriate source/update path after a separate decision, not edited speculatively.'
 ])
(OUT/'audit.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
(OUT/'reviewed-paths.json').write_text(json.dumps(sorted(reviewed),indent=2),encoding='utf-8')
# Evidence and immutability checks are audit-output checks, not skill benchmarks.
for f in findings:
 for e in f['evidence']:
  assert Path(e['path']).read_text(encoding='utf-8-sig').splitlines()[e['line']-1]==e['excerpt']
for s in inv['skills']:
 assert hashlib.sha256(Path(s['path']).read_bytes()).hexdigest()==s['sha256'],s['path']
for key in ['test_next','test_later']:
 for a in plan[key]:
  assert a['task'] and a['success_criteria']
  if key=='test_later': assert a['prerequisite']
assert len(plan['test_next'])<=3
print(json.dumps({'findings':len(findings),'contextual_evidence_skills':len(reviewed),'unchanged_skill_hashes':len(inv['skills']),'actions':{k:len(v) for k,v in plan.items()}}))
