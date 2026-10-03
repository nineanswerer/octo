# 初赛交付说明 — 2026-10-03

队伍：南下。作品：无提醒 Agent / no-reminder-agent 0.4.1。唯一参赛者 GitHub ID：nineanswerer；本人已确认个人报名。私密登记信息不放公开仓库。

公开仓库：https://github.com/nineanswerer/octo 。源码许可 Apache-2.0。原型为 Windows Hub script bundle，来源为用户输入和应用自有草稿。需求见 BRIEF.md；入口与操作见 README.zh-CN.md；权限及隐私见 PRIVACY.md。

核心流程：输入 → 本地规则整理 → 编辑 → 用户确认保存 → 文件读回 → 重启恢复。已有取消、来源变化、空状态与保存失败处理。官方 AI 接口存在，但模型输出质量未通过，完整真实 AI 生成与保存闭环未验收。没有邮箱读取、发送、后台信号或时机学习。

初赛演示、两张关键截图和同源码复验见 demo/README.md 与 validation/INITIAL_DELIVERY.md。应用包仍未签名；本地准入不是上架、正式比赛接受或晋级证明。

官方公开赛程写明初赛截止 2026-10-04 23:59 北京时间，需需求、可运行原型及启动说明、固定源码/包、2–3分钟演示、两张截图、来源及限制、已报名成员名单。应以最终通知为准。

本次交付可供报送准备，但正式提交入口和接收回执仍未确认。赛事 Issue #5仅收集主题和队伍信息，App Hub Submit issue是应用发布渠道；都不能擅自当作最终初赛报送入口。公开源码与可运行作品可先准备，无需等待 Hub 上架。

提交前引用 release/INITIAL_FREEZE.json 中的固定源码/包指纹及本次提交对应 tag，不使用会继续变化的 master 代替冻结版本。冻结之后的新开发另列版本，不替换初赛证据。

官方依据：
- https://github.com/gosimfoundation/hackathon-agenticapp26/blob/main/docs/competition-schedule.md
- https://github.com/gosimfoundation/hackathon-agenticapp26/blob/main/docs/app-hub-submission.md
