# Application-owned draft observation 0.3.0

Only app-owned saved source text is observed. Save source first; saving is not consent. Explicitly enable processing, then source saves and app startup can produce one local-rule suggestion without repasting. Disable stops processing. Source text changes invalidate pending actions. Content equality preserves revision; new content advances it.

Ignored, deferred and handled revisions persist and suppress repeated suggestions across restart. Deferral currently lasts until new content, without a scheduled notification; manual organize is an explicit way to process again. Cancellation of an observed suggestion suppresses its revision. Confirmed output alone writes the result; actual readback verifies success. Clearing removes the three fixed owned files and revokes consent.

No filesystem watcher, email access, background daemon, semantic model or network grant. Rule quality remains limited to keywords and preserving input with a neutral ending. This is the first consent/version state implementation, not complete autonomous task understanding.

Native host 6b9f33ff063c8afe94bec425e890fbc77b25364254fabf86300e3273f3c42da8: 17 observation/permission/version cases and 12 existing manual cases passed. Results: observer-results.json, observer-manual-results.json. Malformed source state does not grant permission. Windows only.

Development record: MiniMax task MCP-18b0cd49-85e1-470e-ac87-172d072a5b7d returned source with defects independently rejected by both Linux and desktop outer reviews. Desktop outer applied a deterministic corrected candidate and ran native acceptance. The model's exit status was not treated as acceptance. Historical 0.2.0 video remains historical and must not be presented as a 0.3.0 recording.
