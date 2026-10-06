---
type: session
status: recorded
created: 2026-09-20
updated: 2026-09-20
schema: 1
---

# Go-kart battery ratings confirmed
Recorded at: 2026-09-20T20:30:52-07:00

## Intent
Resolve the Walmart battery's full-charge voltage and continuous-current rating for motor-controller matching.

## Important user statements
Ethan reported: "the charger is 87.6v5a and the 50 a is continues." This records an 87.6 V/5 A charger and a 50 A continuous-discharge rating. The battery remains a planned candidate rather than a completed purchase.

## Work and verified results
The ratings are user-reported. An 87.6 V LiFePO4 charge voltage implies 24 series cells at 3.65 V/cell and about 76.8 V nominal. This resolves the voltage choice in favor of the Kelly KLS8412S, whose manufacturer publishes a 40-100 V operating range. The 40 A target battery draw retains 20% headroom below 50 A continuous. Maximum regenerative-charge current and BMS low-voltage cutoff remain unknown.

## Decisions and reasons
Keep the QS138 QSJ138A-70 3 kW motor plus KLS8412S controller as the recommended architecture. Do not use the KLS7212S because its published 86 V maximum is below the battery's 87.6 V full charge. Keep regenerative braking disabled until the battery's regenerative/charge limit is documented.

## Saved to
[[03 Projects/Forge go-kart]] and [[05 Knowledge/Go-kart 72 V budget revision]].

## Handoff
Last verified result: charger 87.6 V/5 A and continuous-discharge rating 50 A, both user-reported.
Blocker or open question: BMS low-voltage cutoff, peak discharge/time, maximum regenerative/charge current, battery dimensions/weight, and exact controller/motor sensor compatibility.
Next concrete action: obtain the missing pack specifications, then price the exact KLS8412S Hall-sensor variant and calculate gearing from tire outside diameter.
