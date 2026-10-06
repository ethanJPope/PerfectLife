---
type: session
status: recorded
created: 2026-09-20
updated: 2026-09-20
schema: 1
---

# Blwny manufacturer verification
Recorded at: 2026-09-20T20:47:23-07:00

## Intent
Inspect the manufacturer website Ethan supplied and determine whether it resolves the Walmart battery's missing evidence for a 3 kW go-kart.

## Important user statements
Ethan supplied Blwny's product page as the manufacturer's website. The battery remains unpurchased.

## Work and verified results
The product page, all FAQ answers, refund policy, warranty-registration page, technical-support page, contact page and about page were directly inspected. The manufacturer page lists 72 V, 40 Ah, 2,880 Wh, 50 A BMS, 27.8 lb and compatibility with 250–1,500 W motor systems. This conflicts with Walmart's 24S/76.8 V/3,072 Wh image, 250–3,500 W application claim and 12-month warranty.

Blwny advertises a five-year warranty and UL/CE/RoHS badges, but the linked refund policy has no five-year warranty terms and the site supplies no certificate or file number covering this pack. No cell model, BMS datasheet, test report or pack manual was available. The contact and support pages provide a Gmail address and form but no named legal manufacturer or telephone number. Direct Verisign RDAP data shows the domain was registered 2026-04-13.

## Decisions and reasons
The manufacturer website does not justify approving the battery for a 3 kW system. Treat Blwny's explicit 1.5 kW application limit as controlling until the company reconciles the conflicting listings and provides written technical documentation. The previous QS138/Kelly match is now conditional and blocked for this battery.

## Attempts worth preserving
Public searches targeted at UL did not locate a BLWNY record for this exact pack. This is recorded as lack of verification, not proof that certification does not exist.

## Saved to
[[03 Projects/Forge go-kart]] and [[05 Knowledge/Go-kart 72 V budget revision]].

## Handoff
Last verified result: Blwny's published guidance supports only 250–1,500 W motor systems and provides no accessible pack-specific technical or certification documents.
Blocker or open question: whether Blwny can provide written 3 kW approval and the exact pack/BMS/test/warranty documents.
Next concrete action: request the documentation checklist from Blwny or select a better-documented traction battery supplier.
