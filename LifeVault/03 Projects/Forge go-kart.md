---
type: project
status: planning
created: 2026-09-20
updated: 2026-09-21
schema: 1
---

# Forge go-kart

## Outcome and definition of done
Ethan wants to design and build his own **electric go-kart for paved use** through Hack Club Forge, aiming for Tier 1. Last stated design target: **September 30** (2026 inferred). **Build deadline is now flexible**: Ethan agreed October 12 can move; replacement date not chosen. Evidence: [[07 Journal/2026/09/2026-09-20 1705 Go-kart pitch preparation]]. These replace the earlier October 10 design target. Current requirements: **30 mph maximum, 45 minutes mixed riding, high-quality build and own CAD-designed frame**. The latest requested complete-kart budget target is **$1,200**, though the current all-new estimate is much higher; neither spending nor a budget increase has been approved. Source: [[07 Journal/2026/09/2026-09-20 2101 Sub-650 battery search]] and [[07 Journal/2026/09/2026-09-20 2125 Rolling chassis budget]]. Ethan expects to have most tools, but inventory and required purchases are not verified. Availability is **about 15 hours/week**, interpreting his reply in the context of the weekly-hours question. He also wants Forge's Hackaday Supercon reward.

Source: [[07 Journal/2026/09/2026-09-20 Go-kart scope revision]]. These are user goals, not approval, purchase authorization, or a finding of engineering/budget feasibility.

## Current state
**Read this first in a new task (handoff 2026-09-21):** The active design direction is Ethan's own Fusion-designed, welded frame with a candidate Kunray KR5V V2 72 V/5 kW motor kit and candidate Bomb Moto 72 V/30 Ah battery. Neither is purchased or fully verified. A provisional all-new BOM totals **$2,600.65** versus Ethan's **$1,200 target**; the critical decision is whether suitable existing/donor running gear exists or the budget/scope can change. Ethan's project-only height and weight inputs are stored below with specific permission. The **seated hip-to-heel measurement**, owned-parts inventory, battery documentation, and CAD geometry are still missing. The seat, pedals, axle, steering and brakes in [[03 Projects/Forge go-kart BOM#Current 72 V rolling-chassis budget — 2026-09-20]] are priced candidates/allowances, not selections proven compatible or safe. Last session: [[07 Journal/2026/09/2026-09-21 1553 Go-kart continuation handoff]].

### Driver fit input
Ethan reports a height of **5 ft 10 in** and weight of **155 lb** for this kart's fit, load and frame-design calculations. He specifically approved using and storing these measurements for that purpose on 2026-09-20. Treat them as project-specific self-reported inputs, not verified measurements or general health records. Source: [[07 Journal/2026/09/2026-09-20 2125 Rolling chassis budget#Driver-fit permission and measurement]].

