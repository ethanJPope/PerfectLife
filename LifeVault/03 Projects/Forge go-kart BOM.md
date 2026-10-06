---
type: research
status: provisional
created: 2026-09-20
updated: 2026-09-20
schema: 1
---

# Forge go-kart working BOM
**Power-system selections superseded:** Ethan now specifies 72 V 30 Ah >=100 A continuous and a target below $1,200. See [[05 Knowledge/Go-kart 72 V budget revision]]. The component checklist remains useful; this 48 V table and its CSV are historical candidate pricing, not the current selected architecture.

## Current 72 V rolling-chassis budget — 2026-09-20
This is the active planning estimate for a custom welded frame around the $599 Bomb Moto 72 V 30 Ah candidate and $389.90 Kunray KR5V V2 kit. It is not a purchase list. Exact frame steel, steering geometry, braking hardware, tire size and electrical protection depend on driver fit and reviewed CAD. Current online prices were rechecked on 2026-09-20; allowances require local quotes or final part selection.

Driver-fit input: Ethan reports **5 ft 10 in and 155 lb**, with specific permission to use and store these measurements for this kart. For preliminary Fusion packaging, reserve an adjustable pedal range rather than fixing the pedals from height alone. The next required measurement is comfortable seated hip-to-heel reach with the intended seat angle and the knee slightly bent. Do not release seat rails, pedal mounts, steering-wheel position or frame cut lengths until a physical mock-up confirms reach and clearance.

