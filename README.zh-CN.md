# 无提醒 Agent

> **意图即应用** — GOSIM Agentic App Hackathon 2026 参赛作品

[English](README.md) | [简体中文](#)

## 这是什么

一个**反常识的提醒 App**。Agent 盯着你的"半完成信号"（邮件草稿、买了没上的课、答应了没做的事），浮现"下一步只要 30 秒"的卡片——**不催不推**。

反常识洞察：**拖延最严重的人，永远不会主动设置提醒**。所有提醒 App 都假设用户有主动性——这一个不假设。

## Agent 闭环

```
观察 跨邮件/日历/文件/聊天的半完成信号
推断 你可能要做的事
浮现 在对的时间浮现"轻量下一步"卡片（不打断）
确认 你保留完全主动权——每个动作都要你点
学习 逐渐了解你的拖延模式
```

## 试用 Demo

打开 app 立刻看到 6 条预设信号（邮件草稿、买了没上、承诺没兑现等）。点任意一条 → 看到 Agent 的"下一步 30 秒"建议 → 完成 / 暂缓 / 放弃。

点 **"+ 模拟 Agent 发现新信号"** 模拟 Agent 实时发现新信号。

## Build & Run

前置（都在 `octosense-ws/`）：

- `OctoSense-App-Hub/`（在这里 build card-host + hub）
- `makepad/`, `octoscript-makepad/`, `Octoscript/`（sibling 仓，symlink）

```sh
cd octosense-ws/OctoSense-App-Hub
cargo build --release -p octosense-card-host -p octosense-app-hub

# 跑
export OCTO_HUB="$(pwd)/target/release/hub.exe"
export OCTO_CARD_HOST="$(pwd)/target/release/card-host.exe"
cd ../OctoScript-App-Design-Flow
python tools/octo run ../../apps/no-reminder-agent/bundle --port 8141 --hidden --detach

# HTTP 桥操控
curl 127.0.0.1:8141/snap

# 退出
curl 127.0.0.1:8141/quit

# check
python tools/octo check ../../apps/no-reminder-agent/bundle --allow-unsigned
```

## Capabilities

- `storage`（仅此一个）——本地持久化在 `<app-data>/no-reminder-agent/threads.json`

## 文件

- `bundle/main.splash` — 程序（Splash / Octoscript DSL，~13K 字节）
- `bundle/manifest.json` — schema-1 manifest
- `bundle/listing.json` — 商店 listing
- `bundle/screenshots/` — 5 张真实 PNG
- `BRIEF.md` — 设计文档
- `DEMO-SCRIPT.md` — 60 秒视频脚本

## 不做的事

- ❌ 不接真实邮件/日历 API（用 mock 数据演示）
- ❌ 不做后台定时任务（UI 触发模拟）
- ❌ 不催、不推、不打扰
- ❌ 不"替你做"——只帮你**启动**

## License

Apache-2.0