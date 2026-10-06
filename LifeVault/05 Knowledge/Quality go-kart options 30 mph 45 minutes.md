---
type: research
status: provisional
created: 2026-09-20
updated: 2026-09-20
schema: 1
---

# Quality go-kart options — 30 mph and 45 minutes

## Question and scope
Strict evidence research, checked September 20, 2026. Requirements: Ethan's own CAD-designed/welded frame, 30 mph maximum, 45 minutes mixed riding, paved use, quality prioritized over the old $400–650 target. No replacement spending cap or purchase authorization. Fusion and mostly flat terrain subsequently confirmed: [[07 Journal/2026/09/2026-09-20 1756 Go-kart CAD and terrain]]. Country, design load and fit envelope remain unknown. Sources inspected directly; supplier claims do not independently establish reliability or performance.

## Answer
Compare a documented **3 kW-class motor/controller with roughly 2–3 kWh battery packaging space** first. Preferred CAD-first baseline: Golden Motor HPM3000B/VEC200. Alternative: QS138 70H V3/EM150. Consider 5 kW only if load/grade/acceleration/thermal calculations justify it. These are candidates, not an approved matched system or guaranteed speed/runtime.

Quality criteria: dimensional documentation, operating data, identifiable versions, service instructions and replacement parts. No independently verified brand reliability ranking is claimed.

## Claim ledger and motor options
All checked 2026-09-20. Prices are displayed USD component prices, excluding unquoted shipping/tax; rows are alternatives.