| Group | Planning choice | USD | Evidence / limit |
|---|---|---:|---|
| Battery | Bomb Moto 72 V 30 Ah candidate | 599.00 | Candidate only; missing specifications and warranty conflict remain unresolved |
| Motor/controller | Kunray KR5V V2 72 V 5 kW kit | 389.90 | Candidate listing price; exact contents and interfaces still require confirmation |
| Frame materials | Tubing, plate, floor, gussets and mount stock | 180.00 | Planning allowance; obtain a local cut-list quote after CAD review |
| Seat | OMB/Azusa bucket seat with hardware, no brackets | 81.95 | [Supplier](https://www.ombwarehouse.com/bucket-seat-with-mounting-hardware-only-no-brackets.html); 18.5 x 19 x 18 in; fit not confirmed |
| Seat bracket stock/hardware | Custom welded brackets and fasteners | 20.00 | Planning allowance; geometry depends on driver fit |
| Pedals | BMI mechanical gas/brake pedal pair | 19.95 | [Supplier](https://www.bmikarts.com/Gas-Brake-Foot-Pedal-Set_p_3729.html); use one as the brake pedal; fits tubing up to 1 in |
| Accelerator | Kelly 0–5 V Hall pedal | 49.00 | [Supplier](https://kellycontroller.com/shop/kelly-0-5v-throttle-pedal/); 0.8–4.2 V output; NS18 pinout/compatibility unverified |
| Rear running gear | GoPowerSports 6 in live-axle kit | 320.95 | [Supplier](https://www.gopowersports.com/6-live-axle-kit/); includes 36 in axle, bearings/hangers, rear wheels/tires, 60T #41/420 sprocket and band brake |
| Steering | GoPowerSports complete steering kit | 214.95 | [Supplier](https://www.gopowersports.com/go-kart-steering-kit-complete/); dimensions must match final frame and Ackermann layout |
| Hydraulic brake | BMI caliper/master-cylinder/hose kit plus compatible rotor/hub allowance | 119.95 | $74.95 [supplier kit](https://www.bmikarts.com/Hydraulic-Brake-Kit_p_2856.html) + $45 provisional rotor/hub; mount design and stopping analysis required |
| Front wheels/tires | Matched pair | 80.00 | Planning allowance; select after spindle, load and rolling-diameter decisions |
| Drive parts | #420 chain, links/tensioning and chain guard | 65.00 | Planning allowance; final length and ratio require motor RPM and tire diameter |
| Electrical safety/wiring | DC-rated fuse/holder, contactor or disconnect, precharge, cable, lugs, loom and small control parts | 180.00 | Planning allowance; release only after controller and battery fault/current data are known |
| Assembly/finish | Fasteners, welding/cutting consumables, paint and small hardware | 100.00 | Planning allowance; inventory owned stock first |
| Shipping/tax buffer | Multiple suppliers | 180.00 | Planning allowance, not a quote |
| **Estimated complete kart** |  | **2,600.65** | Before rider protective equipment; volatile prices and allowances |

The requested frame, seat and pedal portion is **$350.90**. The complete non-powertrain portion is **$1,611.75**. With the two current powertrain candidates, the realistic working total is **$2,600.65**, with a sensible uncertainty range of roughly **$2,400–$2,900** until CAD, local steel, shipping and owned-parts inventory are resolved. The $1,200 ceiling is not feasible with all-new parts: it leaves $211.10 after powertrain, which is $139.80 less than the frame/seat/pedal portion alone. A custom frame could remain original while reusing a safe donor's axle, hubs, wheels, steering and brake components, but those parts must be inventoried and reviewed before counting any savings.

## Question and scope
Strict-evidence research, checked 2026-09-20. Build a complete component checklist for Ethan's own Fusion-designed welded electric kart: 30 mph maximum, 45 minutes mixed riding, mostly flat pavement. This is a sourcing/design BOM, not a released shopping list or a safety signoff. The 48 V Golden Motor architecture below is an assistant proposal, not a user-approved purchase.

## Cost and status
Listed-price subtotal: **$2101.78 USD** for nine priced candidate lines only. Variant surcharges, every unpriced line, shipping and tax are additional. This is NOT the complete build cost or a grant request total. No purchased or owned parts are assumed. Empty prices in the CSV mean unknown/included as explained, never free. Kit quantities are counted once.

## Bill of materials
| Group | Qty | Part | Candidate / specification | Listed unit USD | Source | Selection condition |
|---|---|---|---|---:|---|---|
| Power | 1 | Motor | Golden Motor HPM3000B, 48 V, air cooled | 318.00 | [Supplier](https://www.goldenmotor.com/eCar/frame-eCar.htm) | Candidate; exact shaft drawing and mounting revision required |
| Power | 1 | Motor controller | Golden Motor VEC200, 48 V | 260.00 | [Supplier](https://www.goldenmotor.com/eCar/frame-eCar.htm) | Confirm 58.4 V battery maximum, motor pairing and programmable battery-current limit |
| Power | 1 | Battery | Golden Motor FP4852R0 48 V 52 Ah LiFePO4 | 899.99 | [Supplier](https://goldenmotor.bike/collections/bldc-batteries/products/48v-52ah-lifepo4-battery) | OUT OF STOCK on directly inspected page; 150 A continuous supplier claim; confirm documentation |
| Power | 1 | Charger | Battery supplier matched charger | — | TBD / included | Included with battery; no second charger purchase |
| Power | 1 | Battery harness | Supplier harness set | — | TBD / included | Included with battery; extensions and controller harness may still be required |
| Power | 1 | Accelerator pedal | Golden Motor FSC-010 foot throttle | 84.99 | [Supplier](https://goldenmotor.bike/products/foot-throttle) | Verify controller signal range, pinout, idle fault behavior and spring return |
| Power | 1 | Programming interface | Golden Motor PI400 / VEC | 60.00 | [Supplier](https://www.goldenmotor.com/eCar/frame-eCar.htm) | Confirm current VEC200 software/interface compatibility |
| Electrical | 1 | Main traction fuse and covered holder | DC-rated fuse coordinated with cable and controller | — | TBD / included | Size and interrupt rating require battery fault-current data; voltage rating above full charge |
| Electrical | 1 | Main contactor | DC traction contactor with matched coil and suppression | — | TBD / included | Select using full-charge voltage, continuous and interruption ratings |
| Electrical | 1 | Precharge assembly | Resistor and switching / controller-approved precharge | — | TBD / included | Size from controller capacitance and supplier wiring instructions |
| Electrical | 1 | Service disconnect | Touch-protected DC disconnect | — | TBD / included | Must suit pack voltage/current; connector alone is not automatically a load-break switch |
| Electrical | 1 | Emergency stop | Latching emergency-stop switch | — | TBD / included | Wire into validated shutdown circuit, not directly through small switch contacts carrying motor current |
| Electrical | 1 | Key / enable switch | Controller-compatible enable switch | — | TBD / included | Low-current control circuit |
| Electrical | 1 | Brake cutout switch | Pedal-operated switch and bracket | — | TBD / included | Match controller brake input; mechanical braking remains independent |
| Electrical | 1 lot | Power cable and terminations | Battery positive/negative; 3 motor phases; lugs, boots, heat shrink | — | TBD / included | Gauge/length from final current, routing, voltage drop and thermal calculation |
| Electrical | 1 lot | Signal harness and protection | Sealed connectors, control wire, auxiliary fuse, loom, glands, clamps | — | TBD / included | Exact connector and pinout schedule required |
| Electrical | 1 | Energy / speed instrumentation | Compatible speed sensor/display and Wh measurement | — | TBD / included | Match full-charge voltage; supports speed-limit and runtime testing |
| Electrical | 1 | Charging interlock and port protection | Covered charge access; drive inhibit while charging | — | TBD / included | Coordinate with supplied battery charger/port |
| Chassis | 1 cut list | Frame tubing | Weldable structural steel; grade, section and lengths from reviewed Fusion design | — | [Supplier](https://www.metalsdepot.com/steel-products/steel-square-tube) | Source family only; square section is not an approved frame design |
| Chassis | 1 lot | Mounting plate and gusset stock | Motor, seat, battery, controller, brake and steering mounts | — | TBD / included | Thickness/quantity from reviewed drawings |
| Chassis | 1 | Floor pan and foot protection | Formed sheet with finished edges and pedal clearance | — | TBD / included | CAD-defined material, thickness and fastening |
| Chassis | 1 | Motor mount / tension adjustment | Custom slotted or adjustable mount | — | TBD / included | Check torque reaction, stiffness and chain alignment |
| Chassis | 1 | Battery tray and retention | Custom supported tray, restraints and impact protection | — | TBD / included | Accommodate battery, connectors, servicing and ventilation |
| Chassis | 1 | Controller mount | Custom plate / heat-spreading mounting surface | — | TBD / included | Follow controller cooling requirements |
| Chassis | 1 set | Bumpers / side protection | CAD-defined front, rear and side structures | — | TBD / included | Review with frame and intended operating site |
| Drivetrain | 1 | Rear live axle | 1-inch keyed ecosystem provisional; length/material TBD | — | [Supplier](https://www.bmikarts.com/1-Live-Axle-Kit-40-Chain_p_44789.html) | Reference kit only, NOT priced as purchase; diameter requires load review |
| Drivetrain | 2 | Axle bearings | UC205-16 candidate for provisional 1-inch axle | — | [Supplier](https://www.bmikarts.com/1-Live-Axle-Kit-40-Chain_p_44789.html) | Match axle and bearing mounts; load review pending |
| Drivetrain | 2 | Bearing mount sets | Flangettes and weld-on hangers | — | [Supplier](https://www.bmikarts.com/1-Live-Axle-Kit-40-Chain_p_44789.html) | Kit references 400165 / 400170; procure with bearings as matched set |
| Drivetrain | 1 lot | Axle retention hardware | Keys, collars, nuts and spacers | — | TBD / included | Quantity and fits from axle stack drawing; positive wheel retention |
| Drivetrain | 1 | Motor sprocket | Correct motor-shaft bore/key and selected chain family | — | TBD / included | Tooth count and shaft interface unresolved; do not assume standard gas-engine bore |
| Drivetrain | 1 | Rear sprocket and carrier | Matched chain pitch and axle bore | — | TBD / included | Final ratio depends on loaded motor RPM and tire rolling circumference |
| Drivetrain | 1 length | Drive chain and connecting link | Same series as BOTH sprockets | — | TBD / included | Length from CAD; check rating, tension range and guard clearances |
| Drivetrain | 1 | Chain / sprocket guard | Custom securely mounted guard | — | TBD / included | Enclose reachable moving chain and sprockets |
| Running gear | 2 | Front hub assemblies | Sealed-bearing kart hubs matched to chosen spindle | — | TBD / included | Provisional 5/8-inch bearing bore; rated load and wheel interface must be checked |
| Running gear | 2 | Rear hub assemblies | Keyed/clamping hubs matching rear axle | — | TBD / included | Provisional 1-inch bore; match wheel bolt circle and positive retention |
| Running gear | 4 | Wheels | Kart wheels matched to hubs and tires | — | TBD / included | Exact front/rear widths, bolt circles and offsets unresolved |
| Running gear | 4 | Tires | New paved-use kart tires with suitable documented load/speed capability | — | TBD / included | Select dry/wet use and diameters before gearing; rejected deformed clearance tires |
| Running gear | 4 sets | Valve / tube and wheel hardware | Valves or tubes as required; wheel bolts/nuts and spacers | — | TBD / included | Do not add tubes where selected wheel/tire assembly does not require them |
| Steering | 1 | Spindle kit | BMI 421400 family; two spindles and brackets | 38.95 | [Supplier](https://www.bmikarts.com/Complete-Spindle-Set--58-Shaft_p_1319.html) | Base price; 5/8-inch shafts; includes bushings, kingpins and nuts; suitability not load-certified |
| Steering | 1 | Steering shaft and hub | Azusa KAZ1867 family with pitman arms | 33.95 | [Supplier](https://www.bmikarts.com/Steering-Shaft-and-Hub-Assembly-with-Welded-Pitman-Arms_p_4092.html) | Base price; length from driver fit; verify rod-end mounting holes |
| Steering | 1 | Steering wheel | Azusa-compatible wheel | — | TBD / included | Match hub bolt circle and driver clearance |
| Steering | 2 | Steering shaft supports | Bearings/bushings and frame brackets | — | TBD / included | Match selected shaft; include retention collars/rings as needed |
| Steering | 2 | Tie-rod assemblies | Properly rated rods, four ends and jam nuts | — | TBD / included | Length and end size from geometry; inexpensive economy kits not selected as quality solution |
| Steering | 1 set | Steering stops and fasteners | Positive stops, retained pivot bolts and spacers | — | TBD / included | Avoid over-center linkage; check full-lock clearance in CAD |
| Brakes | 1 | Hydraulic brake kit | MCP 600505 / 600510 family, provisional 1-inch hub | 325.95 | [Supplier](https://www.bmikarts.com/MCP-Hydraulic-Brake-Kit_p_581.html) | Base price; caliper, master cylinder, rotor, hub, line and DOT5 fluid included; variant and braking analysis pending |
| Brakes | 1 | Brake pedal assembly | Pedal, pivot, bushings, return spring and travel stop | — | TBD / included | Pedal leverage must match master-cylinder travel and required pressure |
| Brakes | 1 | Brake pushrod and clevis | Mechanically retained adjustable linkage | — | TBD / included | Check pushrod alignment, full travel and return |
| Brakes | 1 set | Brake mounts and line clips | Caliper bracket and master mount | — | TBD / included | Not assumed included in base MCP price; verify fittings and line routing |
| Driver | 1 | Seat | Azusa/BMI K400510 bucket seat candidate | 79.95 | [Supplier](https://www.bmikarts.com/Go-Kart-Bucket-Seat_p_1228.html) | Fit must be confirmed before frame dimensions |
| Driver | 1 set | Seat mounts and padding | Mounting stays, spreading washers, fasteners, padding | — | TBD / included | Match seat instructions and frame; no unreviewed restraint arrangement |
| Finish | 1 lot | Assembly hardware | Specified-grade bolts, locking nuts, washers, rivets and thread retention | — | TBD / included | Generate exact counts and grades from CAD |
| Finish | 1 lot | Fabrication consumables | Welding consumables, cutting/grinding supplies, corrosion protection | — | TBD / included | Inventory owned tools and supplies first |
| Conditional | as needed | Additional braking / parking provision | Front brakes or parking system if review/site requires | — | TBD / included | Not silently included in rear-only braking assumption |
| Conditional | as needed | Auxiliary electrical equipment | DC-DC converter, lights and horn if operating-site design requires | — | TBD / included | No public-road eligibility claim |
| Project costs | as needed | Rider protective equipment and testing tools | Fit-appropriate helmet/eye protection and required inspection/test equipment | — | TBD / included | Separate from kart hardware; inspect existing equipment; eligibility under Forge not established |
| Project costs | 1 total | Shipping, tax, fabrication services | Destination-specific supplier quotes | — | TBD / included | Not included in listed-price subtotal |

## Evidence and compatibility gates
- Battery FP4852R0: directly inspected product page shows **out of stock**; older search text said in stock. Use the live-page observation, recheck before ordering. Supplier lists 150 A continuous, 58.4 V charging, approximately 13.5 kg and 320 x 160 x 290 mm, with charger/harness included. Its 2,496 Wh label conflicts with 51.2 V x 52 Ah = 2,662.4 Wh; confirm usable energy rather than choosing the larger number. Supplier claims are not independent battery testing/certification.
- Provisional runtime check using the smaller 2.496 kWh label and an assumed 80% usable allowance: 1.9968 kWh usable. To last 0.75 hour, average battery draw must be at most 2.6624 kW. At 2 kW average the arithmetic gives 59.9 minutes; at 3 kW, 39.9 minutes. These are conditional calculations, not measured runtime. Verify by Wh logging on the built kart.
- VEC200 battery-voltage ceiling, regenerative charging limits, current settings, throttle behavior and complete wiring must be confirmed for the exact revision. A 200 A phase rating is not a 200 A battery rating. Keep regeneration disabled until pack/controller charge compatibility is established.
- Axle, spindle, hub, wheel and brake choices remain conditional on design payload, track width, steering geometry and braking calculations. Do not infer structural or stopping adequacy from bore diameter or supplier horsepower guidance.
- No final sprocket tooth counts: speed = motor RPM / overall ratio x tire rolling circumference. Use loaded RPM and actual tire dimensions; program and test the 30 mph maximum. A motor wattage label cannot establish top speed.
- The BMI rear-axle kits contain a brake option; they are references for individual pieces, not extra purchases alongside the MCP kit. Do not charge for an entire axle/brake bundle and a second brake system accidentally.
- Reject the researched K266310 wheel package: its page states light-duty hubs and storage-deformed tires. It is not the selected wheel set. Economy tie-rod kits were also not promoted to a reviewed quality specification.
- Driver fit, design payload, destination country and exact tire specification still prevent release of dimensions and final pricing. No harness/rollover structure has been selected; review occupant protection as a system with the experienced builder.

## Claim ledger
| Claim | Direct source / locator | Support | Checked | Limits |
|---|---|---|---|---|
| Motor/controller/interface list prices | Golden Motor eCar catalog linked in BOM | supported-with-limits | 2026-09-20 | Old-style catalog; exact stock/revision and delivered quote unverified |
| Battery specifications, package and stock | FP4852R0 product specification and purchase section linked in BOM | supported-with-limits | 2026-09-20 | Supplier-only claims; inconsistent energy label; currently unavailable |
| Brake kit contents and base price | BMI MCP kit description linked in BOM | supported-with-limits | 2026-09-20 | Selected options and application adequacy unverified |
| Steering/seat base prices | Individual BMI product pages linked in BOM | supported-with-limits | 2026-09-20 | Size-dependent; no vehicle load approval |
| Runtime arithmetic | Capacity x assumed usable fraction / average electrical power | inference | 2026-09-20 | Actual duty cycle and usable energy unknown |
| Full build price / guaranteed performance | No sufficient evidence | unverified | 2026-09-20 | Do not present subtotal as full cost |

## Reuse and handoff
This note is the authoritative current BOM; adjacent CSV is its export. Supersedes the old budget sourcing worksheet for current scope, without deleting history. Related: [[03 Projects/Forge go-kart]] and [[05 Knowledge/Quality go-kart options 30 mph 45 minutes]]. Recheck availability, prices and specifications before pitch submission or purchasing. Next: settle driver envelope/payload; select rated wheels/hubs and battery availability; finish Fusion interfaces and electrical protection sizing; replace TBD lines with exact quantities, parts and quotes. No external messages, purchases or pitch submission performed.

