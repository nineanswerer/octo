# 无提醒 Agent · 南下

**持续维护邮箱中的本人承诺。** 自动创建、改期、取消，排除他人安排；保留原文与历史，允许人工核对和纠错。

0.5.6 交付版本，纯OctoScript，官方mail/model/storage服务。单一授权邮箱、最近5封、应用打开期间每30秒检查、重启默认停用。不发送邮件、不提醒、不扫描其他应用。

## 已验证

2026-10-12，固定0.5.5-rc.1核心在原版OctoSense RC2中，通过POP3 TLS及MiniMax-M3完成五封真实投递邮件的分析：创建纪要→同一事项改期→忽略他人取消→取消本人纪要→独立报名名单。两个事项、历史保留，重复扫描不重复调用，重启记录保持且默认停用。

邮件内容是合成测试，传输和模型分析是真实的；5例通过不代表任意邮件准确率。[本次真实验收](validation/REAL_MAIL_0.5.5.md)。另有53项本地UI/存储检查、9项完整RC2合成交互及7类新存储/来源场景；[异常覆盖边界](validation/LIFECYCLE_0.5.5.md)。

## 使用

1. 在完整宿主配置本人产品模型，宿主邮箱页面连接一个测试邮箱。
2. “启用观察与 AI 分析”核验来源，再单独“同意本次云分析并开始”；模型可能是云服务，费用由本人承担。
3. 查看原文、来源和历史。先停用观察，再确认或补充修正备注；确认不代表完成，备注不改原文。
4. 退出结束观察，重开需重新同意。

[中文说明](README.zh-CN.md) · [安装与无模型查看](docs/RUNNING.md) · [隐私](PRIVACY.md) · [复现](docs/REAL_MAIL_ACCEPTANCE.md)

## 交付与限制

[正式版本与提交状态](SUBMISSION_NOTES.md) · [演示](demo/SEMIFINAL_0.5.6.md)。固定正式版本为 [v0.5.6](https://github.com/nineanswerer/octo/releases/tag/v0.5.6)，工作流封存包及桌面安装回执在 Release。Hub准入和评分由维护者及评委决定。

本轮主媒体为 Release 中的实际 RC2 操作录屏，使用真实验收结果的脱敏保存副本，零新增云调用；采集232.518秒，编码后播放180秒。[复现补充与证据范围](https://github.com/nineanswerer/octo/releases/download/v0.5.6/REPRODUCING_0.5.6.md)说明原生POP3协议选择、历史资料及RC2/RC6证据边界。默认分支追加资料清理，不改固定v0.5.6标签或封存包。

仅验证Windows。网易126原版RC2的IMAP客户端缺ID，读箱被拒；本次用户开启POP3 TLS后验收，没有修复官方宿主。独立card-host没有mail/model服务。最近5封之外可能遗漏；事项/去重各100条、历史20条上限；相对期限保留原文，AI仍可能误判。

旧版本媒体及两个内含早期截图的0.5.3/0.5.4 ZIP已从当前默认分支移出；固定标签和早期验证报告保留历史，不能替代本轮主媒体、安装包或验收。Apache-2.0，作者nineanswerer，队伍南下。[反馈](https://github.com/nineanswerer/octo/issues) · [本队初赛82/100评语](https://github.com/OctoSense-org/OctoSense-App-Hub/issues/74)