2026-09-20 rolling-chassis budget: current all-new planning estimate is **$2,600.65 complete**, including the $599 Bomb Moto battery candidate and $389.90 Kunray kit. The frame materials, seat, brackets and pedals alone are about **$350.90**; the complete non-powertrain portion is about **$1,611.75**. This makes the $1,200 ceiling infeasible without extensive safe donor/owned running gear or a different powertrain/scope. Current priced breakdown: [[03 Projects/Forge go-kart BOM#Current 72 V rolling-chassis budget — 2026-09-20]]. This is planning, not purchase approval.

2026-09-20 30 Ah search: closest direct-buy match is Bomb Moto's **72 V 30 Ah battery at $599**, including a 5 A charger, Samsung 21700 cells, ANT Bluetooth BMS, protective casing and adapters. Bomb Moto recommends an 80 A tune and only warrants a 70 A tune; this still permits about 5.0 kW nominal input and matches the Kunray motor's rated 60 A / 5 kW class. It is the leading budget candidate, not purchase-approved: exact cell model, continuous-current rating, dimensions, weight, BMS settings, regeneration limit and UN 38.3/MSDS remain unpublished, and Bomb Moto's warranty page says six months for batteries while its FAQ says three months. Current stock showed five units. Evidence: [[07 Journal/2026/09/2026-09-20 2105 Thirty Ah budget battery search]].

### Earlier battery candidates and research history
The alternatives below remain research history. Bomb Moto is the current leading battery candidate; none is purchased or fully verified.

2026-09-20 budget correction: Ethan reaffirmed a **$1,200 total-kart ceiling** and asked for a battery below $650. The 40–45 Ah Chakra/Chi candidates are outside this build budget. Earlier sub-$650 candidates were HotPaxx 72 V 20 Ah packs ($549 shrink-wrap / $582 metal case, seller claims 130–150 A continuous) and MDPowerPacks' $499.99 metal-case 72 V 20 Ah pack (seller claims Samsung 50S, JK Bluetooth BMS and 100 A continuous). The HotPaxx metal-case pack was the stronger documented 20 Ah candidate, but it reduces projected mixed-riding runtime and leaves only $228.10 after the $389.90 Walmart motor kit. A complete all-new high-quality kart has not been shown feasible within the remaining amount. Donor/owned running gear would be required, or one of price, motor, or 45-minute runtime must change. Evidence: [[07 Journal/2026/09/2026-09-20 2101 Sub-650 battery search]].

2026-09-20 powertrain revision: Ethan wants the design built around the **Kunray KR5V V2 72 V / 5 kW motor kit with the 100 A Fardriver/Kunray NS18 controller**. This is a design selection, not a purchase. The prior QS138/Kelly path and the Blwny 50 A battery candidate are superseded for the active design. At that stage, 40–45 Ah 20S lithium-ion packs were explored: Chakra's 72 V 40 Ah EVE-40P metal-case pack and ChiBatterySystems' 72 V 45 Ah Pulsar. Those were later set aside for the under-$650, 30 Ah search. Evidence: [[07 Journal/2026/09/2026-09-20 2055 Kunray powertrain revision]].

Latest requirement: try for under **$1,200 complete**, with a **72 V 30 Ah battery rated at least 100 A continuous**; choose motor around it. This supersedes the previous 48 V proposal. Source: [[07 Journal/2026/09/2026-09-20 1811 Go-kart battery budget revision]]. Current feasibility research: [[05 Knowledge/Go-kart 72 V budget revision]]. No verified full build under this target found; donor-parts acceptance pending.

2026-09-20 earlier candidate: Ethan explored the Walmart Blwny-labelled **72 V 40 Ah LiFePO4 / 50 A continuous BMS** listing. Direct inspection of the listing and all six product images confirmed seller claims of **24S, 76.8 V nominal, 3,072 Wh, 87.6 V/5 A charger and 50 A continuous BMS**. The listing showed **$463.93**, 12.80 x 5.96 x 6.93 inches, 27.8 lb, Anderson and XT90 connections, a status display, Bluetooth monitoring, and a stated 12-month warranty; price is volatile and Walmart warns third-party warranty terms should be confirmed before purchase. Blwny's own product page was then inspected and conflicted materially: it lists **2,880 Wh**, explicitly calls the pack compatible with only **250–1,500 W motor systems**, advertises a **five-year warranty**, and shows UL/CE/RoHS badges without certificate identifiers. Its linked refund policy contains no five-year warranty terms, its warranty-registration page refers to a separate policy that is not linked, and its support pages do not supply a pack manual or datasheet. The domain was registered 2026-04-13, so the advertised five-year support has no long operating history. This is a historical candidate, not purchased. The **QS138 3 kW plus Kelly KLS8412S is not an approved match for this battery** unless Blwny gives written confirmation for a 3 kW traction controller and supplies the missing electrical/test documentation. Evidence: [[07 Journal/2026/09/2026-09-20 2047 Blwny manufacturer verification]]; research: [[05 Knowledge/Go-kart 72 V budget revision]].
### Forge program status
2026-09-20: Official Forge documentation and public implementation inspected at commit `0698312589e1d73487c02e6562f7bf3a2e7f4f8f`. Browser access failed twice before tabs could be read. Live shop state and program eligibility are unverified. Ethan subsequently reported **0 coins, 0 streak, and a need for Forge funding before ordering parts**. He confirms welding access and an experienced helper. Existing kart parts remain unknown; riding location remains undecided; runtime is now 45 minutes mixed riding. Ethan now targets approximately **30 mph**; source: [[07 Journal/2026/09/2026-09-20 1730 Go-kart speed target]]. Evidence: [[07 Journal/2026/09/2026-09-20 1658 Go-kart funding constraints]]. No project/pitch submitted, coins spent, or account changes made.

Research and arithmetic: [[05 Knowledge/Forge rules and coin forecast 2026-09-20]]. In particular, public code and prose differ about the daily streak requirement and the moment used for the payout streak. Keep these uncertainties visible.

## Next action
Measure Ethan's comfortable seated hip-to-heel reach with the knee slightly bent; inventory every reusable wheel, axle, hub, spindle, steering, brake and seat component. Use those facts to choose the frame envelope and replace the rolling-chassis allowances with exact parts and a local steel quote. Decide whether the working cap can move toward $2,400–$2,900 or which inspected donor components will reduce cost.

Before selecting the Bomb Moto pack, obtain its exact dimensional drawing and weight for CAD, exact Samsung cell model and 20S6P confirmation, continuous discharge rating, complete ANT BMS model/settings, maximum regenerative current, UN 38.3/MSDS, connector/wire ratings, and written clarification of the three-versus-six-month battery warranty. Use a 60 A commissioning limit and a 70 A design limit unless Bomb Moto provides written support for more. Inventory owned/donor mechanical parts because this $599 battery plus the $389.90 motor kit leaves only $211.10 before shipping/tax for the rest of the kart.

### Historical alternatives — only revisit if chosen again
Inventory every owned or freely reusable axle, wheels/tires, hubs, brake system, steering parts, seat, steel and electrical protection component. Use that inventory to determine whether the $1,200 ceiling can work with the $582 HotPaxx metal-case battery. If 45 minutes remains mandatory, do not release a 20 Ah pack as satisfying it: under an 85% usable assumption it permits only about 1.63 kW average input for 45 minutes. Obtain the HotPaxx dimensional drawing, exact BMS model/settings, UN 38.3/MSDS and regen-current limit before purchase.

For the active Kunray design, obtain written pack-specific evidence before purchase: exact full-charge voltage, charger output, cell model/configuration, continuous and peak discharge, BMS model, charge/regen limit, dimensions, weight, UN 38.3/MSDS, warranty, fuse/precharge details and dimensional drawing. Resolve the Chakra listing's **84 V required versus “87 V” charger-image conflict** and its two different dimension sets. Choose rear tire outside diameter, then calculate 420-chain gearing for a 30 mph electronic cap. Prefer the direct Kunray kit's pedal-throttle/420-sprocket configuration or replace the Walmart kit's half-twist throttle and #35 drive parts. Begin commissioning at conservative current limits with regen disabled until the pack charge-current limit is documented.

Before purchase, require Blwny to reconcile **2,880 versus 3,072 Wh**, **1,500 versus 3,500 W application limits**, and **five-year versus 12-month warranty** in writing. Obtain the exact cell maker/model and configuration, BMS datasheet, peak-current duration, low-voltage cutoff, balancing current, maximum charge/regenerative current, low-temperature charge behavior, UN 38.3 report, exact certification file numbers and model coverage, capacity-test evidence, dimensional drawing and actual weight. Do not finalize a 3 kW controller around this pack without that evidence. Confirm the QS motor's Hall/temperature-sensor pinout with Kelly and price the exact KLS8412S Hall-sensor variant plus programming cable only after the battery decision. Prioritize the 72 V budget revision above. The following 48 V BOM is a historical candidate configuration; reuse its component checklist, not its power-system selections.
Current working parts list: [[03 Projects/Forge go-kart BOM]] with adjacent CSV export. 56 rows; nine listed-price candidate lines subtotal $2,101.78, NOT full build cost. Proposed Golden Motor 48 V architecture; FP4852R0 52 Ah battery is currently out of stock. Exact wheels, electrical protection and CAD-dependent dimensions remain unresolved. This is a provisional sourcing BOM, not a released shopping list.
Confirmed: **Fusion** for CAD and **mostly flat paved terrain**. Evidence: [[07 Journal/2026/09/2026-09-20 1756 Go-kart CAD and terrain]].
Review [[05 Knowledge/Quality go-kart options 30 mph 45 minutes]]. Compare Golden Motor HPM3000B/VEC200 and QS138 V3 systems, with provisional 2–3 kWh battery packaging. Confirm design load/fit and country, then obtain exact battery and running-gear specifications. No runtime guarantee or final matched system. Old donor-budget scenario is superseded.

## Historical schedule — October 12 build target released
The following was the earlier compressed scenario. It is preserved for history, not the current build commitment. New schedule follows reviewed scope, sufficient approved funding and actual parts lead times.
About 15 hours/week yields roughly 21–24 available hours through September 30 and 47–49 total through October 12, depending on how today's time is counted. Use an illustrative allocation of 22 design hours and 26 build hours, not an agreed time budget or guaranteed sufficient workload. Approval, procurement and shipping consume calendar time separately.

| Dates (2026) | Work | Exit condition |
|---|---|---|
| Sep 20–21 | Requirements, owned-parts/tools inventory, rough priced BOM and Tier 1 pitch preparation | Affordable candidate scope, funding route and reviewer eligibility feedback; begin genuine work evidence. |
| Sep 22–26 | Ethan develops layout, component interfaces and CAD assembly | Driver fit, steering/brakes, drivetrain, battery, controls and mounting interfaces resolved enough for review. |
| Sep 27–29 | Independent review, corrections, final costing and submission files | Build-blocking issues resolved; editable CAD/STEP, BOM, README and genuine evidence complete. |
| Sep 30 | Target design completion and submission when ready | Complete reviewed design; approval and spendable coins remain external dependencies. |
| Oct 1–9 | Procurement and assembly only as approved funding, parts and safe reviewed design permit | Complete assembly with inspections; this window is not a delivery or approval forecast. |
| Oct 10–12 | Resolve issues and conduct staged checks/testing with experienced help | Verified working build; unfinished safety-critical issues move completion date. |

Feasibility is unresolved. If advance funding or shipping cannot fit, October 12 must move or the project scope/resources must change. Do not compensate by skipping review/testing or inflating logs.

## Engineering scope gates
- Electric propulsion and paved use are confirmed. Resolve private versus public use, driver envelope, design load, terrain, transport/storage and specific fabrication access before choosing components.
- Establish who can competently review the structure, welds/fasteners, steering, brakes, drivetrain guarding, and shutoff arrangement. This planning document is not a ride-safety signoff.
- Original engineering should come from Ethan. Reused reference parts and rated commercial components should be credited and justified; don't invent safety-critical hardware merely to chase a tier. Ask reviewers which purchased components are acceptable for this scope.
- No exact frame, steering, brake, motor, battery, or engine specification is approved yet. No claim that $400–650 can buy the finished configuration without a sourced BOM.
- Include all required parts and owned/reused parts in the replicable BOM; distinguish total replacement cost from new spending. Include shipping, tax, required fabrication, and necessary safety equipment in the feasibility calculation.
- Build an itemized landed-cost total after selecting compatible parts. The requested $1,200 complete-kart target remains current; do not treat the $2,600.65 planning estimate as Ethan approving a higher budget.

## Historical funding forecast
The former budget and coin targets below are historical. Recalculate after selecting a new BOM. Zero starting coins and funding-before-parts remain last confirmed; flexible price preference is not funding approval.
The Sep 30/Oct 12 forecast below is the historical compressed schedule. Build date is now flexible; new earning dates remain unset. The new parts worksheet is conditional and must not be treated as a quoted grant amount.
Public-source target: $400–650 of grant funding plus the 350-coin ticket needs **750–1,000 coins**, excluding travel and existing balance. At the stated availability, the current schedule does not generate that amount from zero.

Illustrative solo forecast (all hours accepted, Tier 1 design approved, guild multiplier 1, no other spending):

| Stage | Hours | Rate | Assumed streak at approval | Coins |
|---|---|---|---|---|
| Design by Sep 30 | 22 | 7.5/hour | 1.05 | 173.25 |
| Build by Oct 12 | 26 | 5/hour | 1.10 | 143.00 |
| Total after both approvals | 48 | mixed | conditional | 316.25 |

Without streak bonuses: 295 coins total. With the illustrative bonuses, shortfall against kart plus ticket is 433.75–683.75 coins before existing balance; design-stage shortfall for the kart alone is 226.75–476.75 coins. Build earnings cannot pay for parts that must be acquired first. Completion/submission dates do not guarantee approval dates or available funds.

From a zero streak starting Sep 20, Sep 30 is day 11 (5% bracket) and Oct 12 day 23 (10% bracket). Source implementation requires at least one logged hour per qualifying day, and captures streak at approval. These bonuses are conditional, not promises. Maintain only genuine activity; existing streak may change the forecast.

Zero balance and need for advance Forge funding are now confirmed. With the illustrative 5% design bonus, the kart alone requires 51–83 whole accepted design hours (400/7.875 and 650/7.875 rounded up); without bonuses, 54–87. That does not fit roughly 22 design hours by September 30. These are funding thresholds, not permission to pad the project or predictions of useful design workload. Next decision depends on timeline flexibility, genuine scope and owned parts. Possible adjustments are scope/cost reductions or a later build/reward timeline. Ticket availability remains unverified. Do not count the same coins for both parts and ticket.

## Authorship and recordkeeping
Forge's submission rules require original user design, and its journalling guidance says not to use AI to write journals. Codex's role here is research, tutoring, planning, calculation checks, and review. These private LifeVault notes are AI-assisted planning records, not Ethan-authored Forge devlogs or evidence of earned hours. Ethan should write his own actual progress and record genuine activity. Clarify allowable AI assistance with reviewers if uncertain.

## Questions awaiting Ethan
1. Which past projects can honestly be linked in the pitch, and which country should sourcing use?
2. Private paved property or public streets; comfortable seated hip-to-heel reach and final design load? Height/weight are saved for this project with permission. Fusion and mostly flat terrain are confirmed. Speed/runtime: 30 mph maximum, 45 minutes mixed riding.
3. Which kart parts are already owned, and what specific fabrication/review help can the experienced person provide?

## Questions for Forge staff before depending on funding
- Does this specific kart scope qualify for Tier 1, and which commercial safety-critical components are acceptable?
- Confirm current minimum daily activity and whether streak is assessed at submission or approval; public docs and code differ.
- Confirm Supercon reward availability, redemption deadline, exact housing/food coverage, eligibility/guardian arrangements if applicable, and whether a completed build is needed for that specific reward.
- Confirm review turnaround expectations and funding eligibility of shipping/tax/tool/fabrication costs.

No messages have been sent. These questions are preparation for Ethan, not permission to contact staff.

## Decisions and history
| Date | Decision or intent | Evidence | State |
|---|---|---|---|
| 2026-09-20 | Build own go-kart through Forge; aim Tier 1 | Current user request | user goal |
| 2026-09-20 | $400–650 project spending target | Current user request | entire project confirmed in scope revision |
| 2026-09-20 | Finish design by October 10 | Current user request | superseded by September 30 |
| 2026-09-20 | Seek Supercon shop reward | Current user request | not reserved or purchased |

| 2026-09-20 | Electric, paved use; about 15 hours/week; expects most tools | Scope revision | confirmed self-report; inventory unverified |
| 2026-09-20 | Design September 30; fully built October 12 | Scope revision | September 30 last stated design target; October 12 build target subsequently released |

| 2026-09-20 | October 12 build date can move; research parts and prepare pitch | [[07 Journal/2026/09/2026-09-20 1705 Go-kart pitch preparation]] | current; replacement date unset |
| 2026-09-20 | Candidate battery charger is 87.6 V/5 A and discharge rating is 50 A continuous | [[07 Journal/2026/09/2026-09-20 2030 Go-kart battery ratings confirmed]] | user-reported; battery not purchased |
| 2026-09-20 | Walmart listing inspected; advertised ratings are internally consistent, but required cell/BMS/test documentation remains missing | [[07 Journal/2026/09/2026-09-20 2040 Walmart battery listing inspection]] | candidate only; do not buy yet |
| 2026-09-20 | Blwny site conflicts with Walmart on energy, motor-power suitability and warranty | [[07 Journal/2026/09/2026-09-20 2047 Blwny manufacturer verification]] | 3 kW match blocked pending written technical evidence |
| 2026-09-20 | Build the active design around the Kunray KR5V V2 72 V / 5 kW kit and NS18 controller | [[07 Journal/2026/09/2026-09-20 2055 Kunray powertrain revision]] | current design selection; not purchased |
| 2026-09-20 | Entire kart must target $1,200; battery must be below $650 | [[07 Journal/2026/09/2026-09-20 2101 Sub-650 battery search]] | current budget; conflicts with all-new high-quality build and 45-minute target |
| 2026-09-20 | Prefer a 30 Ah pack at approximately the HotPaxx price | [[07 Journal/2026/09/2026-09-20 2105 Thirty Ah budget battery search]] | Bomb Moto $599 candidate leads; documentation checks pending |

## Latest requirements
Own frame and CAD focus confirmed. The **current** budget target is $1,200 complete ([[07 Journal/2026/09/2026-09-20 2101 Sub-650 battery search]]); the older flexible-budget statement in [[07 Journal/2026/09/2026-09-20 1739 Quality go-kart requirements]] is historical.

## Resume handoff
Last verified result: the current priced candidate BOM is [[03 Projects/Forge go-kart BOM#Current 72 V rolling-chassis budget — 2026-09-20]]; the user permitted project-specific height/weight storage. No frame dimensions, final fit, purchases, Forge pitch, or earned/spent coins are verified; Ethan last reported a zero balance and zero streak. Blockers: comfortable seated leg reach, inventory of reusable components, budget gap, battery/controller documentation and external Forge eligibility/funding. Next concrete action: obtain seated hip-to-heel reach and owned/donor parts inventory, then revise the CAD envelope and landed BOM. New-task session: [[07 Journal/2026/09/2026-09-21 1553 Go-kart continuation handoff]].

