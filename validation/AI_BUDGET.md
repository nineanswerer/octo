# Runtime model budget integration 0.3.2

This milestone connects the official host service, not model generation. No `model.complete`, provider setup, paid inference or external message sending was performed. Ordinary API routing remains disabled pending verified competition-voucher spending boundaries.

Verified full host: OctoSense `cf85350129830605d08973befdd8bde6480f6a77`, Windows executable SHA-256 `06288db0e48605e81e38a371606d0c5c14ba98378ae8cd0bca9b138f847f78ce`. Official setup's dependency graph check and the locked release build passed. A signed project-local test catalog was used after the owner explicitly authorized test key creation. Those keys, catalog and signatures are not shipped in this repository and do not constitute official App Hub acceptance.

The full native host installed and launched the app through its normal permission page. Clicking 查询 AI 预算 displayed **宿主 AI 预算：今日调用 0/100；剩余 token 100000**. A separate storage-only probe requesting the same service returned **this app was not granted "model", which "model.budget" needs**. The model-enabled probe returned calls_today 0, calls_per_day 100, tokens_today 0, tokens_per_day 100000, tokens_left 100000 and per_minute 6. These are host limits, not MiniMax Plan or voucher balances.

The app's full-host flow also accepted synthetic unfinished-email input, organized it with existing local rules, and saved the draft. The file readback contained the supplied experiment detail. The root content now scrolls so actions remain reachable in the host's smaller module window. Only explicit budget clicks contact the service. Source edits, cancellation and observation state changes invalidate pending responses; requests have a 15-second timeout and no automatic retry.

Standalone reference-host regression evidence covers 12 manual checks, 17 observation checks and 7 missing-service/data-preservation checks. These checks do not exercise delayed or malformed successful host replies. The timeout and request-generation protection are implemented but not independently verified using a delayed host fixture. Missing service produced the actual error `no service answers "model" on this device`; existing input remained available.

The first probe attempted to serialize the whole host reply object and hit the pinned runtime's JSON heap guard. The repaired probe copied only documented scalar budget fields into a plain object. App status reads those scalar fields directly. UI checks match the named `ai_status_label`, not arbitrary text in a Splash source field.

Next acceptance: verified provider and voucher enforcement, then a real structured call returning has_task, evidence, missing_information, next_step and draft. No generator success or competition acceptance is claimed for this milestone.
