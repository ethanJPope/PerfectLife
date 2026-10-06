---
type: project
status: exploring
created: 2026-10-04
updated: 2026-10-04
schema: 1
---
# AP Research robot design
Retrieval aliases: AP Research; my AP Research; household robot research; AP Research robot project.
User-requested retrieval cue (2026-10-04): "pull in all the context for my AP Research." Load this complete note and the latest linked handoff; use the consolidated current decisions as the current-state authority and earlier entries as dated history. Bring forward design, parts, budgets, research protocol, artifacts, blockers, and next actions without treating tentative choices as confirmed.

## Outcome and definition of done
Investigate improving a general-purpose household robot's physical design over approximately six months, with continued development afterward. Proposed experiment: compare lightweight household pickup/placement with the shared arm lift enabled versus locked. Research question, literature gap, and final protocol remain provisional.
## Why this matters
Ethan's focus is general-purpose capability with efficient anatomy rather than a collection of task-specific robots.
## Current state
Latest delegated Fusion result directly verified 2026-10-04: AP Research Robot - Concept v6, saved and unmodified. Two arms now have vertical shoulder yaw (provisional ±70°), shoulder/elbow/wrist pitch and sliding padded fingers. Fifty sketches fully constrained, healthy extrusions, zero named parameters. Lift Rest remains disabled as Ethan set it.
Added provisional 88 mm yaw rotor / 100 mm bearing-housing envelopes, carriage sweep reliefs and shoulder pitch reliefs. Main chassis/mast/carriage dimensions and 304.8 mm arm link pivot spacing retained. Object assumptions: pillow300×400×60 mm, box100×60×80 mm, bottleD60×220 mm; actual sizes/masses unknown. Shelf solid top1676.4 mm added.
Five static/pre-contact object approaches passed interference checks, as did55 sampled positions of a staged box shelf route and14 individual yaw samples. Shelf route needs about2.03 m overhead and ends about4 mm above shelf; static resting placement checked separately. No continuous collision, stable grasp, payload, actuator, structure or stability validation.
Pillow paired approach is possible, but horizontal jaw closure cannot clamp its assumed400 mm width or60 mm vertical thickness; wrist/clamp orientation remains unresolved.
Latest session: [[07 Journal/2026/10/2026-10-04 1957 Shoulder yaw object study]]
## Next action
Measure and weigh actual objects; choose wrist roll or another clamp orientation for paired pillow grasp; reduce shelf route overhead if required; then design and size real bearings, shafts, transmissions and loaded joints.
## Blockers and open questions
Final test objects/payloads, mast height/stroke, base dimensions, thresholds/stairs, actuator selection, confirmed sponsorship, literature gap, and school protocol requirements remain unresolved. Proposed baseline is the same robot with lift locked; this does not establish superiority over humanoids.
## Decisions
| Date | Decision | Why | Evidence | State |
|---|---|---|---|---|
| 2026-10-04 | Refocus from specialized robots to improving one general robot | Better matches intended research goal | Latest linked voice session | User-confirmed direction; design tentative |
## Resources and artifacts
Existing related designs for later investigation: Hello Robot Stretch and PAL Robotics TIAGo. Their existence does not establish superiority of Ethan's proposal.
## History
Prior specialized-robot concept is known only from Ethan's current recollection; no earlier saved plan recovered.

## Current prototype scope, confirmed 2026-10-04
User-reported: one shared carriage for both arms; approximately six months available to build. Source: latest linked session, prototype scope clarification. Research emphasis remains improving general-purpose robot morphology relative to humanoid designs. Household prevalence of humanoids remains unverified and should not be used as an established premise. Next discussion: choose representative tasks and a feasible comparison baseline.

## Candidate tasks, confirmed 2026-10-04
User-proposed: tidying household objects; tracking user-designated objects and reporting their last observed location. Source: latest linked session, candidate household tasks. Test set remains open. Next action: select manipulation tasks that distinguish physical designs, with explicit success conditions and controlled software/control method; treat last-seen reporting as a separate perception/memory function unless coupled with retrieval.

## Outreach status, user-confirmed 2026-10-04
Ethan reports sending the first interview-referral email and is preparing another. Source: latest linked session, interview outreach milestone. No reply established. Next action: prepare second draft and continue narrowing task set and comparison baseline.

## Design and budget planning, user-confirmed 2026-10-04
Ethan reports both outreach emails sent; sponsorship remains pending and unconfirmed. Source: latest linked session, outreach completed and design planning transition. Wants design options and price ranges depending on sponsorship. Next action: inventory available parts and fabrication access before estimating a bench lift/manipulation test, mobile prototype, and full two-arm configuration using current prices.

