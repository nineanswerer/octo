# 南下 · 无提醒 Agent 0.4.1

A Windows draft helper for unfinished email or notes: provide text, organize a small next step, edit, confirm saving, and verify the saved result. No notifications or automatic sending. Reducing startup effort remains a hypothesis, not a measured benefit.

Current verified behavior: local-rule organization, editing, explicit save/readback, restart recovery and failure handling. Opt-in processing is limited to this app's saved source drafts, with revisions, ignore/defer and duplicate suppression. It does not inspect external mail or run a background watcher.

The official host interfaces `model.complete` and `model.budget` are implemented. A complete OctoSense host and its configured AI provider are required. The existing local R1 test verified transport but failed output quality; successful real AI generation through confirmed save is not accepted. Synthetic response checks are labeled. Development Codex/MiniMax agents are separate from runtime AI.

## Run on this computer

Open PowerShell in this repository and run:

```powershell
$env:OCTO_CARD_HOST='C:\Users\steam\Desktop\octo\runtime\host-repro\OctoSense-App-Hub\target\release\card-host.exe'
& .\octocard.bat
```

Paste unfinished text, choose 整理草稿, edit, then 确认保存. Saved data lives under `.local-state/no-reminder-agent/`. The standalone renderer has no model service. Full-host AI configuration is described in [official setup](docs/OFFICIAL_RUNTIME_AI.md).

For another machine, build the pinned renderer and set `OCTO_CARD_HOST` to its absolute executable path; [reproduction evidence](validation/INITIAL_DELIVERY.md) identifies the source, binary and commands. Only Windows is verified. Host binaries and credentials are not shipped.

## Initial-round evidence

[Current native recording and two screenshots](demo/README.md), [delivery and remaining limitations](SUBMISSION_NOTES.md), [product brief](BRIEF.md), [privacy](PRIVACY.md), [Apache-2.0 license](LICENSE).

Existing cumulative 60 native control/UI/file checks are not 60 real model cases. [AI validation](validation/AI_LIVE_LOCAL.md) separates real transport from failed quality. Admission and competition acceptance remain separate; no submission receipt is claimed.
