# 南下 · 无提醒 Agent

**从授权邮件主动识别与你有关的事项、截止时间、改期和取消，保留证据，不催促你。**

例如邮件说"今天晚上6点前交稿"，记录事项；后续"改成明天中午"，更新同一事项并保留旧期限；再说"取消"，标记取消并保留记录，不能当作完成。

**[0.5.4 历史演示、截图和应用包下载](submission/2026-10-06/README.md)** · [中文使用说明](README.zh-CN.md) · [需求与范围](BRIEF.md)

当前候选 **0.5.5-rc.1，纯 OctoScript**，使用官方宿主mail/model/storage服务。只观察一个邮箱最近5封，应用打开时每30秒检查，重启默认停用。先核验来源，再单独同意云分析；不发送邮件、不弹提醒、不扫描其他应用。

本候选增加事项详情，支持查阅来源证据和历史期限，并人工确认事项或保存修正备注。确认不代表完成，修正备注保留原邮件证据。

## 当前验证

**本候选的53项本地UI/持久化检查在当前源码上通过，详见 [本地验收记录](validation/local-review-0.5.5-rc.1.json)；完整RC2桌面、真实邮箱与模型回环、新版截图和录像仍待验收。** 候选截图为标注的原生合成示例，0.5.4历史材料不作为本候选新增功能的验收证据。

候选封存包将仅通过GitHub Actions artifact提供，生成与桌面验收尚待完成；本候选不创建GitHub Release、不作为最终提交，也未获得App Hub准入。

以下为 **0.5.4 历史验证记录**：27项合成原生业务检查、5项生产界面检查及8项录像检查通过。正常业务演示使用合成邮件和预设模型响应，已明确标注；**0.5.4 已完成真实 QQ 测试邮箱与在线 MiniMax 模型的5封受控业务回环：创建、改期、忽略他人事项、取消、独立新事项；重启保留记录并默认停用。** [历史真实回环结果](validation/real-mail-0.5.4-results.json)。这些结果不保证本候选、任意邮件的识别质量或官方审核。 [历史验证与限制](validation/COMMITMENT_CHANGES.md) · [历史App Flow对照](validation/APP_FLOW_AUDIT.md)。

## 运行

正式业务需要带官方mail/model服务的完整OctoSense宿主，配置本人可用模型并授权邮箱。应用不收集密码或模型密钥。[宿主版本与启动](docs/RUNNING.md) · [模型配置](docs/OFFICIAL_RUNTIME_AI.md)。

独立card-host只能查看界面与缺服务状态。在Windows设置OCTO_CARD_HOST为对应card-host.exe的完整路径后运行octocard.bat。0.5.4历史验证仅覆盖Windows，本候选的完整宿主验收尚待完成。

## 交付文档

| 内容 | 入口 |
| --- | --- |
| 使用与隐私 | [中文说明](README.zh-CN.md)、[权限和数据](PRIVACY.md) |
| 可复现验收 | [测试邮件与验收步骤](docs/REAL_MAIL_ACCEPTANCE.md)、[历史合成录像复现](demo/INITIAL_0.5.3.md) |
| 历史审核材料（0.5.4） | [七项回答](build/REVIEW-ANSWERS.md)、[审核包](build/review.json) |
| 提交版本及状态 | [赛事与App Hub记录](SUBMISSION_NOTES.md) |
| 许可与反馈 | [Apache-2.0](LICENSE)、[项目Issues](https://github.com/nineanswerer/octo/issues) |

作者nineanswerer，队伍南下。[官方赛事报送](https://github.com/gosimfoundation/hackathon-agenticapp26/issues/13#issuecomment-5992477923)。App Hub [#74](https://github.com/OctoSense-org/OctoSense-App-Hub/issues/74)仍固定v0.5.1、待审核；不代表赛事晋级或已上架。