## Resource and budget scope, confirmed 2026-10-04
User-requested planning brackets: $500, $1,000, $5,000, contingent on sponsorship. Expected printer access in about three weeks: user-described Bambu Lab P2S. Many small sensors/electronics reportedly available, excluding LiDAR; no suitable motors currently available; metal fabrication access limited/unclear. Source: latest linked session, budget brackets and available resources. Next action: define arm reach and object payload before selecting actuators; verify exact inventory and use current vendor prices for a complete bill of materials.

## Preliminary mechanical requirements, confirmed 2026-10-04
Tentative user targets: two feet of arm reach; thirty-to-fifty-pound payload. Source: latest linked session, preliminary reach and load targets. Payload per arm versus combined and payload position remain unknown. These requirements supersede assuming only lightweight tabletop objects; prior compact prototype budget scopes do not establish feasibility at this load. Next action: clarify payload distribution, then calculate joint torque including arm mass and base stability before pricing actuators.

## Payload clarification, confirmed 2026-10-04
Thirty-to-fifty pounds is the combined two-arm payload; tentative reach remains two feet. Source: latest linked session, payload clarified. This resolves the earlier per-arm versus combined ambiguity. Full-extension load requirement remains unconfirmed. Next action: determine whether full payload must be lifted at maximum reach or only carried close to the torso, then size joints and stability.

## Task scope clarification, confirmed 2026-10-04
Actual training/test tasks: small household objects, including pillows and miscellaneous floor clutter. Thirty-to-fifty-pound combined lifting capacity is an aspirational maximum, not the typical task load or a confirmed first-prototype requirement. Full-load position depends on the object. Source: latest linked session, actual task payload versus aspirational maximum. Next action: select and weigh representative test objects, retaining two feet as tentative reach, then price actuators for this test envelope separately from future heavy-load upgrades.

## Tentative availability, confirmed 2026-10-04
User estimates weekday after-school work at three-to-five hours (per-day versus total unclear) and weekend days at five-to-six hours. Most Saturdays through October 24 occupied by off-season FRC, except next Saturday. Fall break offers Wednesday-through-Sunday focused project availability. Source: latest linked session, tentative project availability. Next action: clarify weekday-hours interpretation, then scope a realistic six-month plan with reserve time for experiments and writing.

## Availability clarification, confirmed 2026-10-04
Weekday estimate is three-to-five hours per day. Main FRC season reduces project weekdays to one reserved weekday, with weekend estimates unchanged. Source: latest linked session, availability clarified and main FRC season. Earlier per-day ambiguity is resolved. Main-season start and competition-weekend exceptions remain unknown. Next action: front-load core mechanics and preserve testing/writing capacity under reduced main-season availability.

## Long-term platform goal, confirmed 2026-10-04
User intends continued development beyond AP Research, potentially a capstone next year. Wants future mechanical headroom and general-purpose potential rather than optimizing exclusively for current test objects. Training as dominant bottleneck remains a user hypothesis. Source: latest linked session, long-term platform intent and availability correction. Next action: define first-version requirements and upgrade interfaces, pricing initial capability separately from future heavy lifting.
Availability correction: user expects flexible build time during main-season FRC; no concrete hours committed. Off-season ends after October 24, with no FRC expected until main season; winter break offers extra availability. Earlier assistant planning-hour targets are estimates only.

## Candidate mast pivot, 2026-10-04
User proposes bottom-mounted forward tilt joint for the mast to assist nearby floor pickup; not yet adopted. Source: latest linked session, tilting mast proposal. Next action: sketch side-view floor reach and base interference with upright mast before deciding whether tilt adds useful workspace sufficient to justify torque, structural, and stability costs.

## Reference morphology, confirmed 2026-10-04
Ethan identifies ROBOTIS AI Worker as the remembered inspiration and likes its overall layout. Exact LinkedIn post not established. Proposes a taller version for more range of motion; dimensions remain open. Source: latest linked session, reference identified and taller lift proposal. Next action: specify highest target surface and lowest floor pickup geometry before choosing mast height and lift stroke.

## Vertical workspace target, confirmed 2026-10-04
Tentative upper shelf surface: five and a half feet (approximately 1.68 m) above floor, while preserving floor pickup. Source: latest linked session, upper shelf target. Robot/mast height and carriage travel remain undetermined; arm geometry, object clearance, shelf depth, and chassis interference must be included. Next action: sketch side-view workspace to derive low/high carriage positions and lift stroke.

