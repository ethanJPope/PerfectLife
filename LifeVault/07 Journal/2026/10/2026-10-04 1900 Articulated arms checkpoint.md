---
type: session
status: complete
created: 2026-10-04
updated: 2026-10-04
schema: 1
---
# Articulated arms checkpoint
Timestamp: 2026-10-04T19:00:34-07:00.
Source: current AP Research Fusion conversation. Ethan approved the arm/gripper plan: "ok you are good to go." Execution and checks directly observed through Fusion MCP; this is delegated work, not evidence of independent CAD mastery.

## Verified result
Saved articulated two-arm concept with direct numeric dimensions, geometric constraints, shoulder/elbow/wrist pitch joints and sliding padded finger envelopes. Zero named user parameters. 38 sketches fully constrained; extrusion features healthy. Pre-arm archive preserved. Final document verified saved as AP Research Robot - Concept v5, isModified=false, with floor/shelf/carry position snapshots.

Shoulder X120/Y±300 mm; forearm/gripper Y±340 mm. Two 304.8 mm links per arm plus 110 mm wrist-to-grip-center offset; two-foot centerline baseline does not include gripper length. Shared lift retains 400–1400 mm shoulder heights. Gripper pad opening verified 0–100 mm. Shoulder/elbow pitch limits ±150°, wrist ±180° are assistant concept choices, not final specifications.

Floor grip X450/Z50 mm, carry X400/Z900 mm, shelf X500/Z1726.4 mm: both arms reach within 0.35 mm numerical error. Native interference analysis found zero solid overlaps at all three poses, all 22 sampled transition positions, and 0/40/100 mm gripper opening checks. All solids included; touching faces excluded. No continuous path certification or physical task success inferred.

Corrected an observed Fusion cut-participant issue: default clearance cuts affected adjacent arm bodies. Recreated cuts explicitly scoped to intended component, then reran pose/transition/gripper/feature checks. Verified rendered pose views. Captured positions persist through snapshots; temporary Drive Joint values alone reverted after script execution.

## Limits and exact next action
No shoulder yaw; arms stay in separate sagittal planes. Cooperative central-object grasp not demonstrated. Housings/links/pads are envelopes; shafts, bearings, transmissions, actuator sizing, payload, stability, structural strength, cables and manufacturing unresolved. Shelf is only a height reference; no object or shelf solid in interference checks.
Next: select and weigh test objects, decide necessary inward shoulder motion, then develop real joint packaging and size loaded joints. Keep current dimensions provisional. No purchase or actuator selection occurred.

## Artifacts
Folder: D:/PerfectLife/AP Research/CAD.
- robot-before-arms-2026-10-04.f3d
- robot-articulated-arms-2026-10-04.f3d
- arms-floor-preview.png; arms-carry-preview.png; arms-shelf-preview.png
- arm-pose-checks-2026-10-04.json; arm-validation-2026-10-04.json
- arm-concept-report-2026-10-04.md
Project: [[03 Projects/AP Research robot design]]. Previous: [[07 Journal/2026/10/2026-10-04 1841 Mast and carriage checkpoint]].


## Live scale verification follow-up — 2026-10-04
User requested confirmation of scale after noticing blocky chassis/mast/carriage. Fresh Fusion MCP measurements confirm mm units; chassis 600×450×200 mm with underside Z75; mast 120×140×1325 mm from Z275 to Z1600; carriage 120×660×120 mm; lift travel1000 mm; all four arm pivot distances304.8 mm. Joint housings extend each link body to354.8 mm overall; pivot spacing, not bounding length, defines reach. Straight grip-center reach719.6 mm (28.33 in), fingertip reach749.6 mm (29.51 in), excluding40 mm lateral arm-layer offset. Thus the two-foot baseline excludes the gripper.
Live document remains v5 but isModified=true and arms/fingers are in changed asymmetric poses. No model changes or save performed during read-only verification; do not assume carry pose current or overwrite user changes. Numeric evidence: D:/PerfectLife/AP Research/CAD/live-scale-check-2026-10-04.json.
