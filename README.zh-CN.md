[Current 0.3.0 behavior and 29 passed checks](validation/OBSERVER.md). Historical 0.2.0 video below.

# 南下 · 无提醒 Agent 0.2.0

提供未完成邮件原文，应用以本地规则整理可编辑草稿；确认后保存并读回核验，重启恢复一致的草稿。取消不会覆盖以前保存的内容。

当前不读取邮箱、不发送邮件、不调用在线模型，也没有后台观察或时机学习。开发使用 MiniMax 不代表运行时模型能力。

运行与宿主要求见 [README](README.md)，权限见 [PRIVACY.md](PRIVACY.md)，开发节点见 [计划](DEVELOPMENT_PLAN.md)。Windows 实测 12 项通过：[验证记录](validation/mail-mvp.json)。未签名本地检查通过不等于官方收录或赛事验收。[122.5 秒实录](demo/mail-workflow.mp4)及[说明](demo/README.md)已完成，正式提交和接收回执仍待完成。
