# Current 0.4.0 update

An explicit AI button now calls the official host's `model.complete` interface, handles structured evidence/missing information/next step/editable draft, and keeps confirmation plus save readback. The application does not read or reuse development-agent credentials. Local rules remain a fallback.

53 native UI/file checks passed across real service-error paths, synthetic callbacks and existing workflows. In the full official Windows host, the actual call returned `no_provider`; no provider-backed generation is claimed. Configure AI through the host's official AI providers settings. [Validation and limitations](validation/AI_COMPLETE.md), [privacy](PRIVACY.md).

# Previous 0.3.2 update

The app now queries the official host's AI budget through `model.budget` on an explicit click. Successful budget retrieval, refusal without model permission, and actual draft saving were verified in the complete Windows host through a signed local test catalog. This is a service connection check: the app still uses local rules and does not call `model.complete`. The budget is a host call/token limit, not money or voucher balance. [Validation and limitations](validation/AI_BUDGET.md).

# Previous 0.3.0 update

Explicit opt-in app-owned draft processing with source revisions, ignore/defer and duplicate suppression is now implemented. See [observation behavior and validation](validation/OBSERVER.md). No online model or external/background observation. The earlier 0.2.0 recording below is historical.

# No-Reminder Agent 0.2.0

Windows OctoSense local draft helper. Paste an unfinished email, organize, edit and confirm saving. Local keyword rules preserve the original text and add a neutral closing. Saved files are read back and restored on restart.

Current runtime does not monitor email, use online models, send messages, observe in the background or learn timing. MiniMax development agents are separate from runtime behavior.

## Run

Set OCTO_CARD_HOST to an absolute Windows card-host.exe path, then run octocard.bat. Data defaults to .local-state. No host binary is included. Only Windows was tested.

Check with: hub.exe check bundle --allow-unsigned. The development bundle is unsigned; signature-requiring hosts refuse it. Local admission does not establish official installation or competition acceptance.

## Evidence

Twelve native UI/file checks passed: empty start/input, unrelated text, generation, changed-source protection, save/readback, repeated save, restart, cancellation, clearing, write failure and inconsistent restore. [Results](validation/mail-mvp.json), [screenshot](bundle/screenshots/01-main.png).

Tested host SHA-256: BF277982100470A5C2AE0C9E5AEA556802ED7A61ADD64432D606BA2A79DAB1EF. This identifies a local binary, not a certified competition baseline. [Current 122.5-second demonstration](demo/mail-workflow.mp4) and [recording details](demo/README.md) are available. Final submission and official acceptance remain pending.

[Privacy](PRIVACY.md), [plan](DEVELOPMENT_PLAN.md), [Apache-2.0 license](LICENSE). Sole entrant nineanswerer; registration confirmed by entrant.
