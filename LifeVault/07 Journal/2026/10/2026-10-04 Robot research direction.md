---
type: session
status: active
created: 2026-10-04
updated: 2026-10-04
schema: 1
---
# Robot research direction
Recorded at: 2026-10-04T10:53:25-07:00
## Intent
Resume AP Research and discuss a revised general-purpose household robot design.
## Important user statements
Source: Ethan's voice conversation on 2026-10-04, paraphrased. Earlier thinking involved multiple specialized household robots. Ethan now wants to improve a general robot's physical design, questioning whether humanoid anatomy is necessary. Proposed changes: redesign torso, move arms vertically on a linear mechanism, and probably replace legs with a drivetrain. These are exploratory proposals, not a completed design.
## Work and verified results
Targeted LifeVault search found no earlier AP Research or humanoid notes. No old vaults consulted.
## Saved to
[[03 Projects/AP Research robot design]]
## Handoff
Next action: identify representative household tasks and whether stairs are required, then define measurable efficiency and comparison designs.

## Follow-up: vertical lift designs, verified 2026-10-04
Ethan asked whether vertically translating arm designs are used in homes or commercial settings.
- Stretch: 2021 design paper reports teleoperated and autonomous tasks in real homes: https://arxiv.org/abs/2109.10892 . Current Stretch 4 datasheet markets commercial/industrial indoor use and specifies a vertical lift: https://hello-robot.com/wp-content/uploads/2026/05/HelloRobot-DataSheet-Stretch-4-Rev5_AsLaunched.pdf . Different generations; do not conflate.
- Toyota HSR: original 2012 announcement specifies 500 mm shoulder-height travel and reports a 2011 trial in a user's home: https://global.toyota/jp/detail/1558047 . Toyota also reports a North American in-home trial in 2017: https://pressroom.toyota.com/retired-army-ranger-robot-sidekick-conduct-special-ops-toyota/ . Historical trials do not establish widespread household adoption.
- TIAGo: manufacturer describes research use; official hardware documentation specifies wheeled base and 35 cm torso lift: https://pal-robotics.com/robot/tiago/ and https://docs.pal-robotics.com/sdk/24.09/hardware/tiago/hardware-overview.html . A whole-torso lift differs from independently sliding arms.
Research implication (assistant inference): compare a defined mechanical change against these existing baselines; vertical lifting plus wheels alone is established prior art. Household purpose, home trials, and routine consumer deployment are distinct claims.

## Prototype scope clarification, confirmed 2026-10-04
Source: Ethan's subsequent voice statements today, paraphrased. Ethan proposes one shared carriage for both arms because it seems feasible to build in approximately six months. He wants the research framed around improving general robot design relative to humanoids and establishing a clear research gap. His belief that humanoids receive the most household exposure is a proposed framing premise, not a verified adoption fact; publicity, home demonstrations, and household deployment must be distinguished.

## Candidate household tasks, user-reported 2026-10-04
Ethan proposes tidying/interacting with household objects and tracking specifically user-designated items, such as reporting where keys were last seen. These are candidate functions, not a finalized test set or implemented capabilities. He requests additional household task ideas suitable for evaluating the design. No actual household locations, imagery, or item-tracking data collected.

## Interview outreach milestone, 2026-10-04
Source: Ethan's voice report today. Ethan reports sending the first email requesting an introduction for a robotics research interview. Delivery and response are not independently verified. He is preparing a second referral request. No recipient-identifying details stored.

## Outreach completed and design planning transition, 2026-10-04
Source: Ethan's voice report today. Ethan reports sending both outreach emails. The second draft requested a robotics interview referral and possible component/funding sponsorship. No sponsor commitment, funds, or response established. Ethan now wants to discuss actual design and possible budget ranges contingent on sponsorship. Next action: inventory existing hardware, tools, and fabrication access, then estimate staged prototype options with current component prices. No purchase authorized or made.

## Budget brackets and available resources, user-reported 2026-10-04
Ethan requests $500, $1,000, and $5,000 prototype planning brackets, dependent on possible sponsorship. Reports expected access to a Bambu Lab P2S printer in about three weeks (future access, not current completion), many small sensors/electronics but no LiDAR, limited/unclear metal fabrication access, and no suitable motors currently available. Existing computer, battery, motor drivers, camera specifications, structural hardware, and exact sensor inventory remain unverified. No purchases authorized.

## Preliminary reach and load targets, user-reported 2026-10-04
Ethan proposes starting with two feet of reach and a thirty-to-fifty-pound carried load. Unresolved: whether that load applies to one arm, both arms together, or carrying near the body rather than at full horizontal reach. These are tentative design targets, not established capabilities. Ethan questions whether suitable motors might cost around $50. Next action: clarify load distribution before actuator selection or a revised budget.

## Payload clarified, user-confirmed 2026-10-04
Ethan clarifies that the tentative thirty-to-fifty-pound payload is shared between both arms, not per arm. Two feet remains the tentative reach. Equal load sharing is an analytical assumption, not a guaranteed operating condition. At full horizontal reach and ideal equal sharing, payload-only static torque is approximately 40.7–67.8 N m per shoulder; arm mass, acceleration, uneven loading, and margin are additional. Next discussion: distinguish lifting at full reach from carrying close to the body.

## Actual task payload versus aspirational maximum, user-confirmed 2026-10-04
Ethan clarifies that thirty-to-fifty pounds shared between both arms is a desired maximum, not the normal training/test payload. Actual intended tasks involve small household objects such as pillows and miscellaneous floor clutter. Payload position depends on the object; maximum load at maximum reach is not a confirmed requirement. Two feet remains the tentative reach. Next action: select representative objects and measure their masses, dimensions, and pickup positions before sizing the first prototype. Do not silently convert the aspirational maximum into a required first-build capability.

