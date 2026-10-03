# 南下 · 无提醒 Agent 0.4.1

面向有半完成邮件或笔记、却难以继续写的人。只处理你提供的内容，不催促、不自动发送。

已验证：本地规则整理、编辑、确认保存、读回核验、重启恢复和失败反馈。可显式启用应用内已保存来源草稿的处理，支持版本、忽略、暂缓及去重；不观察外部邮箱或后台事件。

官方 AI 接口已实现，但需要完整宿主及模型配置。现有本地模型测试只证明调用链路，输出质量未通过；不能称为可靠的 AI 应用。开发双环与应用运行时分开。

在本仓库打开 PowerShell：

```powershell
$env:OCTO_CARD_HOST='C:\Users\steam\Desktop\octo\runtime\host-repro\OctoSense-App-Hub\target\release\card-host.exe'
& .\octocard.bat
```

输入原文 → 整理草稿 → 编辑 → 确认保存。保存位置为 `.local-state/no-reminder-agent/`，状态明确为“尚未发送”。此入口只启动渲染器，AI 按钮不能靠它完成模型请求。

[复现与验收](validation/INITIAL_DELIVERY.md) · [演示](demo/README.md) · [交付状态](SUBMISSION_NOTES.md) · [官方 AI 配置](docs/OFFICIAL_RUNTIME_AI.md) · [隐私](PRIVACY.md) · [开发计划](DEVELOPMENT_PLAN.md)。只验证 Windows；未取得正式初赛或 App Hub 接收回执。
