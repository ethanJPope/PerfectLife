# Articulated arm concept checkpoint

Completed 2026-10-04, Phoenix time. User-authorized delegated Fusion modeling.

## Geometry and motion
- Two 304.8 mm links per arm; 609.6 mm link-center reach plus 110 mm wrist-to-grip-center offset. Finger tips extend 140 mm beyond the wrist. This exceeds two feet if the gripper is included.
- Shoulders at X120, Y±300 mm; shared lift supplies shoulder heights 400–1400 mm. A 40 mm forward standoff was added to the carriage front.
- Forearms and grippers run in Y±340 mm lanes, with 40 mm lateral separation between upper-arm and forearm layers.
- Shoulder and elbow pitch limits ±150 degrees; wrist pitch ±180 degrees. These are provisional envelope limits, not actuator specifications. No shoulder yaw or wrist roll.
- Each gripper has two sliding fingers and separate padding envelopes. Verified pad-to-pad opening: 0, 40 and 100 mm.
- 20 root component occurrences, 18 as-built joints, 38 fully constrained sketches; healthy extrusion features and zero named user parameters.
- Pivot housings and clearance reliefs are concept envelopes. Shafts, bearings, transmissions, bolts and pad material are not designed. Cut participants explicitly restricted to the intended component.

## Checks
| Pose | Shoulder height | Requested grip center X/Z | Result |
|---|---:|---:|---|
| Floor | 400 mm | 450 / 50 mm | Both grip centers within 0.35 mm; zero solid overlaps |
| Close carry | 900 mm | 400 / 900 mm | Both grip centers within 0.1 mm; zero solid overlaps |
| Shelf | 1400 mm | 500 / 1726.4 mm | Both grip centers within 0.15 mm; zero solid overlaps |

All 22 sampled positions across the floor-to-carry and carry-to-shelf joint interpolations had zero solid overlaps. These samples include all solid components, including both arms, fingers and pads; coincident faces excluded. This is not continuous collision certification. Shelf height 1676.4 mm is a reference; no shelf solid or manipulated object was included. Gripper opening checks also had zero solid overlaps.

The arms currently move in separate sagittal planes. Cooperative grasp of a central object is not demonstrated; shoulder yaw or another lateral motion will need consideration. Payload, motor torque, stability, structural strength, cables and manufacturing remain unverified.

## Artifacts
- `robot-before-arms-2026-10-04.f3d`: pre-edit backup.
- `robot-articulated-arms-2026-10-04.f3d`: completed assembly archive.
- `arms-floor-preview.png`, `arms-carry-preview.png`, `arms-shelf-preview.png`: verified pose views.
- `arm-pose-checks-2026-10-04.json`, `arm-validation-2026-10-04.json`: numeric evidence.

Next: select and weigh representative objects, determine whether inward shoulder motion is needed, then develop actual bearing/shaft/actuator packaging and size the loaded joints.