## Existing actuator inventory correction, confirmed 2026-10-04
User owns untested CQRobot 37D encoder gearmotors, 70:1, supplied Amazon listing identifies 6V/12V version: https://www.amazon.com/dp/B08ZK97WLY . Source: latest linked session, owned gearmotors identified. Quantity and motor drivers unknown. Earlier no-suitable-motors statement is refined: candidate motors exist, suitability unverified. Next action: determine quantity and driver availability, then test one motor under controlled load before assigning it to the base, lift, or arm.

## Visual concept milestone, 2026-10-04
User reports two brand-new owned CQRobot gearmotors (untested). First brainstorming image generated to check vision alignment; user acceptance pending. Source and image location: latest linked session, first visual concept and motor quantity. Next action: review shared carriage, mast, arm proportions, and base with user; wheel type remains undecided.

## Consolidated current decisions and handoff — 2026-10-04
Source: Ethan's messages and voice transcripts in this chat, plus verified tool outcomes; captured in [[07 Journal/2026/10/2026-10-04 1703 Robot design handoff]]. User explicitly requested saving all important project information. This section supersedes earlier unresolved details where clarified; earlier sections remain chronological history. Last confirmed 2026-10-04; recheck changing prices and status before use.

### Adopted direction versus provisional targets
- General-purpose household platform, not a collection of specialized robots. Six-month AP Research deliverable should be achievable independently of broad autonomy; continue afterward, possibly as a capstone.
- User accepted overall concept image. Its differing mast lengths were a generation inconsistency: intended mast is FIXED height; only shared carriage moves. Telescoping and forward-tilting mast are not adopted.
- Two articulated arms on ONE shared vertical carriage; padded two-finger grippers accepted for initial project. Interchangeable fingertips and replaceable arm mounts preserve upgrade options.
- Differential drive first, swerve potentially later once funding is known. User has carpet and wood flooring. Threshold heights, stair requirements and actual motor suitability unknown. Swerve single-module feasibility test was discussed but is not the current first-build direction.
- Approximately 0.61 m / two-foot arm reach and 1.68 m / 5.5-foot shelf surface remain tentative targets; not mast height or validated workspace. Preserve floor pickup.
- Normal tasks: pillows and lightweight floor clutter. Fetch/deliver and lightweight two-arm box movement were assistant suggestions, not a finalized task set. Tracking keys/last-seen locations is a separate sensing feature, not the main morphology experiment.
- Future 30–50 lb COMBINED load is aspirational, not first-build requirement. Training as main bottleneck is a hypothesis. Manual control first can isolate mechanical performance.

### Proposed research and data
Assistant-recommended question: effect of shared vertical carriage on success and completion time moving lightweight household objects between heights, compared with fixed carriage on SAME robot. User discussed this direction; final adoption/protocol and novelty require literature review and school guidance.
Conditions: lift enabled versus locked at pilot-selected fixed height; same objects, arms, grippers, starting positions, control method. Repeat object/height combinations, alternate condition order, include failures and predefine success/timeout.
Record success/failure, completion time, drops, regrasp attempts, base repositioning, object and pickup/placement heights, failure reason. Potential tasks: floor-to-bin, table-to-surface, low-to-high shelf within demonstrated capability. No unsupported claim of humanoid household prevalence or superiority.

