# Shoulder yaw and object envelope study

Completed 2026-10-04 through user-authorized delegated Fusion modeling. All object and housing dimensions below are assumptions, not measurements or selected hardware.

## Changes

- Added `Left_Shoulder_Yaw` and `Right_Shoulder_Yaw`, each limited to ±70 degrees, with Rest disabled. Verified vertical rotation axes and combined yaw/pitch motion using measured world grip-center positions.
- Existing pitch and finger motions follow the yawed arm frames. Retained 304.8 mm link pivot spacing, lift travel and main envelope dimensions.
- Added 88 mm rotor and 100 mm outside / 91 mm inside diameter bearing-housing envelopes, 30 mm tall. These reserve space; bearing fits, transmission, shafts, fasteners and structural load paths are not designed.
- Added R50.5 mm carriage sweep reliefs and enlarged shoulder pitch reliefs to R35.5 mm. Cut operations explicitly target only the intended bodies. These are provisional geometry, not manufacturing tolerances or strength approval.
- Preserved the user's disabled lift Rest setting. Backed up the pre-edit assembly and current poses.
- 50 fully constrained sketches, healthy extrusion features, zero named user parameters.

## Assumed reference objects

| Reference | Dimensions | Purpose |
|---|---|---|
| Pillow block | X300 × Y400 × Z60 mm | Paired central approach; no deformation modeled |
| Box | X100 × Y60 × Z80 mm | Floor, carry and shelf approach checks |
| Bottle cylinder | Diameter60 × height220 mm | Central floor approach using yaw |
| Shelf | Depth400 × width1000 × thickness25 mm | Front edge X400; top Z1676.4 mm |

References are separate grounded components prefixed `10_ASSUMED_`; only references relevant to each pose are shown. Masses are unknown. The box is positioned 1 mm forward of the nominal grip center so its rear face clears the palm despite solver error; box/bottle approaches use 62 mm jaw opening for a nominal 1 mm side gap. These are pre-contact checks, not gripping simulations.

## Results

Five poses passed native solid interference checks including active objects and the shelf where applicable: paired pillow approach, central bottle floor approach, box floor approach, box carry and box resting at shelf height. Requested grip-center errors were under 0.35 mm. All robot solids were included; coincident faces excluded.

The first poses/path attempts exposed carriage sweep collisions, shoulder/forearm clearances and shelf conflicts. Geometry and poses were revised and checks repeated. The successful shelf route uses the negative elbow branch and these grip-center waypoints (all left-arm Y340 mm):

| Stage | Shoulder height | Grip X/Z |
|---|---:|---:|
| Floor | 400 mm | 450 / 50 mm |
| Carry | 900 mm | 400 / 900 mm |
| Retract and raise outside shelf | 900 mm | 300 / 1500 mm |
| Raise lift outside shelf | 1400 mm | 300 / 2000 mm |
| Advance above shelf | 1400 mm | 470 / 1950 mm |
| Lower to approach | 1400 mm | 470 / 1730 mm |

All 55 sampled positions across this route passed checks with a box envelope following the gripper and the shelf present. The route ends about 4 mm above the shelf; the resting box placement is checked separately as a static pose. It needs approximately 2.03 m overhead clearance including the box. This route demonstrates a geometric possibility and is not yet an efficient or dynamically validated trajectory.

Fourteen individual yaw checks (each side at −70, −50, −30, 0, 30, 50, 70 degrees, with the other arm folded at yaw0) passed robot interference checks. This does not establish that arbitrary simultaneous arm motions are safe. Discrete samples are not continuous collision certification.

## Unresolved grasp limitation

Both grippers can approach opposite sides of the central pillow, but their current closing axes are horizontal and the jaw opening is only 100 mm. This does not clamp the 400 mm wide pillow or its 60 mm vertical thickness. Wrist roll or another clamp orientation is needed before claiming a paired pillow grasp. Pillow softness, edge grasping, friction, pad compliance, forces and stable object support are not modeled.

## Files and next step

Pre-edit backup: `robot-before-shoulder-yaw-2026-10-04.f3d`.
Completed archive: `robot-yaw-object-study-2026-10-04.f3d`.
Evidence: `yaw-object-pose-checks-2026-10-04.json`, `yaw-motion-checks-2026-10-04.json`, `yaw-model-health-2026-10-04.json`.
Views: `yaw-paired-pillow-approach-preview.png`, `yaw-bottle-floor-preview.png`, `yaw-box-shelf-preview.png`.

Next: measure and weigh actual objects; choose wrist/clamp orientation for the pillow; reduce the shelf route's overhead requirement if needed; then size and package real loaded joints. No actuator selection or physical load validation occurred.
