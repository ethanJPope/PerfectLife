---
type: session
status: recorded
created: 2026-09-20
updated: 2026-09-20
schema: 1
---

# Walmart battery listing inspection
Recorded at: 2026-09-20T20:40:08-07:00

## Intent
Use Ethan's Chrome tab to inspect the entire Walmart battery listing before matching it to the go-kart motor system.

## Important user statements
Ethan authorized read-only control of his Chrome tab so the listing could be inspected. The battery is still a candidate and has not been purchased.

## Work and verified results
The listing and all six product images were inspected. Seller claims are 24S LiFePO4, 76.8 V nominal, 40 Ah, 3,072 Wh, 50 A continuous BMS, 87.6 V/5 A charger and 4,000+ cycles. The current displayed price was $463.93; dimensions 12.80 x 5.96 x 6.93 inches; listed weight 27.8 lb. It is Blwny-branded, sold and shipped by Ruyi, and has no ratings or reviews. The listing shows Anderson and XT90 connections, a voltage/capacity display, Bluetooth monitoring and a 12-month stated warranty, but Walmart warns third-party seller terms may differ.

The voltage/capacity/energy arithmetic is consistent. Important missing evidence includes the exact cell and BMS specifications, peak-current duration, cutoff and balancing settings, charge/regenerative current limit, low-temperature charge protection, IP rating, UN 38.3/safety documents, capacity testing and a reliable dimensional drawing. The stated weight and size imply unusually high complete-pack energy density for LiFePO4 and need documentary verification. One product graphic appears to swap charge-time and operating-temperature labels.

## Decisions and reasons
Keep the battery as a candidate but do not recommend purchase from the listing alone. The proposed QS138 3 kW motor and Kelly KLS8412S controller remain the power-system match, with battery current limited and measured at no more than 40 A. Keep regenerative braking disabled until the seller documents the pack's allowed charge/regenerative current and BMS behavior.

## Attempts worth preserving
Walmart's expanded warranty language adds no independent coverage evidence; it repeats the 12-month claim and instructs buyers to confirm third-party Marketplace terms with the seller.

## Saved to
[[03 Projects/Forge go-kart]] and [[05 Knowledge/Go-kart 72 V budget revision]].

## Handoff
Last verified result: the listing's major electrical ratings are internally consistent, but the pack lacks enough documented evidence for a high-quality go-kart purchase decision.
Blocker or open question: cell identity/configuration, BMS limits, test/certification reports, actual dimensions/weight and enforceable warranty terms.
Next concrete action: obtain those documents from the seller, then finalize the motor/controller purchase list and gearing from the chosen tire diameter.