| Option | Direct evidence | Assessment / limits |
|---|---|---|
| Golden Motor HPM3000B + matching VEC200 | [Manufacturer](https://www.goldenmotor.com/eCar/frame-eCar.htm): 48/72V versions; listed $318 motor + $260 controller = $578; motor IGES/PDF, controller STEP and wiring links. | Preferred CAD comparison baseline, initially 48V. Battery, pedal, protection and drive hardware extra. Confirm ordered revision and voltage/current limits. |
| QS138 70H V3 + Votol EM150-2SP | [QS kit](https://www.cnqsmotor.com/product/qs138-70h-v3-3000w-motor-conversion-kit-with-votol-em-150-controller/): $493.85 displayed sale / $581 official; 3 kW label; 15T 428 adapter, controller, display and hand throttle; dimension images. | 72V-class alternative with reduction. Confirm pedal compatibility, wiring, rotation and settings. Motorcycle speed claims do not predict kart speed. Battery/charger extra. |
| Golden Motor HPM5000B + VEC300 | Same manufacturer page: $490 + $452 = $942. | Higher-power option if justified. Broad published ratings vary with version; avoid assuming identical output at all voltages. |
| E&C packaged QS138 V3 | [Official kit](https://electroandcompany.com/collections/kart-fabrication/products/qs138-70h-v3-3000w-em-150-kit): $1,399, sold out, 2–4 weeks stated lead time; harness/tuning, motor rated 3 kW continuous versus 28 kW burst claim, 2.35 reduction. | Integration-service alternative only with supplier-approved mild kart tune. Sprocket excluded; rotation restriction matters to layout. No need for the headline burst power here. |

Support: verified as supplier listings, with unverified final application suitability. Golden Motor's [48V dynamometer table](https://www.goldenmotor.com/hubmotors/hubmotor-imgs/HPM3000-48V3KW%20Data.pdf), dated 2014-12-31, reports roughly 3,180 W shaft output at 4,119 RPM and 3,458 W input. Useful historical manufacturer evidence, not proof of a current unit or 45-minute kart operation. Check current revision. Motor drawing PDF opened; native IGES/STEP links located but web parsing failed, so no claim those models were imported or validated.

## Battery calculation
45 minutes = 0.75 hours. Use 80% of nominal energy for an illustrative reserve/usable-capacity allowance, not a measured property or prescribed discharge limit.

Required nominal kWh = average battery-side kW × 0.75 / 0.80.

| Assumed average battery draw | Nominal energy required |
|---|---:|
| 1.5 kW | 1.406 kWh |
| 2.0 kW | 1.875 kWh |
| 2.5 kW | 2.344 kWh |
| 3.0 kW | 2.813 kWh |

These are sensitivity cases, not consumption predictions. The 2–3 kWh range is an initial comparison envelope. A hypothetical 48V×50Ah pack is 2.40 kWh; 72V×40Ah is 2.88 kWh. At 2 kW average and 80% usable, runtimes calculate to 57.6 and 69.12 minutes. At 3 kW, the 2.40 kWh example lasts only 38.4 minutes. Arithmetic checked by execution and reversing energy/time. Actual grade, mass, starts/stops, temperature and losses remain unresolved.

## Battery candidates and counterevidence
- **48V route:** seek an assembled traction pack around 2–3 kWh with documented discharge capability matched to the selected controller settings and approved full-charge voltage. No exact 48V pack passed all fit/current/documentation checks in this research. This remains a quote/specification request, not an orderable matched system.
- **Higher-voltage reference:** [E&C/Eon Lithium 76V 40Ah pack](https://electroandcompany.com/collections/batteries/products/high-power-76v-40ah-li-ion-battery), $1,889, lists 88.2V maximum, 300A continuous, approximately 40 lb and 8.25×6.25×11 inches. Nominal energy calculates to 3.04 kWh. Far more current capability than this concept needs. Not automatically compatible with the raw QS/EM150 kit or any 48V controller: confirm full-charge voltage, regen, protection, charger and connectors. No independent certification established here.
- **Reject BatterySpace BS-087 for this motor application:** [listing](https://www.batteryspace.com/lifepo4-battery-pack-51-2v-40ah-2048wh-with-bms-192.aspx) specifies 2.048 kWh but only ≤40A discharge, telecom-backup use and no UN38.3 testing. Energy capacity alone is insufficient.
- **Do not base the runtime target on E206:** [E&C E206](https://electroandcompany.com/products/e206-spec-karting-kit) is sold out and advertises 15-minute racing sessions, not this 45-minute use case.
- Allied's current commercial page emphasizes 105/168Ah versions despite older 65Ah search results. No stale 65Ah recommendation made.

Battery specification must cover actual cell configuration/full-charge voltage, continuous and timed peak current, BMS/cutoffs, temperature limits, mechanical protection, matched charger and connectors. Motor phase current is not battery current. Exact controller settings must respect all component limits.

## Mechanical package and CAD work
Own welded steel frame with purchased documented running gear is the proposed direction. No tube size, material grade, wall thickness, wheelbase, track or weld design is approved yet.

| Assembly | Candidate or design work |
|---|---|
| Brakes | [MCP 600505/600510 hydraulic kit](https://www.bmikarts.com/MCP-Hydraulic-Brake-Kit_p_581.html), $325.95 listing; caliper/master cylinder, rotor/hub, line/fluid. Match axle bore and rotor variant; pedal linkage and mounting still needed. Brake torque, heating and axle distribution require analysis for final mass. [Manufacturer service resources](https://www.mcpbrake.com/) available. |
| Axle, hubs, bearings | Choose one documented kart component family; match bores, keys, carriers, bearing mounts and retention. Diameter follows load review, not appearance. |
| Wheels/tires | Purpose-built kart assemblies matched to surface/load/speed and supplier-approved rim width. Actual tire outside diameter drives gearing. Exact SKU remains open. |
| Steering | Purchased spindles/kingpins/joints; original CAD defines supported column, geometry, clearance and stops. Check lock-to-lock movement. |
| Driver interface | Fit seat/pedals/floor to driver envelope; assess restraint/rollover approach together with experienced reviewer. |
| Drive | Correct shaft interface, sprockets/chain, adjustment and guard; include QS internal reduction exactly once in gearing. |
| Battery/controller | Model real mass, retention, connectors, cable bends, ventilation, impact protection and removal for service. |
| Electrical controls | Compatible returning pedal, drive inhibit, DC-rated protection/disconnect/contactor, precharge where required, matched charging and protected wiring; exact ratings pending. |

Ethan's CAD deliverables: packaging sketch, original frame and assembly, mounting plates, battery retention, motor adjustment, steering/brake integration, guards, manufacturing drawings and cut list. Include assumptions for loads/gearing/braking/energy, purchased-part references and review/test plan. FEA needs justified inputs and review, not merely a colored result plot.

## Pitch scope update — review draft
Idea: Custom CAD-designed electric go-kart for paved riding.

Proposed tier: Tier 1, subject to reviewer feedback.

I'm designing: My own welded frame and complete mechanical assembly, including driver fit, motor/battery mounts, steering/brake integration, chain adjustment, guards and service access. I plan to use commercial propulsion, battery and running gear, targeting 30 mph maximum and about 45 minutes mixed riding, to be checked through calculations and testing.

Why over $200: The original work is a buildable, documented vehicle assembly with engineered interfaces. I have welding access and an experienced helper for review.

Past projects: Ethan must add truthful examples. BOM: compare the sourced options above, then select battery and mechanical parts before giving a complete total. The old $628.45 scenario is superseded.

[Forge final-design requirements](https://github.com/hackclub/forge/blob/0698312589e1d73487c02e6562f7bf3a2e7f4f8f/docs/requirements/submitting.md) require original user design, complete assembly, source files, BOM and a sanity check. CAD can be the principal work; modeling purchased parts or copying a frame alone does not establish Tier 1. Reviewer decision remains open. Flexible price preference does not resolve funding before parts.

## Gaps and recheck
Need design load/fit envelope, riding location, country, past projects, final battery specifications and supplier compatibility confirmation. Recheck exact dimensions/revisions before detailed CAD, prices/stock before pitch/order. No components tested or external messages/purchases made.
