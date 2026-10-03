# Official runtime AI interface — 0.4.0

The app now makes an explicit `host.request("model.complete", {task,input,schema,class}, callback)` request. It reads `r.data.output`, shows source evidence, missing information, one next step and an editable draft. All fields are required; every supplied evidence string must be a nonempty exact source substring. An actionable result requires evidence, next step and draft. This does not prove that all generated facts are correct: users must review.

Only clicking the AI button sends current input. Source restoration, local observation and local rule processing do not call models. Budget queries and completion share one pending/generation guard. Cancellation, source changes, clearing, observer controls and local fallback invalidate old callbacks. A 45-second app timeout discards late results; it does not cancel a host/provider operation already underway. No app retries, developer credentials or provider endpoints are added. The official host owns provider selection and authentication. Drafts are saved only after confirmation and actual readback; nothing sends email.

## Independent evidence, 2026-10-03

| Check | Actual result |
| --- | --- |
| Standalone native UI, official completion service absent | 8 checks passed: empty input, visible error, retained input, no auto save, failed completion cannot save, local fallback, old draft cleared, edits invalidate |
| Synthetic native callbacks, isolated test-only bundle | 9 checks passed: draft/details, confirmation required, save readback, any invalid evidence rejects, positive needs evidence, no-task details, cancelled/changed source drops late replies |
| Existing mail workflow | 12 native UI/file checks passed |
| Existing source/consent lifecycle | 17 native UI/file checks passed |
| Existing budget/error behavior | 7 native UI/file checks passed |
| Complete official Windows host, signed local test catalog | 0.4.0 installed through ordinary permission dialog; actual model.complete returned `no_provider: No AI provider is set up. Add one in AI providers.` Input preserved |
| Bundle gate | Restamped production bundle passed with unsigned warning only |

The complete host is pinned at cf85350129830605d08973befdd8bde6480f6a77, binary SHA256 06288db0e48605e81e38a371606d0c5c14ba98378ae8cd0bca9b138f847f78ce. Standalone test host is the existing Windows host-repro App Hub build. Native response fixtures replace only the model transport in a private copy, label themselves synthetic, and never call a provider; they are not model-quality or live inference evidence. Public JSON records summarize actual results, not a claimed official acceptance.

## Dual-loop provenance

MiniMax Plan implementation receipt MCP-2dad3b50-20fc-4d89-a310-08cf7425afe9 and correction MCP-bdd3333d-f39f-422c-95d5-b9bef0953aa4 are retained in the private workspace. Both dispatched beneath the official outer-duty lock with fresh quota checks. First response-layer/invalidation issues were rejected. The second draft rewrote previously verified UI/save code using unsupported methods; native UI failed. Desktop Codex outer restored the verified body and independently repaired the prompt, boolean checks, evidence handling and snapshot guard. Final evidence belongs to the combined reviewed implementation, not to the MiniMax ACK alone. No unknown config file is committed.

## Still unverified

Actual provider-backed inference, six-case model quality, host cancellation/fallback behavior under network delay and the 45-second timeout are not verified. The isolated host has no provider configured. This version proves official interface integration and result-handling behavior, not live AI generation or competition acceptance. Next step is verify the intended official host AI setup without copying development credentials, then run bounded real generation and collect same-version demonstration evidence.

2026-10-03 follow-up: actual local inference and the unchanged45-second timeout have now been exercised. Model-quality acceptance failed and remains pending; see AI_LIVE_LOCAL.md for0.4.0/0.4.1 results and the new placeholder guard. Earlier unverified statements above describe the initial0.4.0 service-only milestone.
