# Official runtime AI setup verification — 2026-10-03

Application baseline: 0.4.1 / 87a6066. This change adds setup documentation and a read-only configuration diagnostic; application code and provider settings are unchanged.

MiniMax Plan implementation receipt: MCP-15559edc-ac18-4de7-9cbf-4358c0f15de0, dispatched under the official outer-duty lock with Codex outer review. Fresh quota was 96% interval / 49% weekly. Ordinary API disabled. Inner output contained an incorrect fallback field/unreachable branch and incomplete malformed-encoding handling; outer corrected these before acceptance. Its self-reported verification was not taken as test evidence.

Outer command `python runtime/verify_runtime_ai_config.py` passed 13 cases: missing profile, configured profile, BOM, invalid JSON, invalid encoding, array/null root, disabled/nonboolean-enabled, missing/malformed config, malformed llm, and empty primary. Checks include exact exit/status, counting only valid fallback selections, no secret/path/provider output, no stderr and preserving profile bytes. These are synthetic configuration checks, not model responses.

Outer command `python runtime/verify_official_ai_setup_ui.py` launched the existing full official Windows shell with isolated project-owned home/data/core and captured its actual native AI providers page. Exact labels Add model and No models yet were observed, and the screenshot was independently inspected. No model requests, connection tests, credential imports or configuration writes were performed. Only the owned shell process was closed. [Actual screenshot](OFFICIAL_AI_PROVIDERS.png).

The initial inspection helper printed too much text and hit Windows stdout encoding; its output was restricted and UI assertions tightened, then the final command completed successfully. Render success does not establish that provider authentication, network connectivity or generation works.

Full shell source: cf85350129830605d08973befdd8bde6480f6a77. Binary SHA256: 06288db0e48605e81e38a371606d0c5c14ba98378ae8cd0bca9b138f847f78ce.

The setup guide follows the [official model service](https://github.com/OctoSense-org/OctoSense/pull/95). Host-configured inference and development-agent funding are distinct. No universal free runtime endpoint was found in the checked public event/source documents; this is not proof that organizers cannot separately supply a configuration. Actual remote-model quality and confirm/save/readback acceptance remain pending.
