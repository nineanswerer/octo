# Official host with real local inference — 2026-10-03

The 0.4.0 signed local test application (source SHA256 d6630e2db22a0166ac02708523bc0c72521537d265c7bbef0616e4ae0e845da7) was launched inside the same pinned complete official Windows host. This private copy predates the production source line-ending cleanup; it is not byte-identical to the public source. Its actual model.complete request was answered by the locally cached deepseek-r1:7b through a loopback-only Ollama server on port11439. No model downloads, cloud route, API key, competition voucher or development credential was used. The isolated host profile selected official family_id=local, OpenAI-compatible loopback route, empty fallback list and empty env_vars. Personal profiles were not changed. The test profile was removed after the exact owned process was stopped and the cached model unloaded.

## Observed result and quality finding

The actual native UI displayed original evidence and a clarification next step. The model-generated draft was only `待补充`. The official structured-response transport and application callback succeeded, but this draft omits the known completed data-ingestion fact and is not a useful progress email. **Business quality acceptance failed.** A successful HTTP reply or schema-valid object is not enough.

The server log recorded two actual chat-completions requests, approximately25.09s and10.85s; this is consistent with the official host's bounded structured-output retry, not an application retry loop. No cost or exact token count is inferred from these durations. The screenshot is an unmodified real native capture using synthetic input and actual inference, not a mocked result. See AI_LIVE_LOCAL_RESULT.json and AI_LIVE_LOCAL.png.

## Additional timeout verification

Five independent native UI/file checks passed using a clearly synthetic48s transport while leaving the production45s timeout unchanged. Timeout observed at45.22s; input retained; no automatic save; late valid callback ignored; confirmation remained blocked. See AI_TIMEOUT_RESULTS.json. These are timeout/control-flow checks, not model-quality evidence. Together with the prior53 checks,58 native UI/file checks have passed; the single real local inference connection is reported separately.

MiniMax Plan task receipt MCP-99abe6b5-d13b-442d-901f-9f1a5c684183 was actually dispatched under the official outer lock with current quota97% interval/49% weekly. Its test script contained pass stubs, unconditional true assertions and Python-file patching instead of Splash transport patching. Outer rejected it before execution; retained privately. The passing timeout harness was written and run independently by desktop Codex. Do not attribute passing checks to the inner ACK.

## Next bounded work

### 0.4.1 follow-up

MiniMax receipt MCP-d6a38709-978f-4f2c-8927-4afed1879fd6 implemented only a strengthened generation contract and a guard rejecting drafts consisting solely of `待补充` or `[待补充]`; desktop outer independently inspected the diff. Eleven synthetic-response native checks passed, adding placeholder refusal and blocked save to the earlier nine. With five timeout checks, the cumulative control-flow/UI/file set now totals60 checks, separate from actual model-quality acceptance.

The real model test checked the installed version was0.4.1 before clicking. It returned evidence the application could not match to the original source, and the application correctly rejected it (`AI 证据与原文不符`). Real model quality remains failed. Neither a placeholder draft nor mismatched evidence is relaxed to obtain a passing demonstration. See AI_QUALITY_LOCAL_RESULT.json and AI_QUALITY_SYNTHETIC.json. Source SHA256 f2f34fe91974c83999c88f6a7b1d3ef4415a87d21970ed32456cda767d3e4dae.

Improve the prompt/result contract so drafts preserve known facts and missing facts produce concrete labeled placeholders; reject placeholder-only drafts. Repeat the real model case and independently assess the draft before accepting. Then run the six-case actual-model quality set, including completed/neutral text, uncertainty and injection. Once useful generation plus confirmation/readback is verified in the full host, prepare a reproducible local-model launch path and same-version demonstration. Local model installation or cached manifests alone do not guarantee performance on another device; no cross-platform or official competition acceptance is claimed.

Implementation references: [official model.complete](https://github.com/OctoSense-org/OctoSense/pull/95), [Ollama local OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility). The application continues to call the official service and never a model endpoint directly.
