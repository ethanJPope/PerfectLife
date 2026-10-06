---
type: research
status: provisional
created: 2026-09-20
updated: 2026-09-21
schema: 1
---

# Forge rules and coin forecast — 2026-09-20

## Question and scope
Strict evidence mode: can a new go-kart fund a $400–650 kart and Supercon reward? Current targets are September 30 design and October 12 build at about 15 hours/week; original October 10 scenario below is historical. Public repository HEAD resolved to `0698312589e1d73487c02e6562f7bf3a2e7f4f8f`. Relevant source files were fetched and read, not executed. Live authenticated UI was inaccessible; deployment parity, personal balances, reward availability and review timing remain unverified.

## Finding
A conditional plan is possible; sufficient spendable coins by submission cannot be promised. Public code credits approved projects, not pending submissions. Starting with zero coins, 750–1,000 coins covers the specified grant range and the source-defined ticket, excluding travel. Reviewer-adjusted hours and tier determine the outcome.

## Supercon-only forecast — 2026-09-21
Ethan separately wants to earn coins for the Supercon ticket and flight support within 2–3 weeks; this does not cancel the go-kart project. Source: [[07 Journal/2026/09/2026-09-21 1821 Supercon coin planning]]. The [official tier guide](https://forge.hackclub.com/docs/about-forge/tiers) states **Tier 2 = 6.5 coins/hour**, **Tier 3 = 5.0 coins/hour**, and reviewer-assigned final tier. The [Forge shop](https://forge.hackclub.com/shop) was inspected in the source task and lists the **350-coin ticket** with housing/food and stackable flight support at **8 coins per $10**. The public [order model](https://github.com/hackclub/forge/blob/0698312589e1d73487c02e6562f7bf3a2e7f4f8f/app/models/order.rb#L65-L68) also supports the rate. Exact lodging dates, reimbursement process/eligible expenses, ticket availability/deadline, and event-specific completed-build eligibility remain unverified; the interface alone cannot prove server rules. The [Hackaday announcement](https://hackaday.com/2026/08/13/supercon-ten-tickets-on-sale-now/) gives November 6–8, 2026 in Pasadena.

Assuming **zero existing coins**, **Tier 2 design rate of 6.5**, no streak/guild bonus, all hours accepted, no project-parts spending, and flight support in $10 increments:

| Illustrative flight support | Ticket + flight coins | Accepted Tier 2 design hours |
|---:|---:|---:|
| $200 | 350 + 20×8 = **510** | **78.46 h** |
| $300 | 350 + 30×8 = **590** | **90.77 h** |
| $400 | 350 + 40×8 = **670** | **103.08 h** |

For a whole-hour planning threshold, round those hours **up** to 79, 91, or 104 hours respectively. Ethan later selected a **three-week window** and tentatively estimated **20 hours/week** for this Supercon sprint ([[07 Journal/2026/09/2026-09-21 1821 Supercon coin planning#Availability update]]). At the assumed Tier 2 design rate, **60 accepted hours × 6.5 = 390 coins**: ticket first leaves 40 coins, or **$50 in flight support**. With an illustrative 10% multiplier on all 60 hours, **429 coins** leaves 79 after the ticket: 9 complete $10 flight units cost 72 coins, giving **$90 support and 7 coins remaining**. At Tier 3 without bonuses, 60 × 5 = **300 coins**, short of the ticket. From zero, $200 flight support plus ticket needs 510 / 6.5 = **78.46 accepted Tier 2 design hours**, approximately **4 weeks** at 20 hours/week; $300 needs 590 / 6.5 = **90.77 hours**, approximately **4.54 weeks**. These are arithmetic scenarios, not commitments or earning forecasts. The earlier 15 hours/week report remains relevant to the go-kart context but is superseded for this sprint. The old zero balance was not reconfirmed on 2026-09-21. The build-stage rate may differ from the design rate; verify before forecasting mixed work. Project funding coins, if any, are additional to ticket and flight targets. Review latency and bonus timing are unknown; no coin delivery date is promised.

Tier 1 is a **requested comparison**, not Ethan's selected project tier. The [tier guide](https://forge.hackclub.com/docs/about-forge/tiers) gives **7.5 coins/hour** and requires a #forgery pitch for an ambitious, polished project with major original work; the reviewer chooses the final tier. If all 60 hours were accepted as Tier 1 design with no bonuses or parts spending: **60 × 7.5 = 450 coins**, leaving 100 after the 350-coin ticket. Twelve complete $10 flight units cost 96 coins, so that buys **$120 of flight support with 4 coins left**. With an illustrative 10% multiplier on every hour: **60 × 7.5 × 1.10 = 495 coins**, leaving 145 after the ticket; eighteen flight units cost 144 coins, so **$180 support with 1 coin left**. The $200 flight scenario needs 510 coins: **68 accepted Tier 1 design hours** without bonus or **61.82 hours** at 8.25 coins/hour. Both exceed 60 hours. These calculations do not establish eligibility, actual bonus timing, approval, or a coin delivery date.

## Claim ledger
All checked 2026-09-20. “Source-verified” means the inspected documentation/code says this, not confirmation of the deployed site or the user's account.

| Claim | Source | Status / limits |
|---|---|---|
| Tier 1 7.5 coins/hour; Tier 2 6.5; reviewer chooses final tier/payout; Tier 1 requires a #forgery pitch and substantial original engineering | [Tier guide](https://github.com/hackclub/forge/blob/0698312589e1d73487c02e6562f7bf3a2e7f4f8f/docs/about-forge/tiers.md) | Source-verified; kart category alone gives no guarantee. |
| Grants convert at 1 coin per USD; ticket constant is 350; flight reimbursement is 8 coins per $10 | [Order model](https://github.com/hackclub/forge/blob/0698312589e1d73487c02e6562f7bf3a2e7f4f8f/app/models/order.rb#L65-L68) | Source-verified; live terms/availability still to confirm. |
| Ticket description includes housing and food | [Shop UI source](https://github.com/hackclub/forge/blob/0698312589e1d73487c02e6562f7bf3a2e7f4f8f/app/javascript/pages/Shop/Index.tsx#L374-L379) | Source-verified; exact dates, rooms, travel and guardian arrangements unspecified. |
| Supercon occurs Nov 6–8, 2026 in Pasadena | [Hackaday announcement](https://hackaday.com/2026/08/13/supercon-ten-tickets-on-sale-now/) | Organizer-verified; Forge package is a separate reward. |
| Streak multipliers: 3 days 1.02; 7 days 1.05; 14 days 1.10; 30 days 1.15; 60 days 1.20; 100 days 1.25 | [User model](https://github.com/hackclub/forge/blob/0698312589e1d73487c02e6562f7bf3a2e7f4f8f/app/models/user.rb#L110-L117) | Source-verified; multipliers agree with tier guide. |
| Since Aug 22, daily streak qualification requires at least 1 logged hour; day follows user timezone; short late-sync window exists | [Streak service](https://github.com/hackclub/forge/blob/0698312589e1d73487c02e6562f7bf3a2e7f4f8f/app/services/streak_service.rb) | Code-verified; prose only says journal daily. Use stricter rule and confirm with staff. |
| Freeze cost 5 coins; freezes can cover missed days, but only when enough cover the full gap | [User model](https://github.com/hackclub/forge/blob/0698312589e1d73487c02e6562f7bf3a2e7f4f8f/app/models/user.rb#L138) and streak service above | Code-verified; owned count unknown; never assume a freeze is available. |
| Earnings require approval; calculation uses accepted hours × tier rate × streak × guild multiplier, rounded to cents | [Project model](https://github.com/hackclub/forge/blob/0698312589e1d73487c02e6562f7bf3a2e7f4f8f/app/models/project.rb#L248-L277) | Code-verified; no guild bonus included in forecast. |
| Approval handler captures current streak | [Approval handler](https://github.com/hackclub/forge/blob/0698312589e1d73487c02e6562f7bf3a2e7f4f8f/app/controllers/admin/projects_controller.rb#L448-L480) | Code-verified; conflicts with prose's “when submitting.” Submission-day streak alone is not a secure budget assumption. |
| Normal shop items use a built-project gate; Supercon uses a separate handler that does not contain that same check and sends orders to staff review | [Shop controller](https://github.com/hackclub/forge/blob/0698312589e1d73487c02e6562f7bf3a2e7f4f8f/app/controllers/shop_controller.rb#L151-L169) | Code inference about the specific gate only, not a guarantee of eligibility or fulfillment. |

## Requirements affecting success
[Submission requirements](https://github.com/hackclub/forge/blob/0698312589e1d73487c02e6562f7bf3a2e7f4f8f/docs/requirements/submitting.md): complete assembly, real attachments, applicable firmware, independent sanity check, clear README/images, linked BOM CSV with total, editable CAD plus STEP and other applicable source files. Original work must be the builder's; AI-generated design files are not an acceptable substitute.

[Pitch guidance](https://github.com/hackclub/forge/blob/0698312589e1d73487c02e6562f7bf3a2e7f4f8f/docs/requirements/pitching.md): describe the idea, actual original design work, references, prior work, Tier 1 justification and a rough BOM before committing heavily to the design.

[FAQ](https://github.com/hackclub/forge/blob/0698312589e1d73487c02e6562f7bf3a2e7f4f8f/docs/about-forge/FAQ.md): research needs Lapse evidence; coding beyond one hour requires Hackatime or Lapse; building should be lapsed. No double-dipping. Funding eligibility and reimbursements should be clarified before purchases. Purely mechanical projects can be valid; adding an unnecessary PCB is not inherently required.

[Journalling guidance](https://github.com/hackclub/forge/blob/0698312589e1d73487c02e6562f7bf3a2e7f4f8f/docs/design/how-to-journal.md): record personal decisions, errors, progress images, and genuine work; do not have AI author the journals. LifeVault planning notes must stay distinct from submitted Forge journals.

## Current forecast — revised deadlines
Source of updated goals: [[07 Journal/2026/09/2026-09-20 Go-kart scope revision]]. Rough capacity is 21–24 hours through September 30 and 47–49 hours through October 12, based on 15 hours/week and whether today is counted. Allocation is illustrative, not a scope estimate.

The [project model](https://github.com/hackclub/forge/blob/0698312589e1d73487c02e6562f7bf3a2e7f4f8f/app/models/project.rb#L124-L129) sets build review to **5 coins/hour**, distinct from Tier 1 design's 7.5. All-stage forecasts must use the appropriate rate.

- Design: 22 accepted hours × 7.5 × 1.05 = **173.25 coins**.
- Build: 26 accepted hours × 5 × 1.10 = **143 coins**.
- Both approvals: **316.25 coins**; no-bonus fallback = 22 × 7.5 + 26 × 5 = **295 coins**.
- Zero-balance shortfall against 750–1,000 target: **433.75–683.75 coins**.
- Before building, design payout alone is **226.75–476.75 short** of the $400–650 kart funding goal.

Assumptions: solo project, Tier 1 design accepted, all stated hours accepted, guild multiplier 1, zero initial coins, no other spending/travel, and qualifying streak preserved at approval. Starting Sep 20 with zero streak yields day 11 on Sep 30 (1.05) and day 23 on Oct 12 (1.10). Public code requires one logged hour daily. Approval timing and actual initial streak can change results. Coins are not available merely because submission or construction is complete. Procurement before build earnings is an independent funding constraint.

## General design-only formula and historical October 10 scenario
Let B be existing spendable coins, P eligible project funding dollars, T the ticket price, F optional flight support dollars in $10 increments, and X any other intended coin spending.

New coins needed = max(0, P + T + 8 × ceil(F / 10) + X − B).

Required accepted hours = new coins needed / (tier rate × streak multiplier × confirmed guild multiplier).

This formula assumes a solo new design and no already-counted earnings. Use an actual quoted flight amount and confirmed eligibility before budgeting reimbursement. Guild multiplier is assumed 1.0, not guessed. Forecast below uses B=0, T=350, F=0, X=0, and rounds hours upward to whole hours.

| Target | Coins | Tier 1, 14-day streak (8.25/hour) | Tier 1, no streak (7.5/hour) | Tier 2, 14-day streak (7.15/hour) |
|---|---|---|---|---|
| $400 kart + ticket | 750 | 91 h | 100 h | 105 h |
| $650 kart + ticket | 1,000 | 122 h | 134 h | 140 h |

September 20–October 10 inclusive has 21 calendar days. Starting at zero streak and working each day reaches day 14 on October 3 and day 21 on October 10; not day 30. At 8.25 coins/hour, the unrounded 750/1,000 thresholds average 4.33/5.77 accepted hours per day. Starting later or reserving non-work days raises the average.

Cross-check: 91 × 8.25 = 750.75; 122 × 8.25 = 1,006.50. At 110 accepted hours, 907.50 coins leaves 557.50 after reserving the ticket. At 63 accepted hours (21 days × 3 hours), 519.75 coins leaves only 169.75 for the kart after the ticket. Streak alone is not enough.

Illustrative stress test, NOT an estimated rejection probability: if only 90% of logged hours are accepted, 1,000 coins at 8.25 per accepted hour needs at least 135 genuinely logged hours (135 × 0.90 × 8.25 = 1,002.375 before final rounding). Do not stretch logs to hit a target. If the honest scope takes fewer hours, change funding/reward expectations.

## Unresolved
Live balance/streak/timezone, tier and accepted hours, program/account eligibility, deployed-code parity, redemption availability/deadline, precise package inclusions, reviewer turnaround, and the kart's engineering/budget feasibility. No promise of spendable coins on September 30 or October 12, even if the relevant submission is completed then.

## Recheck
Recheck rules/shop before pitching, before final submission, and before redemption. Ask staff to settle code/documentation discrepancies. Evidence snapshot: `D:\PerfectLife\research-sources\forge-snapshot`. It contains public source only, not credentials or account data. No messages or purchases were made.
