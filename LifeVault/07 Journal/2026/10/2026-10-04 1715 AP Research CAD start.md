---
type: session
status: active
created: 2026-10-04
updated: 2026-10-04
schema: 1
---
# AP Research CAD start
Recorded at: 2026-10-04T17:15:43-07:00
Source: current chat, Ethan's direct message.
## Intent
Begin the robot's actual Fusion model using good design practices beyond dimension tables.
## Important user statements
Ethan: "i fixed my issue with fusion so we can begin work on the actual 3d model."
Ethan wants design best practices beyond dimension tables. Repair method unspecified; do not infer Reset was the solution.
## Work and verified results
Fusion working is user-reported, not independently observed. Reviewed Autodesk guidance on top-down modeling, Hybrid design, component activation, and sketch constraints. No CAD action or learner attempt observed in this chat.
## Decisions and reasons
Assistant recommendation, pending user action: start with a layout/skeleton in a Hybrid Design to evaluate workspace and hardware packaging; use simple constrained sketches, components, controlled references, and joints before detailed fabrication features.
## Saved to
[[03 Projects/AP Research robot design]]
## Handoff
Last verified result: user reports Fusion issue fixed.
Open questions: geometry, payload envelope, funding and actuator selection remain unresolved.
Next concrete action: follow latest progress and batching preference below.

## Progress and teaching preference — 2026-10-04
Evidence: attached Fusion screenshots show saved AP Research Robot - Concept v1, millimeter units, Hybrid Design, active 00_Layout, and an empty XZ sketch (view cube Front; global X right, Z up). User subsequently confirmed unchecking 3D Sketch. Vertical construction line has been instructed but completion is not established.
User explicitly requests complete lists of steps, then a review after completing the batch, rather than per-click confirmation. Apply this preference to CAD tutoring; only break down further when requested or troubleshooting a mismatch.
Next proposed batch: parameterized side-view base envelope plus target shelf reference, constrain and change-test, then save. Assistant starter base dimensions (600 mm length, 200 mm body height, 75 mm clearance) are unvalidated layout placeholders, not adopted requirements. Shelf target 1676.4 mm and reach target 609.6 mm remain tentative user targets. No completed layout geometry yet.

## Parameter preference correction — 2026-10-04
Direct user statement: "i dont like parameters. i want to use all of the best practices besides parameters". The previous assistant parameter-table recommendation is superseded. Use direct numeric sketch/feature dimensions and geometric constraints, without named user parameters or parameter-table setup. Keep batches with review afterward. Revised next batch: center-aligned construction rectangle, 600 mm long by 200 mm high, underside 75 mm above origin/floor; shelf reference 1676.4 mm high; fully constrain, temporarily edit width to 650 mm to test centering, restore 600 mm, save Layout_Side. These base dimensions remain proposed placeholders. No new CAD completion claimed.

## Corrected layout checkpoint — 2026-10-04
Later user report: sketch saved, new component not yet created. User explicitly requests switching from tutoring to delegated modeling: set up Fusion MCP and create the chassis envelope on their behalf.
Directly observed in user screenshot C:/Users/ethan/AppData/Local/Temp/codex-clipboard-4f2d5de5-1e8b-4ad5-8af1-403afe76d1a7.png: 600 x 200 mm chassis envelope, 75 mm clearance, 1676.4 mm dimension now anchored to floor origin and shelf level; shelf marker length 600 mm. Temp attachment persistence is not guaranteed; this note preserves the observed result.
Preserved attempts: rectangle first centered on floor, then bottom coincident with floor, then correct clearance; shelf reference initially measured from rectangle center. Final guided correction replaced that height dimension with origin-to-shelf measurement. Outcome successful-with-help, not independent mastery. Full constraint status, width change-test, naming/final save not confirmed.
Next batch proposed: finish and save Layout_Side; activate root; create internal 01_Base_Envelope; sketch XZ and project only four layout rectangle edges with Projection Link; ensure a normal closed profile; symmetric solid extrusion with Whole Length 450 mm, New Body; name Chassis_Envelope and save. Width is unvalidated assistant placeholder. No 3D model completion claimed.

## Fusion MCP setup — 2026-10-04
Official Autodesk built-in local MCP confirmed in documentation; no third-party add-in needed. Added Codex global server `fusion`, Streamable HTTP endpoint http://127.0.0.1:27182/mcp, to C:/Users/ethan/.codex/config.toml via Codex CLI and checked registration. Connection to default port refused before activation. User asked to enable Preferences > General > API > Fusion MCP Server and report port. Enabling not confirmed; no live document inspection or model mutation yet. Next: verify MCP initialize/tool discovery after enablement, inspect saved active design, then create/verify requested envelope while preserving original layout. Native desktop UI controls unavailable in this session, so preference activation is a user step.
Sources: https://help.autodesk.com/view/fusion360/ENU/?guid=ADSKMCP_FusionDesktopMcp_connecting_to_the_fusion_mcp_server_html ; https://developers.openai.com/codex/mcp .

## Connected and delegated chassis completed — 2026-10-04
Ethan enabled built-in Fusion MCP and said done. Standard Streamable HTTP initialization at http://127.0.0.1:27182/mcp succeeded (protocol 2025-03-26); tools/list exposed fusion_mcp_read, fusion_mcp_execute, fusion_mcp_update and electronics read. Connection registration persists in Codex config; transient MCP session IDs are deliberately not saved.
Current native catalog did not expose the newly configured tools, so tools were invoked via local HTTP JSON-RPC using PowerShell. Start fresh initialize, send notifications/initialized, then discover tools each future session; read server-provided schemas. Read tool supports API documentation, open document list, active command and screenshot; execute supports Fusion Python script with def run(_context: str), output via print, exceptions left uncaught. Inspect active document and APIs before mutations.
Read-only preflight: AP Research Robot - Concept v1, sole open active document, 00_Layout/Layout_Side, zero bodies, fully constrained source sketch, healthy state, nine construction lines, zero user parameters. Chassis edges were at X +/-300 mm, Z 75/275 mm, Y 0. Floor-to-shelf reference verified at 1676.4 mm.
Exported pre-edit archive. Created root-level 01_Base_Envelope, Base_Profile on component XZ plane, four linked projections of source rectangle perimeter, normal geometry, single profile. Extruded symmetrically with whole length 450 mm, NewBody, feature Chassis_Width_450mm, body Chassis_Envelope. Source layout preserved. User explicitly delegated this batch including saving; this is assistant-executed work, not evidence of independent student mastery.
Independent readback/checks: bounds [-300,-225,75] to [300,225,275] mm, volume 54000 cm3, one solid body, healthy feature, fully constrained source/profile, all four projections reference source entities, zero named user parameters. computeAll succeeded. Saved and read back AP Research Robot - Concept v2, isSaved=true, isModified=false. Final viewport fitted isometric; final screenshot visually inspected successfully. The source-layout width-change exercise was not performed; actual link objects verified instead.
Artifacts: D:/PerfectLife/AP Research/CAD/robot-before-chassis-2026-10-04.f3d; D:/PerfectLife/AP Research/CAD/robot-chassis-envelope-2026-10-04.f3d; D:/PerfectLife/AP Research/CAD/chassis-envelope-proof.png. These represent provisional packaging, not a manufacturable solid chassis or validated load capability.
Next action: establish mast position and shared carriage travel, check arm workspace and chassis interference before detailing parts. No further user setup currently needed; Fusion must remain open for MCP access.