## Tentative project availability, user-reported 2026-10-04
Ethan estimates three-to-five hours after school on weekdays (per day versus weekly total unclear) and five-to-six hours on weekend days. Most Saturdays through October 24 are occupied by an off-season FRC competition, except the next Saturday. Reports fall-break availability Wednesday through Sunday for focused work on this project. These are tentative availability estimates, not commitments or verified completed work. Next action: clarify weekday hours before estimating total weekly capacity. Use the break for task definition, measurements, inventory, and design planning while printer access remains expected in about three weeks.

## Availability clarified and main FRC season, user-confirmed 2026-10-04
Ethan confirms three-to-five hours each weekday, not weekly total. Weekend days remain estimated at five-to-six hours each, subject to previously stated Saturday constraints. During main FRC season, expects to reserve one weekday for this project; other weekdays are largely occupied by robotics/homework, while weekend availability remains the same. Exact main-season start and later competition-weekend constraints unknown. Derived arithmetic, not guaranteed commitments: normal weeks 25–37 hours; weeks with Saturday unavailable 20–31 hours; main-season weeks 13–17 hours if the reserved weekday retains 3–5 hours and both weekend days are available. Plan below maximum estimates and build/test core mechanics before main-season reduction.

## Long-term platform intent and availability correction, confirmed 2026-10-04
Ethan intends to continue developing the robot after the six-month AP Research project, potentially for a capstone next year. Wants mechanical/design headroom and broader future capability rather than a device tailored only to the research test. Believes training may be the main bottleneck; this is a hypothesis, not verified. No approval for a specific oversized actuator or heavy-lift first build inferred. Assistant proposal: reusable base and guided shared lift with replaceable arm mounts, interchangeable grippers, accessible power/control interfaces, and repeatable measurements; choose affordable first-build payload separately from future maximum.
Ethan clarifies availability remains flexible and he expects some build time during FRC. Off-season FRC ends after October 24; no FRC expected between then and main-season start. Winter break offers substantial additional time. Exact weekly commitments and main-season start remain unknown; prior suggested hours were planning assumptions, not user commitments.
Next action: agree on first-version design requirements and modular interfaces; define what comparative experiment tests without claiming superiority over all humanoids.

## Tilting mast proposal, 2026-10-04
Ethan asks whether the vertical elevator should pivot forward on a bottom joint to improve pickup of nearby floor objects. Exploratory proposal, not an adopted feature. Assistant recommendation: map floor reach and chassis interference with a fixed mast first; retain the possibility of an interchangeable mast mount. Tilting shifts upper-structure weight and adds gravity torque at the pivot; benefit depends on carriage height and arm geometry. Lower carriage positions get less forward displacement for the same mast tilt. Relevant primary precedent: Stretch design reports floor-reaching gripper with a vertical mast: https://arxiv.org/html/2109.10892v1 . This does not establish that Ethan's proposed geometry can reach the floor.

## Reference identified and taller lift proposal, confirmed 2026-10-04
Ethan visually identifies ROBOTIS AI Worker as the robot he remembers seeing on LinkedIn; exact original post remains unverified. Likes its layout and asks whether making the design taller could increase range of motion. Taller dimensions/lift travel are exploratory, not finalized. Official reference documentation: https://ai.robotis.com/ai_worker/hardware_ai_worker.html . Assistant recommendation: define low/high gripper targets and arm workspace first, preserve floor reach, and evaluate extra carriage travel rather than merely raising fixed arm mounts; check stability when raised. Next action: identify highest intended pickup/placement surface.

## Upper shelf target, user-reported 2026-10-04
Ethan tentatively proposes a highest shelf surface about five and a half feet above the floor (approximately 1.68 m). This is a target surface height, not a finalized mast height or lift stroke. Gripper/object clearance and arm orientation may require additional endpoint height. Shelf depth, opening clearance, carriage lower position, and arm geometry remain unknown. Next action: draw side-view workspace with floor pickup, 1.68 m shelf surface, tentative 0.61 m arm reach, and base interference; derive carriage travel before selecting lift hardware.

## Owned gearmotors identified, 2026-10-04
Ethan reports owning untested CQRobot 37D encoder gearmotors, confirms 70:1 option, and supplies https://www.amazon.com/dp/B08ZK97WLY . Retrieved product summary identifies 6V/12V 70:1 model with 64 CPR encoder, 150 RPM no-load at 12V, 27 kg cm stall torque at 12V (approximately 2.65 N m), and 5.5 A stall current at 12V. These are listing specifications, not measured performance or continuous ratings. Quantity, available driver, and continuous torque remain unknown. This refines the earlier statement of no suitable motors: some candidate motors are owned, but suitability is untested. Assistant assessment: evaluate for wheel drive first; guided screw lift or externally reduced/counterbalanced joints require sizing/testing. Encoder requires external motor driver and feedback control; not a complete smart servo.

## First visual concept and motor quantity, 2026-10-04
Ethan reports owning two brand-new CQRobot 70:1 encoder gearmotors; prior statement says untested. Asked for a quick exploratory image to check alignment with his vision. Built-in image generation produced a concept sheet with upright mast, shared two-arm carriage, sensor head, low wheeled base, raised and lowered poses. Preview file: C:/Users/ethan/.codex/generated_images/01a1080a-13ab-72d0-acb8-34d41d335b6d/exec-6bb0a56d-5de9-4953-a14a-b96d2b222f69.png . Image is illustrative, not verified geometry, load capability, motor selection, or manufacturing design. Generated wheels resemble mecanum rollers despite prompt requesting conceptual swerve; drivetrain remains undecided. Next action: obtain user's visual feedback and revise concept as needed.
