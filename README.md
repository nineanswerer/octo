# 南下 · 无提醒 Agent

**从授权邮件主动识别与你有关的事项、截止时间、改期和取消，保留证据，不催促你。**

例如邮件说“今天晚上6点前交稿”，记录事项；后续“改成明天中午”，更新同一事项并保留旧期限；再说“取消”，标记取消并保留记录，不能当作完成。

**[作品演示、截图和应用包下载](submission/2026-10-06/README.md)** · [中文使用说明](README.zh-CN.md) · [需求与范围](BRIEF.md)

当前 **0.5.3，纯 OctoScript**，使用官方宿主mail/model/storage服务。只观察一个邮箱最近5封，应用打开时每30秒检查，重启默认停用。先核验来源，再单独同意云分析；不发送邮件、不弹提醒、不扫描其他应用。

## 当前验证

27项合成原生业务检查、5项生产界面检查及8项录像检查通过。正常业务演示使用合成邮件和预设模型响应，已明确标注；**真实邮箱与在线模型完整业务回环尚未验收。** [验证与限制](validation/COMMITMENT_CHANGES.md) · [App Flow对照](validation/APP_FLOW_AUDIT.md)。

## 运行

正式业务需要带官方mail/model服务的完整OctoSense宿主，配置本人可用模型并授权邮箱。应用不收集密码或模型密钥。[宿主版本与启动](docs/RUNNING.md) · [模型配置](docs/OFFICIAL_RUNTIME_AI.md)。

独立card-host只能查看界面与缺服务状态。在Windows设置OCTO_CARD_HOST为对应card-host.exe的完整路径后运行octocard.bat。仅验证Windows。

## 交付文档

| 内容 | 入口 |
| --- | --- |
| 使用与隐私 | [中文说明](README.zh-CN.md)、[权限和数据](PRIVACY.md) |
| 可复现验收 | [测试邮件与验收步骤](docs/REAL_MAIL_ACCEPTANCE.md)、[合成录像复现](demo/INITIAL_0.5.3.md) |
| 当前审核材料 | [七项回答](build/REVIEW-ANSWERS.md)、[审核包](build/review.json) |
| 提交版本及状态 | [赛事与App Hub记录](SUBMISSION_NOTES.md) |
| 许可与反馈 | [Apache-2.0](LICENSE)、[项目Issues](https://github.com/nineanswerer/octo/issues) |

作者nineanswerer，队伍南下。[官方赛事报送](https://github.com/gosimfoundation/hackathon-agenticapp26/issues/13#issuecomment-5992477923)。App Hub [#74](https://github.com/OctoSense-org/OctoSense-App-Hub/issues/74)仍固定v0.5.1、待审核；不代表赛事晋级或已上架。
