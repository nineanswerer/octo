# 南下 · 无提醒 Agent

帮助你继续完成写了一半的邮件或笔记：提供原文，整理草稿，编辑后确认保存，应用读回文件核验结果。不催促、不自动发送。

当前初赛候选为 **0.4.1，OctoScript 应用**，固定版本为 [`v0.4.1-initial`](https://github.com/nineanswerer/octo/tree/v0.4.1-initial)。

已验证本地规则整理、编辑、保存核验、重启恢复和失败反馈；支持应用内已保存来源的版本、忽略、暂缓及去重。跨软件主动发现需求是后续目标，目前尚未实现。

官方宿主 AI 接口已实现，但需要完整宿主和模型配置。现有本地模型测试证明了调用链路，输出质量未通过验收。开发时的 Codex / MiniMax 双环不属于应用运行功能。

## 使用方法

在本仓库目录打开 PowerShell，运行：

```powershell
$env:OCTO_CARD_HOST='C:\Users\steam\Desktop\octo\runtime\host-repro\OctoSense-App-Hub\target\release\card-host.exe'
& .\octocard.bat
```

输入原文 → 点击“整理草稿” → 编辑 → 点击“确认保存”。文件保存在 `.local-state/no-reminder-agent/`，成功状态为“已保存并核验，尚未发送”。

上述路径是本机已验证的渲染器。其他电脑需构建匹配宿主，并设置 `OCTO_CARD_HOST` 为其绝对路径；仓库不附带宿主二进制或密钥。独立渲染器没有模型服务。目前只验证 Windows。

## 文档与交付材料

| 内容 | 入口 |
| --- | --- |
| 中文使用说明 | [功能、启动与操作](README.zh-CN.md) |
| 项目需求 | [面向谁、解决什么问题、当前范围](BRIEF.md) |
| 初赛交付状态 | [已有材料、限制与待办](SUBMISSION_NOTES.md) |
| 当前版本演示 | [演示说明](demo/README.md) · [122.5 秒实录](demo/initial-0.4.1.mp4) |
| 两张关键截图 | [保存成功](demo/screenshots/initial-saved.png) · [保存失败](demo/screenshots/initial-failure.png) |
| 初赛独立验证 | [复现步骤与验证结论](validation/INITIAL_DELIVERY.md) · [12 项检查结果](validation/INITIAL_DELIVERY_RESULT.json) |
| 官方 AI 配置 | [宿主接口、模型配置与使用条件](docs/OFFICIAL_RUNTIME_AI.md) |
| AI 实测情况 | [真实调用与输出质量限制](validation/AI_LIVE_LOCAL.md) |
| 开发计划 | [赛制节点与验收条件](DEVELOPMENT_PLAN.md) |
| 数据与隐私 | [读取、保存与权限范围](PRIVACY.md) |
| 冻结版本信息 | [文件指纹与版本记录](release/INITIAL_FREEZE.json) |
| 应用包预检 | [预检输出](release/hub-check.txt) · [审查回答](release/REVIEW_ANSWERS.md) |
| 开源许可 | [Apache-2.0](LICENSE) |

演示展示本地规则流程，不代表已完成实时 AI。应用包预检、界面和文件验证、App Hub 上架及赛事接收是不同事项；目前没有正式初赛或 App Hub 接收回执。
