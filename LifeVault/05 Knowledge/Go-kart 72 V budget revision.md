---
type: research
status: provisional
created: 2026-09-20
updated: 2026-09-20
schema: 1
---

# Go-kart 72 V budget revision
## Thirty-amp-hour options near $600, 2026-09-20
Closest direct-buy candidate: [Bomb Moto 72 V 30 Ah e-moto battery](https://bombmoto.com/products/b1-battery-72v-2024), observed at **$599** with five listed in stock. Published contents are a 72 V/30 Ah pack, Samsung 21700 cells, ANT Bluetooth BMS, protective casing, copper circuitry, XT90 output, XT60 charge input, adapters and a 72 V/5 A charger. Bomb Moto says the pack can briefly supply 100 A or slightly more, recommends an 80 A controller tune, and warrants a 70 A tune. The 70 A limit is suitable for the Kunray's 5 kW rated class: 72 V x 70 A = 5.04 kW nominal input. It does not allow treating the controller's 100 A ceiling as a normal setting.

Evidence limitations: Bomb Moto does not publish the exact Samsung cell model, pack series/parallel arrangement, continuous-current rating, dimensions, weight, exact ANT BMS model/settings, regenerative-charge limit, conductor construction or UN 38.3/MSDS on the product page. Its [warranty page](https://bombmoto.com/pages/warranty) states a six-month battery warranty, while its [FAQ](https://bombmoto.com/pages/faq-24) says three months for batteries; returns are discretionary, unused/uninstalled, buyer-paid and subject to a possible 25% restocking fee. Get these points resolved in writing before purchase. The listing's 2–6 hour ride-time statement is not useful for this kart and is not used.

Runtime calculation: 72 V x 30 Ah = 2.16 kWh nominal; at an explicit 85% usable assumption, 1.836 kWh is available. That is about 55.1 minutes at 2 kW average, 44.1 minutes at 2.5 kW and 36.7 minutes at 3 kW. Forty-five minutes is plausible if mixed-riding average input stays near or below 2.45 kW; it is not guaranteed.

Budget calculation: $599 battery + $389.90 Walmart Kunray kit = **$988.90**, leaving **$211.10** of the $1,200 ceiling before shipping/tax and all remaining mechanical/electrical parts. This still requires substantial owned, donor or unusually inexpensive running gear.

Manufacturer-quote alternative: [AMORGE's official 20S6P 72 V pack](https://www.amorge.com/post/amorge-20s6p-72v-30ah-220a-lithium-battery-pack-for-voltinsu-em-5-electric-dirt-bike) offers a metal case, ANT Bluetooth BMS, 84 V charging, customizable QS8/XT60 connectors and a one-year warranty. The Samsung 50S option is 30 Ah with claimed 150 A continuous/210 A peak. A third-party tracker listed that configuration at $614 before confirmed shipping and showed other inconsistent price summaries; AMORGE publishes no direct price. Treat it as a quote lead only. It qualifies only if the written delivered price with charger stays at or below $650 and the transport/BMS documents are supplied.

Decision: Bomb Moto is the best immediate price/capacity fit found, but it is not proven to have exactly the same documentation and warranty quality as HotPaxx. Its lower supported tune is acceptable for the rated Kunray motor. Do not call it purchase-ready until its missing pack data and warranty conflict are resolved.

## Sub-$650 battery search for the Kunray system, 2026-09-20
Ethan reaffirmed that the complete kart should cost no more than $1,200 and requested a battery below $650. Current prices were checked on 2026-09-20.

| Candidate | Published specification | Price | Evidence assessment |
|---|---|---:|---|
| [HotPaxx 72 V 20 Ah metal-case pack](https://www.hotpaxx.com/product-page/copy-of-72v-20ah-120a-lithium-ion-battery) | EVE 40P cells; 150 A continuous/200 A 10-second seller claims; QS8/6 AWG; Bluetooth; 5 A charger; 84 V/20 Ah implied; one-year manufacturing-defect warranty | $582 shipped in lower 48 | Best documented option found under $650. Still require exact BMS, dimensions, weight, UN 38.3/MSDS and regen limit. Imported pack; seller warranty excludes incompatible use and unauthorized BMS changes. |
| [HotPaxx 72 V 20 Ah shrink-wrap pack](https://www.hotpaxx.com/product-page/72v-20ah-120a-lithium-ion-battery-1) | EVE 40P; 130 A continuous/180 A maximum seller claims; QS8/6 AWG; Bluetooth; 5 A charger | $549 shipped in lower 48 | Electrically adequate by seller claims, but a custom kart needs a separately engineered rigid and insulated enclosure. The $33 saving is not compelling versus the metal-case version. |
| [MDPowerPacks 72 V 20 Ah metal-case pack](https://mdpowerpacks.shop/products/72v-20ah-100a-battery) | Seller claims 20S4P Samsung 50S, 100 A continuous, JK Bluetooth BMS, display, metal case and 5 A charger | $499.99 plus unspecified shipping | Cheapest plausible candidate, but the site gives no pack datasheet, weight, formal warranty period, BMS model, transport documents or named business identity beyond a Maryland location and Gmail address. Do not select without documentation. |
| [HotPaxx 72 V 24 Ah metal-case pack](https://www.hotpaxx.com/product-page/72v-24ah-180a-battery-em5-in10) | EVE 40P; ANT 220/550 BMS; 180 A continuous/240 A max seller claims; 10 A charger; QS8/6 AWG | $624 shipped in lower 48 | More energy within battery budget, but only $186.10 remains after the Walmart motor kit, making the full $1,200 build infeasible without extensive owned/donor hardware. |

### Runtime and total-budget effect
At 72 V nominal, 20 Ah is 1.44 kWh and 24 Ah is 1.728 kWh. With an explicit 85% usable-energy planning assumption:
- 20 Ah provides 1.224 kWh: about 29.4 minutes at 2.5 kW average, 24.5 minutes at 3 kW, and requires average input at or below 1.63 kW to last 45 minutes.
- 24 Ah provides 1.469 kWh: about 35.3 minutes at 2.5 kW, 29.4 minutes at 3 kW, and requires average input at or below 1.96 kW to last 45 minutes.

These packs can supply acceleration power according to their published current ratings, but capacity governs runtime. Thirty mph remains feasible through gearing and controller limits; 45 minutes of typical mixed driving is not a reliable expectation from 20–24 Ah with this 5 kW system.

With the $389.90 Walmart motor kit, the powertrain subtotals are $971.90 for HotPaxx metal-case 20 Ah, $938.90 for HotPaxx shrink-wrap 20 Ah, $889.89 plus shipping for MDPowerPacks, or $1,013.90 for HotPaxx 24 Ah. The remaining $228.10/$261.10/$310.11-before-shipping/$186.10 must cover the frame steel, live axle and bearings, wheels/tires, hydraulic brake, steering, seat, foot throttle conversion, chain system, contactor/precharge/disconnect, correctly DC-rated fuse, cable/connectors, guards, fasteners, tax and contingencies. No verified all-new high-quality BOM fits those balances. A $1,200 result requires substantial owned or donor running gear, or a change to the motor/runtime/total budget.

## Kunray KR5V power-system revision, 2026-09-20
Ethan selected the Kunray KR5V V2 72 V / 5 kW kit as the foundation for the next design. This is a design choice, not a purchase.

### Verified motor/controller facts
- [Kunray KR5V manufacturer page](https://cnkunray.com/products/kr5v): rated 5 kW, rated 60 A, peak 80–100 A, rated 5,000 rpm, peak 8,000 rpm, rated/peak torque 8.5/35 Nm, external Hall sensor, KTY84-130 temperature sensor, IP54 and air cooling. Manufacturer offers #35 and 420 sprocket variants.
- [Kunray kit page](https://cnkunray.com/products/kunray-kr5v-72v-5000w-electric-brushless-motor-for-electric-motorcycle-razor-100a-fardriver-controller-35-chain-set): matched NS18 controller, advertised 100 A line current and 300 A phase current. The direct listing offers a pedal-throttle and 420-10T selection, which better fits a kart than the Walmart half-twist/#35 bundle.
- [Walmart listing](https://www.walmart.com/ip/16577716642): $389.90 observed, sold by Kunray and fulfilled by Walmart; included half-twist throttle, #35 9T motor sprocket, 65T axle sprocket and chain. Price and availability are volatile.
- [Fardriver controller manual](https://www.far-driver.com/wp-content/uploads/Fardriver-controller-Manual.pdf): standard 72 V models list an 88 V maximum and support programmable bus/phase current and regenerative braking. The custom NS18 model is not identified in the table, so confirm its exact label and maximum voltage. A 20S lithium-ion pack at 84 V full has more voltage margin than a 24S LiFePO4 pack at 87.6 V full.

### Battery options
| Option | Published specification | Observed price | Assessment |
|---|---|---:|---|
| [Chakra 72 V 40 Ah EVE-40P](https://www.chakra-battery.com/products/72v40ah-ant420a-chakra-lithiumbattery) | 20S10P, 2.88 kWh, EVE INR21700-40P, 250 A continuous claimed, ANT Bluetooth BMS, metal case, QS10 discharge, 4 AWG cable, 5 A charger, one-year warranty | $930 | Best value candidate, pending charger-voltage, dimensions, weight, BMS/regen, transport-test and construction evidence. Listing drawing says 250 x 155 x 236 mm while text says 11 x 6 x 9.7 in. A listing image says 87 V charger, but 20S lithium-ion requires 84.0 V; require written correction/confirmation. |
| [ChiBatterySystems Gladiator 72 Pulsar Standard 45 Ah](https://chibatterysystems.com/collections/sur-ron-72v/products/72pulsar) | 3.24 kWh, 200 A continuous/360 A peak claimed, smart BMS, active balancing, steel case, 6 AWG/QS10-P, individual cell fusing, two-year warranty, about 35 lb | $1,599 | Better-documented premium option; Sur-Ron form factor must be checked against CAD and an exact dimensional drawing requested. |

[EVE's official 40P cell page](https://www.evemall.eu/consumer-battery/cylindrical-ncm-cell/21700-40p) lists 4 Ah and up to 50 A continuous per cell. In a claimed 10-parallel Chakra pack, a 100 A controller draw divides to about 10 A per cell before imbalance, supporting ample cell-level current margin if the advertised cells/configuration are authentic. This does not verify the assembled pack or its BMS.

### Calculated performance envelope
The Chakra pack has 2.88 kWh nominal. At an explicit 85% usable planning assumption, 2.448 kWh is available: about 59/49/42/37 minutes at 2.5/3.0/3.5/4.0 kW average battery input. Forty-five minutes is plausible only if mixed-riding average input stays at or below about 3.26 kW. The Chi 45 Ah pack has 3.24 kWh nominal and 2.754 kWh at the same assumption: about 66/55/47/41 minutes at those loads. These are energy calculations, not road-test guarantees.

The included 9T/65T ratio is 7.22:1. Using the manufacturer's 5,000 rpm rated speed, ideal wheel-speed calculations are about 22.6 mph on 11-inch tires, 26.8 mph on 13-inch tires and 30.9 mph on 15-inch tires; peak-rpm calculations are higher and should not define the road-speed target. Actual loaded speed depends on tire growth, voltage sag, losses, mass and controller mapping. Choose tire diameter before final sprockets and use an electronic 30 mph cap.

### Commissioning envelope and release checks
- Start near the motor's 60 A rated battery current and roughly 150–180 A phase current. After instrumented thermal testing, consider about 80 A battery and 220–250 A phase. Treat 100 A line and 300 A phase as controller ceilings, not initial settings.
- Disable regenerative braking until the chosen pack's maximum regenerative/charge current and full-charge behavior are documented.
- Use a kart foot pedal with compatible signal range and a dependable return mechanism. Prefer 420 chain for this high-quality kart build.
- Before purchase, require the exact BMS model and settings, 84.0 V charger confirmation, full-charge voltage, dimensions and weight, cell evidence, UN 38.3/MSDS, wiring/fuse/precharge details, warranty and a pack drawing. Confirm the exact NS18 controller maximum voltage from its label/datasheet.

Listed powertrain subtotal: Walmart motor kit plus Chakra pack = $1,319.90 before tax, shipping and remaining kart hardware. Direct Kunray pedal/420 kit at $429 plus Chakra = $1,359. Premium Chi plus the direct Kunray kit = $2,028. These are component comparisons, not full-build totals or purchase approval.

## Blwny manufacturer-site verification, 2026-09-20
Strict-evidence question: does Blwny's own website provide enough support to approve its 72 V 40 Ah battery for Ethan's 3 kW go-kart system? Result: **no**. The manufacturer's page adds material contradictions and still provides no pack-specific technical documents.

### Claim ledger
| Claim | Directly inspected source | Status | Limitation or conflict |
|---|---|---|---|
| 72 V, 40 Ah, 2,880 Wh, 50 A BMS, 27.8 lb | [Blwny product page](https://blwny.com/products/blwny-72v-40ah-lifepo4-battery) | seller claim | The Walmart product image says 24S, 76.8 V nominal and 3,072 Wh. Both energy figures follow different nominal-voltage conventions, but the pages do not explain this. |
| Compatible with 250–1,500 W motor systems | [Blwny product page](https://blwny.com/products/blwny-72v-40ah-lifepo4-battery) | verified as current manufacturer guidance | Conflicts with Walmart's 250–3,500 W advertising and does not support the proposed 3 kW kart controller. |
| Five-year manufacturing-defect warranty | [Product FAQ](https://blwny.com/products/blwny-72v-40ah-lifepo4-battery) and [registration page](https://blwny.com/pages/register-warranty) | unverified terms | The linked [refund policy](https://blwny.com/policies/refund-policy) only states a conditional 30-day return policy and contains no five-year coverage, exclusions, remedies, transfer terms or claim procedure. Walmart states 12 months. |
| UL, CE and RoHS / safety-tested cells | [Blwny product page](https://blwny.com/products/blwny-72v-40ah-lifepo4-battery) | unverified for this exact pack | No certificate, report, file number, certified model, laboratory or scope is provided. A badge is not enough to establish whole-pack certification. No BLWNY result for this battery was found through public UL-targeted searching; absence from that search is not proof that no record exists. |
| Automotive-grade cells and 4,000+ cycles | [Blwny product page](https://blwny.com/products/blwny-72v-40ah-lifepo4-battery) | unverified | No cell maker/model, cycle-test conditions, retained-capacity threshold or test report. |
| U.S.-based support | [Contact page](https://blwny.com/pages/contact) and [technical-support page](https://blwny.com/pages/technical-support) | supported only as a site claim | Only a Gmail address and contact form are given; no named legal manufacturer, telephone number or pack-specific downloadable guide was found. The generic support page's “below 10 V” BMS-reset guidance is not useful for a 72 V pack. |
| Business history | [Verisign RDAP record](https://rdap.verisign.com/com/v1/domain/blwny.com) | verified domain fact | `blwny.com` was registered 2026-04-13. A young domain does not prove the seller is illegitimate, but it cannot demonstrate a five-year warranty track record. |
| Four five-star product reviews | Current product page review section | seller-hosted evidence only | All four displayed reviews are dated 2026-08-31 and use brief, nonspecific wording. They are not independent technical validation. |

### Decision
Do not approve this battery for the 3 kW motor system from the currently published evidence. Although a claimed 50 A continuous BMS would arithmetically allow 3.84 kW at 76.8 V, Blwny's explicit 1.5 kW application ceiling is the controlling supplier guidance until Blwny explains it in writing. A 40 A controller limit does not resolve that contradiction by itself.

Evidence that would change the decision: a pack datasheet identifying 24S configuration and actual nominal voltage; cell maker/model and parallel count; continuous/peak discharge curves and temperature limits; BMS model/settings including charge and regenerative limits; UN 38.3 report; certification documents with file numbers covering this exact model; capacity and cycle-test reports; construction/dimensional drawing; and complete written warranty terms. No seller message was sent.

## Motor match for the Walmart 72 V 40 Ah / 50 A BMS candidate, 2026-09-20
Ethan is leaning toward the Walmart battery but has not purchased it. He reports the charger is **87.6 V/5 A** and that **50 A is the continuous-discharge rating**. These are useful user-supplied specifications, not independently inspected seller documentation. For LiFePO4, 87.6 V / 3.65 V implies **24 series cells**, giving about 76.8 V nominal. The 40 A controller target leaves 20% current headroom below the reported continuous limit.

Formerly recommended architecture, now **conditional and blocked by Blwny's published 1.5 kW application limit**:
- [QS Motor QS138 QSJ138A-70](https://www.cnqsmotor.com/product/motor138-qs138-qsmotor-qsj138a-70-motor138-with-gearbox/): 72 V, 3 kW, internal 1:3 reduction, 428 sprocket compatibility, advertised 85-92% efficiency, $339.86 sale price plus a listed $7 15T sprocket. Manufacturer claims only; shipping/tax excluded.
- [Kelly KLS8412S](https://kellycontroller.com/shop/kls-s/): 48-84 V nominal, published 40-100 V operating range, 120 A one-minute motor/phase boost, 50 A controller continuous motor-current rating, programmable battery-current limit, Hall-sensor support and configurable motor current. The exact 84 V/120 A/Hall variant price was not exposed; page-wide range is $99-$359. Add the $19 PC programming cable. Do not confuse phase current with battery current.
- [Kelly 0-5 V accelerator](https://kellycontroller.com/shop/kelly-0-5v-accelerator/): $25, 0.8-4.2 V output. A kart foot pedal may be preferable; verify its output and return spring before selection.

Provisional controller settings, pending battery documentation and motor commissioning:
- Target maximum battery current: **40 A**, giving 20% headroom below the user-reported 50 A continuous BMS rating. Kelly's interface uses percentages rather than a direct amp entry: its FAQ defines battery current as controller peak motor current x Motor Current % x Battery Limit %. With the KLS8412S's 120 A published peak, 100% motor current and a 33% battery limit calculate to about 39.6 A. Start with a lower motor-current percentage for commissioning and choose the paired Battery Limit percentage so the calculated result remains <=40 A; confirm actual DC draw with instrumentation before loaded driving. At the inferred 76.8 V nominal voltage, 40 A is 3.072 kW input; at 87.6 V full charge it is 3.504 kW. Higher phase current can preserve low-speed torque without demanding the same current from the battery.
- Regenerative braking: **disabled initially**. The 5 A charger establishes the supplied charging rate but does not prove the battery's maximum regenerative-charge current, and regen near an 87.6 V full charge can raise pack voltage.
- Controller high-voltage threshold: provisionally about **90 V**, above the 87.6 V full-charge voltage and below the controller's published 100 V maximum. Verify the exact controller firmware range before writing this setting.
- Controller low-voltage threshold: do not finalize until the seller supplies the BMS low-voltage cutoff. A conservative commissioning value around **72 V (3.0 V/cell)** can protect reserve capacity, but it is a proposed setting rather than a verified pack requirement.
- Commission with unloaded wheel/motor identification first, then conservative current and speed limits; independently confirm Hall angle, temperature-sensor compatibility and current readings.

Why KLS8412S instead of a generic 72 V controller: the inferred 24-series LiFePO4 pack reaches 87.6 V, while the Kelly 72 V KLS7212S is published only through 86 V. The 84 V KLS8412S is published through 100 V. The common Kunray kit's included controller is fixed/listed at 50 A, leaving no current margin. A VEVOR 3 kW kit lists 65 A maximum and can exceed the battery rating. The QS/Votol EM150 complete kit is mechanically attractive and $493.85, but its published/default current is 120 A and a secondary manual gives an 87 V overvoltage setting, below this battery's 87.6 V full charge.

This selection could be capable of the 30 mph design goal with appropriate axle ratio and tire diameter, but it is not approved with the Blwny battery under current evidence. Final sprocket sizing requires actual tire outside diameter, loaded motor RPM and vehicle mass. No purchase, seller contact, or external message was made.

## Walmart candidate comparison, 2026-09-20
User supplied [Walmart item 20423867677](https://www.walmart.com/ip/20423867677). Direct browser inspection of the listing and its six product images on 2026-09-20 found:
- Blwny brand; sold and shipped by third-party seller Ruyi; no ratings or reviews.
- Current displayed price **$463.93** (was $519.99), free 30-day returns. Price and availability are volatile.
- Product-image ratings: **24S LiFePO4, 76.8 V nominal, 40 Ah, 3,072 Wh, 50 A continuous BMS, 87.6 V/5 A charger and 4,000+ claimed cycles**. The voltage, capacity and energy are arithmetically consistent.
- Listed dimensions **12.80 x 5.96 x 6.93 inches** and assembled weight **27.8 lb**. Accessories list the battery, warranty card, Anderson adapter cable and 5 A charger. Images identify a 50 A-rated Anderson connector, XT90 male plug, voltage/capacity display, handle and Bluetooth monitoring by QR code.
- Warranty section says **12 months** and "free replacement within 72 hours for non-human damage," while Walmart explicitly warns that Marketplace seller terms can differ and should be confirmed before purchase.
- One seller graphic appears to swap the labels for operating temperature and charging time: it displays `7~8H` beside operating temperature and `-20 C ~ 60 C` beside charging time. The likely intended claims are 7–8 hours charging and -20 C to 60 C operation, but this is an inference. Ideal 40 Ah / 5 A charge time is 8 hours before taper.

The listing does **not** supply the cell manufacturer/model, parallel configuration, BMS model/datasheet, peak-current duration, low-voltage cutoff, balancing current, maximum charge or regenerative current, low-temperature charge cutoff, wire gauge, connector series/authenticity, formal IP rating, UN 38.3 report, UL/IEC certification, capacity test, dimensional drawing or confirmed third-party warranty procedure. The claimed 3.072 kWh at 27.8 lb works out to about **244 Wh/kg at the complete-pack level**, and the listed dimensions imply about **355 Wh/L**. Those unusually high LiFePO4 pack-level density figures make the weight/dimensions or capacity claims worth verifying with test evidence; this is a red flag, not proof the listing is false.

Conclusion: **candidate only; do not buy from the listing alone**. It is electrically plausible for the proposed 3 kW setup if the missing documents check out. Ask the seller for the exact cell datasheet/configuration, BMS datasheet and limits, UN 38.3 and relevant safety documents, capacity-test report, photos/diagram of internal construction, exact dimensions/weight and written warranty terms. This candidate supersedes Ethan's earlier >=100 A continuous preference for the current comparison.

Using the claimed 24S nominal voltage, 76.8 V x 40 Ah = **3.072 kWh nominal**. At an 80% usable planning assumption, usable energy is 2.458 kWh. Average battery draws of 2/2.5/3 kW imply about 73.7/59.0/49.2 minutes. A 45-minute target permits about 3.28 kW average input under these assumptions. At 76.8 V nominal, 40 A is 3.072 kW and the claimed 50 A continuous limit is 3.84 kW. At 50 A continuously, the idealized full-capacity runtime is 48 minutes; reserve and real losses reduce it. These remain calculations from seller ratings, not measured capacity or runtime. No predicted top speed without gearing/load. No purchase or seller contact.

## Comparison only: 48 V 25 Ah LG 50 A candidate
2026-09-20: Ethan asked about [AliExpress item 3256809224983761](https://www.aliexpress.us/item/3256809224983761.html), exact option 48V25Ah LG 50A, at his displayed $324.33. Browser inspection selected that option; assistant session displayed $318.33 with new-shopper discount. Use user's price for his comparison, not a promised checkout price. Listing identifies UNITPACKPOWER; exact LG cell model, authentic capacity and 50 A continuous versus peak rating were not verified in inspected text. This is comparison, NOT a confirmed change from the user's 72 V battery requirement.

Conditional calculations: 48 x 25 = 1,200 Wh nominal; 80% usable assumption gives 960 Wh. At average battery inputs 1/1.5/2/2.4 kW, runtime is 57.6/38.4/28.8/24 minutes. For 45 minutes average input must be <=1.28 kW. If 50 A is continuous, nominal input-power ceiling is 48 x 50 = 2.4 kW, before drivetrain losses. Cannot sustain 3 kW mechanical output. Requires a compatible 48 V controller/motor setup, not an assumed drop-in replacement for the 72 V kit. No top-speed prediction without gearing/load.

Relevant specific product-history check: [CPSC UPP warning](https://www.cpsc.gov/Recalls/2024/CPSC-Warns-Consumers-to-Stop-Using-Unit-Pack-Power-UPP-E-bike-Batteries-Due-to-Fire-and-Burn-Hazards-Risk-of-Serious-Injury-and-Death), April 15 2024, names U004/U004-1. This listing's exact model was not established as either affected model; do not apply that warning to all UPP packs as a factual claim. Confirm exact model and verifiable certification before recommending purchase. No purchase or seller contact performed.

## User-linked AliExpress candidate, inspected 2026-09-20
[Listing 3256812647454710](https://www.aliexpress.us/item/3256812647454710.html), Cloud Lithium Pioneer Power Store, opened successfully in browser. User asked runtime/speed; has not approved buying it. Title and seller description claim 72 V **40 Ah**, model WL7240S, with 84 V 5 A charger. Default 50 A option displayed $374.38; selecting 100A BMS 7000w displayed **$402.07**, before checkout tax/price confirmation. No cart or purchase action.

Important mismatch: variant choices say 50/80/100/120/150 A BMS; expanded seller description says maximum continuous discharge 80/120/220 A, without mapping to variants. Exact 100 A continuous pack rating and actual 40 Ah capacity are unverified. Platform AI overview was excluded as evidence. Need cell model/configuration, exact pack continuous-current documentation and capacity test; do not approve from BMS label alone.

Conditional runtime from claimed energy: 72 x 40 = 2,880 Wh; assumed 80% usable = 2,304 Wh. At average battery draw 1.5/2/2.5/3/3.5 kW, runtime is 92.16/69.12/55.296/46.08/39.497 minutes. For 45 minutes, average draw must stay <=3.072 kW under these assumptions. These are scenarios, not measured riding predictions. 3 kW motor output is not the same as 3 kW battery input. No top speed is established by the battery listing; requires motor RPM under load, overall ratio, tire diameter, load and resistance. Existing 30 mph design goal remains, not proven performance.

## Current correction: 100 A continuous minimum
Ethan subsequently said: "i would be fine with 100 a+ continuous" (2026-09-20). Current target is **72 V 30 Ah, at least 100 A continuous**, under $1,200 for the complete kart. This replaces the 150 A minimum below; the earlier search is retained as history.

Additional directly inspected sources, 2026-09-20:
- [All4eBikes 72 V 30 Ah 100 A](https://all4ebikes.co.uk/batteries/triangle-battery-72v/triangle-ebike-battery-72v-30ah-100a/): GBP668.90 displayed, explicitly claims 100 A continuous. Exact cell model/discharge evidence and delivered price need verification; not a certified match.
- [Spark Cycleworks Brute 72 V 30 Ah](https://www.sparkcycleworks.com/index.php/product/brute-72v-30ah-spare-stock-battery-only/): $850, battery only, 120 A discharge label. Does not specify continuous versus peak; keep unverified against requirement. With the $181.99 motor benchmark this leaves only $168.01 before charger and every other part.
- [iEE Power 72 V 30 Ah](https://www.ieepower.com/product/72v-30ah-e-bike-triangle-lithium-battery/): $899–949 depending on charger selection; 100 A BMS/discharge stated but continuous qualifier and conflicting cell descriptions need clarification. Not an accepted match merely because BMS says 100 A.

No verified complete under-$1,200 configuration yet. A useful negotiation target is battery plus charger delivered <=$600, motor/controller <=$200 and everything else <=$400. These are maximum budget allocations, NOT supplier quotes or an established feasible BOM. Donor mechanical components may be needed; user acceptance still pending.

Proposed motor remains the 72 V 3 kW budget class. A 100 A battery rating provides nominal 7.2 kW capability but does not require the motor to draw it. The 2.16 kWh capacity and conditional 45-minute average-power ceiling of 2.304 kW (80% usable assumption) are unchanged. Exact motor/controller availability and 84 V tolerance remain unresolved.

Source session: [[07 Journal/2026/09/2026-09-20 1815 Go-kart 100 A correction]].
## Question and scope
Strict evidence, checked 2026-09-20. Ethan now asks to try for a complete kart below $1,200 using a 72 V 30 Ah battery capable of at least 150 A continuous discharge, then select the motor around it. Existing 30 mph maximum, 45-minute mixed riding and own Fusion frame goals remain. Source: [[07 Journal/2026/09/2026-09-20 1811 Go-kart battery budget revision]].

## Result
No verified all-new complete build under $1,200 found. Keep the battery requirement; do not substitute a 150 A peak pack or imply the motor must consume 150 A. Proposed budget motor class is 72 V 3 kW with its matched controller. Exact controller must accept 84 V full charge for a 20S lithium-ion pack. The earlier 48 V parts proposal is superseded for current selection.

## Claim ledger
| Candidate | Inspected supplier source | Evidence and price | Limits |
|---|---|---|---|
| RISUN 72 V 30 Ah triangle pack | [Product](https://m.risunmotor.com/products/72v-30ah-200a-425a-smallest-size-most-powerful-triangle-lithium-battery-inr21700-50xg-18c-discharge-rate-battery-with-6a-10a-charger-) | $979.99 displayed; supplier claims 200 A continuous; charger options included in description | Supported-with-limits: charger variant and delivered quote need confirmation; no independent pack testing verified |
| AMORGE 72 V 30 Ah high-current pack | [Manufacturer project](https://www.amorge.com/post/amorge-20s6p-72v-30ah-220a-lithium-battery-pack-for-voltinsu-em-5-electric-dirt-bike) | Manufacturer lists a 220 A-labelled project; no public price inspected | Quote lead only. Must confirm actual continuous rating, cells, BMS, wiring, thermal limits, charger and shipping; label alone not acceptance |
| Electro Watts Samsung 50S 20S6P | [Product](https://electrowattsebikes.co.uk/products/72v-30ah-high-performance-ebike-battery-150a-ant-bms-dual-copper-plating-triangle-ebike-battery) | GBP829.99; 150 A continuous supplier claim; UK-plug charger; 3–7 week delivery statement | Payment gateway disruption notice on site; not chosen for this budget; currency not silently converted |
| VEVOR 72 V 3 kW kit | [Product 010199783752](https://www.vevor.com/brushless-dc-motor-c_11227/3000w-electric-brushless-dc-motor-kit-72v-4900rpm-motor-with-upgraded-controller-p_010199783752) | $181.99 displayed; controller kit; page lists out-of-stock options | Budget candidate only. Exact SKU availability, full-charge rating, foot throttle and thermal duty unverified |
| QS138 70H V3 + EM150-2SP | [Manufacturer kit](https://www.cnqsmotor.com/product/qs138-70h-v3-3000w-motor-conversion-kit-with-votol-em-150-controller/) | $493.85 displayed sale; motor, controller, display and hand throttle | More costly option; foot control and kart integration extra; exact revision/84 V compatibility still verify |

All entries checked 2026-09-20, supplier-only evidence. Price and product claims do not establish assembled vehicle safety or quality.

## Checked arithmetic
- RISUN plus budget VEVOR listed prices: 979.99 + 181.99 = $1,161.98. Leaves $38.02 of $1,200 before chassis, running gear, brakes, protection, throttle, shipping or tax.
- RISUN plus QS kit: 979.99 + 493.85 = $1,473.84 before those remaining parts.
- Battery nominal energy: 72 x 30 = 2,160 Wh. At a planning assumption of 80% usable, 1,728 Wh / 0.75 hour = 2,304 W maximum average battery draw for 45 minutes.
- At 2 kW average, conditional runtime 51.84 minutes; at 3 kW, 34.56 minutes. No measured runtime guarantee.
- 72 x 150 = 10.8 kW nominal electrical capability, not the required motor power or a command to draw 150 A. 30 Ah / 150 A = 0.2 hour = 12 minutes idealized, before reserve and losses.

## Cost-reduction route, not a quote
A lower delivered battery quote and inspected donor mechanical parts could improve feasibility while preserving Ethan's own frame. User has been asked whether donor wheels/axle/steering/brakes are acceptable; no answer yet. No donor price, battery quote or complete $1,200 BOM has been fabricated. Do not downgrade brakes or protective wiring to force a total. Do not choose a larger motor merely to consume the available battery current.

## Next action / reuse
Obtain an exact delivered battery quote for 72 V 30 Ah >=150 A continuous with charger and documented cell/pack ratings; decide donor parts; verify exact motor/controller full-charge limits and availability. No external inquiry was sent. Current complete component checklist remains [[03 Projects/Forge go-kart BOM]], but its former 48 V selections are historical. Recheck these volatile listings before use.
