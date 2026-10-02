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
