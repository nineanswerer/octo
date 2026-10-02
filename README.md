# 无提醒 Agent (No-Reminder Agent)

> **The Intent Is the App** — OctoSense entry for GOSIM Agentic App Hackathon 2026

[English](#) | [简体中文](README.zh-CN.md)

## What's this

An anti-reminder app. Agent watches your **half-finished signals** (draft emails, untouched courses, broken promises) and surfaces "next 30 seconds" cards — **without nagging**.

The anti-common-sense insight: **people who procrastinate the most will never set their own reminders.** Every reminder app assumes user initiative — this one doesn't.


## Demo Video

Watch the 60-second demo: [`demo.mp4`](./demo.mp4) (<1 MB, MP4 H.264 + AAC narration).

## The Agentic loop

```
Observe  half-finished signals across mail/calendar/files/chat
Infer    what you probably mean to do
Surface  a 30-second "next step" card at the right moment
Confirm you keep full control — every action needs your tap
Learn    your procrastination patterns over time
```

# Run
export OCTO_HUB="$(pwd)/target/release/hub.exe"
export OCTO_CARD_HOST="$(pwd)/target/release/card-host.exe"
cd ../OctoScript-App-Design-Flow
python tools/octo run ../../apps/no-reminder-agent/bundle --port 8141 --hidden --detach

# Drive via HTTP
curl 127.0.0.1:8141/snap

# Quit
curl 127.0.0.1:8141/quit

# Check (gate)
python tools/octo check ../../apps/no-reminder-agent/bundle --allow-unsigned
```

### One-click (Windows desktop)

Double-click `octocard.bat` in `C:\Users\steam\Desktop\octo\` — auto-starts the app at port 8141.

## Capabilities

- `storage` (only) — local persistence in `<app-data>/no-reminder-agent/threads.json`

## Files

- `bundle/main.splash` — the program (Splash / Octoscript DSL, ~13K bytes)
- `bundle/manifest.json` — schema-1 manifest
- `bundle/listing.json` — store listing
- `bundle/screenshots/01-05.png` — 5 real PNG captures (main/detail/after-complete/after-signal/empty-state)
- `demo.mp4` — 60-second demo video
- `BRIEF.md` — design rationale
- `DEMO-SCRIPT.md` — demo script notes

## What we are NOT doing

- ❌ No real email/calendar API integration (mock data for demo)
- ❌ No background tasks (UI-triggered simulation)
- ❌ No nag / push notifications
- ❌ No "I'll do it for you" — only help you **start**

## License

Apache-2.0