### Hardware inventory and compute
- TWO brand-new, untested CQRobot CQR/37D 70:1 encoder gearmotors. Listing https://www.amazon.com/dp/B08ZK97WLY : at 12 V, 150 RPM no-load, 27 kg·cm (~2.65 N·m) stall torque, 5.5 A stall current, 64 CPR motor encoder. Listing values, not continuous ratings or measurements. Candidate differential-drive motors; no loaded tests performed.
- FOUR HW-039 boards; user read BTS7960B markings. Candidate brushed-DC H-bridges, normally one board/motor; actual authenticity, thermal/current capability and logic interface unverified. Advertised 43 A chip current limitation is NOT a continuous module rating. Encoders connect to microcontroller separately. L298N also owned and rejected for loaded base because current/voltage losses unsuitable for listed motor stall demand.
- Temporary battery user identified NPW36-12, 12 V sealed lead-acid; multimeter reading user-reported 12.4 V. Not selected as final battery. Resting voltage alone does NOT prove battery health or load capability (corrects frontend's stronger 'healthy' assertion). User chose CAD instead of bench testing; no successful test inferred. Wiring/fuse/current checks pending.
- Jetson Orin Nano planned as main computer; user expects funding, not received/guaranteed. Jetson for perception/planning/logging; separate microcontroller for encoders, motor commands, limits and communication-loss handling. Microcontroller model not selected.
- Existing small sensors/electronics reportedly abundant; exact inventory unknown. Camera/depth-camera options, lift limits, wheel/joint feedback, regulated power needed. LiDAR postponed; no camera chosen. Local inference is a goal, not guaranteed training or model performance.
- Bambu Lab P2S access expected about three weeks after discussion; not confirmed arrived. Limited/unclear metal fabrication. User also owns SO-101 and reports servos stall too early for desired loads; this is user experience, not an established defect diagnosis.

### Budget and actuator research (estimates, not purchases)
Funding brackets $500/$1,000/$5,000; sponsorship pending, no award or purchase established. User initially targets $50–$100/motor while reserving compute. Original $5,000 allocation: arms/grippers $800; lift $600; base $500; power $400; compute $550; vision $300; printing $250; mechanical hardware $300; controls/wiring $200; research setup $100; tax/shipping $400; contingency $600. Total $5,000. Printing allowance: eight 1 kg rolls at assumed $25 plus $50 supplies. This is a planning envelope, not full quoted BOM; excludes printer purchase/labor/paid fabrication/training workstation and future heavy-load capability.
Later AR4 research suggests exploring $1,400–$1,600 arm-actuation allocation instead of $800; whole budget must be rebalanced, not silently increased. No actuator selected.
- ST3215 ~$21.99: small-joint/gripper test candidate; advertised stall torque not continuous.
- XL430 ~$27.50, listed sold out; manufacturer estimated continuous 0.28 N·m, limited loads.
- StepperOnline geared NEMA23 20:1 ~$47 motor only; encoder version 23HS22-HG20-E1000 $73.28 plus driver, listed <=1.6° no-load backlash. Gearbox permissible torque not continuous motor output.
- CubeMars AK45-36 V3.0 $185.90, listed sold out: upgraded candidate; detailed torque/thermal/holding validation pending.
- Jetson Orin Nano Super manufacturer list $399 as checked 2026-10-04; availability recheck required.
Evidence: AR4 publishes 26-inch reach, 1.9 kg payload; StepperOnline complete six-axis motor/driver/power package listed $699 (~$117/joint average, not individual price), excludes structure/controller/gripper. https://anninrobotics.com/docs/what-are-the-dimensions-and-key-specifications-of-the-ar4-robot/ ; https://www.omc-stepperonline.com/custom-kits . Stronger reference than small SO101, not verified endurance or transferable custom-arm rating.
PARA paper reports 2 kg at 940 mm with expensive ClearPath servos; proposed $100 stepper substitution was not demonstrated equivalent performance. https://pmc.ncbi.nlm.nih.gov/articles/PMC9123426/ . Builder tests showed printed reducers/inserts can deform/fail; full joint bearings/transmission matter. Single loaded shoulder test recommended before buying full set; repeat motion/holds and log current/temp/sag/backlash within manufacturer limits. Suggested 100-cycle screen is our proposal, not lifetime certification.

### Design artifacts and completed work
Fusion 360 chosen; Hybrid Design for internal components/joints. No detailed CAD assembly completed.
FigJam board: https://www.figma.com/board/5qoofGVXb12s6bk6IaQpLA/Untitled . Verified edits: raster three-pose storyboard (floor pickup/carry close/shelf placement); editable notes comparing central mast/rear mast/wider shoulders; prototype/research notes; actual manufacturer reference images and source links for ROBOTIS AI Worker (upper body), PAL TIAGo Pro, Hello Robot Stretch 4 (four poses). These are accurately labeled reference variants; not all identical to earlier referenced robots. Layout alternatives are descriptive notes, not separate CAD/rendered designs. Sharing settings unchanged.
Proof screenshots: D:/PerfectLife/figjam-robot-concept-proof.jpg ; D:/PerfectLife/figjam-robot-reference-images-proof.jpg . Storyboard is concept, not validated geometry.

### Previous Fusion blocker — superseded by CAD-start update below
Fusion repeatedly froze at 'Signing in' / Not Responding. Ending process/relaunch did not resolve; Service Utility opened via Settings > Apps > Installed apps > Autodesk Fusion > Modify. Network Diagnostics showed all listed checks green, including sign-in endpoint (does not prove full authentication works). User reports Repair finished but startup froze again. User reports NO unsaved/unsynced Fusion designs. Assistant instructed Reset next; completion NOT confirmed. Resume by asking whether Reset completed and whether Fusion gets past sign-in; do not claim fixed or repeat repairs blindly. Service Utility proof: D:/PerfectLife/fusion-service-utility-proof.png . Once resolved, begin Hybrid concept assembly starting with base footprint, then mast/shared carriage, arms/grippers and low battery/Jetson space.

## Latest CAD-start update — 2026-10-04
Current milestone: [[07 Journal/2026/10/2026-10-04 1957 Shoulder yaw object study]]. Saved v6 has shoulder yaw, reference objects/shelf and checked approach/path samples; earlier checkpoints below are history.
Current milestone superseding earlier entries: [[07 Journal/2026/10/2026-10-04 1900 Articulated arms checkpoint]]. Saved v5 includes articulated arm/gripper envelopes and verified pose snapshots. See Current state and latest checkpoint for current dimensions and limits; v3/v2 details below are history.
Current milestone superseding the chassis-only checkpoint below: [[07 Journal/2026/10/2026-10-04 1841 Mast and carriage checkpoint]]. Saved v3 has root-level 02_Mast_Envelope and 03_Shared_Carriage; base pinned, mast rigidly attached, carriage slider limited to +/-500 mm around 900 mm rest shoulder height. Mast spans X -160..-40, Y -70..70, Z 275..1600 mm. Beam spans X -40..80, Y -330..330, rest Z 840..960 mm. Four fully constrained two-link reach studies use 304.8 mm links, shoulder Y=+/-300 mm, and floor/shelf grasp centers 50 mm above each surface; they are not manufactured arm parts. Both sample targets geometrically reachable; real joints/grippers, task objects, dynamics, payload, stability and trajectories unresolved. See latest session for complete assumptions, interference evidence and archive paths. These assistant choices are not final user-confirmed specifications.
Latest verified result: built-in Autodesk Fusion MCP enabled by Ethan and successfully connected at http://127.0.0.1:27182/mcp. User-authorized delegated modeling created root-level 01_Base_Envelope with Base_Profile (four linked projections) and Chassis_Width_450mm symmetric extrusion, body Chassis_Envelope. Verified bounds in mm: X -300 to 300, Y -225 to 225, Z 75 to 275; one solid, healthy extrusion, fully constrained source and projected sketches, zero user parameters. Original nine construction lines preserved. Saved document verified as AP Research Robot - Concept v2 with isModified=false. Isometric camera fitted for user. Next: mast placement/shared carriage travel and reach geometry; no structural or load validation implied.
Artifacts: D:/PerfectLife/AP Research/CAD/robot-before-chassis-2026-10-04.f3d (pre-edit backup); D:/PerfectLife/AP Research/CAD/robot-chassis-envelope-2026-10-04.f3d (completed geometry archive); D:/PerfectLife/AP Research/CAD/chassis-envelope-proof.png (verified isometric preview). MCP execution used standard local HTTP initialize/tools-list/tools-call requests because the new server was not yet exposed in the current chat's native tool catalog; future sessions can rediscover it. See linked session for tool details.
Latest milestone: screenshot codex-clipboard-4f2d5de5-1e8b-4ad5-8af1-403afe76d1a7.png verifies the 600 x 200 mm chassis envelope, 75 mm floor clearance, and corrected 1676.4 mm floor-to-shelf dimension. Earlier setup-only state below is historical. Full constraint status, width change-test, final sketch naming/save and any 3D body remain unverified. Next: finish/save layout and create first 3D chassis packaging envelope. Learning evidence: [[06 Learning/Fusion robot CAD]].
Source: [[07 Journal/2026/10/2026-10-04 1715 AP Research CAD start]]. User explicitly reports Fusion issue fixed and requests best practices beyond dimension tables. Prior Fusion blocker is superseded; exact repair method unknown. Initial setup verified below; no layout geometry completion established.
Assistant recommends a Hybrid layout/skeleton first: simple side/top sketches to establish reach and hardware envelopes, then components and joints, then detailed manufacturing features.
Latest user clarification (2026-10-04): Ethan dislikes parameters and wants design best practices without them. Use direct numeric sketch/feature dimensions and geometric constraints; omit named user parameters and parameter-table setup. Continue batched instructions. This supersedes the assistant's parameter-table exercise, not the prior layout dimensions (which remain unvalidated placeholders).
Progress: screenshots verify AP Research Robot - Concept v1 saved, Hybrid/mm setup, active 00_Layout and empty XZ sketch; user confirms 3D Sketch unchecked. No layout geometry completion confirmed. Ethan explicitly prefers complete batches of CAD steps and review afterward instead of per-click checks. Latest source and next batch: [[07 Journal/2026/10/2026-10-04 1715 AP Research CAD start#Progress and teaching preference — 2026-10-04]]. Proposed 600 mm base length, 200 mm body height and 75 mm clearance are assistant layout placeholders only, not requirements or validated dimensions.



