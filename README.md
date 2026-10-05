# 南下 · 无提醒 Agent

[官方 App Design Flow 核查](validation/APP_FLOW_AUDIT.md)：当前截图与七项审核材料已补正；真实邮箱与在线 AI 完整回环尚未验收，不能宣称完整流程全部通过。

**初赛交付入口：[0.5.3演示与关键截图](demo/INITIAL_0.5.3.md) · [固定版本与提交记录](SUBMISSION_NOTES.md) · [中文使用说明](README.zh-CN.md)。** 视频约2分6秒，明确标注合成邮件和预设模型响应；真实邮箱/在线AI回环尚待验收。

最新开发版本 **0.5.3**：更新时保留变更前原文与出处，取消保留原事项并明确“取消不代表完成”；历史满时停止写入。27项合成原生及5项生产界面检查通过，[验证与限制](validation/COMMITMENT_CHANGES.md)。真实语义关联、乱序、用户纠正和真实邮箱回环仍待完成。下方0.5.2授权说明继续适用；App Hub审核仍固定v0.5.1。

**让 AI 从授权来源主动识别需要记录的事，而不是由人逐条创建待办。**例如邮件说“今天晚上6点前交稿”，AI判断是否与你有关，记录事项、截止时间原文与出处；后续说“改成明天中午”，更新同一事项。

0.5.3沿用 **0.5.2的单独云分析确认机制，纯 OctoScript 应用**。已实现邮箱与模型请求、事项保存读回、更新、去重及账号绑定；先准备来源，再明确同意本次分析，确认前重新核对账号。24项合成原生检查及5项生产界面检查通过；**真实邮箱与真实模型的完整回环尚待本人授权验收，不能称为已完成。** [本次证据](validation/CLOUD_CONSENT.md)。App Hub [#74](https://github.com/OctoSense-org/OctoSense-App-Hub/issues/74)提交的固定版本仍为0.5.1，尚待审核。

Windows 宿主邮箱凭据存储修复尚未验收，此前请勿接入私人邮箱凭据。网页登录仍在开发。当前执行顺序见[邮箱接入计划](docs/MAIL_INTEGRATION_PLAN.md)，本次验证见[0.5.1来源绑定](validation/MAIL_SOURCE.md)。

已核查[十个官方仓库的更新](docs/UPSTREAM_REVIEW_2026-10-04.md)：新版宿主已有新邮件事件驱动 Agent 的参考实现，后续优先评估复用；尚未升级本机宿主或宣称真实回环完成。

## 如何使用

1. 在带官方 `mail` 和 `model` 服务的完整 OctoSense 宿主中加载应用，配置可用模型。
2. 点击“连接邮箱”，在宿主授权页面完成登录。应用不收集密码。
3. 点击“启用观察与 AI 分析”核验来源，查看邮箱与数据用途，再点击“同意本次云分析并开始”。拒绝不会读取邮件正文或调用模型；停用、错误或重启需重新同意。
4. 查看自动记录的事项、截止原文、证据及出处；需要时点击“停用观察”。

仅应用打开时每30秒检查，重启默认停用；历史及去重各100条，满后停止。不发送邮件、不弹提醒。不扫描其他软件；最近5封之外可能遗漏。AI可能误判，时间不确定时保留原文供核对。

`octocard.bat` 仍可打开独立渲染器查看界面，但它没有邮箱和模型服务，**不能完成上述回环**。只验证 Windows。宿主构建与配置见下方文档，仓库不附带宿主二进制或凭证。

## 文档与交付材料

| 内容 | 入口 |
| --- | --- |
| 中文使用说明 | [授权、启用与保存位置](README.zh-CN.md) |
| 项目需求 | [核心目标与初赛最小范围](BRIEF.md) |
| 新版本验证 | [0.5.0真实检查与合成测试的区别](validation/TASK_OBSERVER.md) |
| 真实回环验收 | [四封测试邮件与验收步骤，尚待执行](docs/REAL_MAIL_ACCEPTANCE.md) |
| 合成记录截图 | [原生界面，非真实AI理解证据](validation/OBSERVER_SYNTHETIC_RECORD.png) |
| 初赛交付状态 | [固定版本、实际提交与未验收内容](SUBMISSION_NOTES.md) |
| 官方 AI 配置 | [宿主、模型与配置条件](docs/OFFICIAL_RUNTIME_AI.md) |
| 宿主复现 | [构建记录](validation/INITIAL_DELIVERY.md) |
| 开发计划 | [赛制节点与当前优先级](DEVELOPMENT_PLAN.md) |
| 数据与隐私 | [读取、保存、停用及权限范围](PRIVACY.md) |
| 旧版0.4.1演示 | [旧草稿原型录像和截图，非0.5.0回环](demo/README.md) |
| 旧版冻结记录 | [0.4.1文件指纹](release/INITIAL_FREEZE.json) |
| 开源许可 | [Apache-2.0](LICENSE) |

旧草稿原型保留在 [`v0.4.1-initial`](https://github.com/nineanswerer/octo/tree/v0.4.1-initial)，未覆盖标签。当前开发代码与旧录像不能混作同版本证据。初赛仓库地址已在官方赛事[#13评论区](https://github.com/gosimfoundation/hackathon-agenticapp26/issues/13#issuecomment-5947691976)报送；App Hub #74已递交但待审核，不代表赛事通过。
