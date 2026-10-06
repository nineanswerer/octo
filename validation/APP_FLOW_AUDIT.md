# 官方 App Design Flow 对照核查（2026-10-05）

依据：[script-app/FLOW.md](https://github.com/OctoSense-org/OctoScript-App-Design-Flow/blob/main/flows/script-app/FLOW.md)。源码权威为本仓库 master；初赛冻结 `v0.5.3-initial` 保留不变，App Hub #74 仍是 v0.5.1，二者不是本次 master 材料补正。

| 流程 | 当前证据与边界 |
| --- | --- |
| 1–4 需求、脚本及权限 | BRIEF.md、bundle/main.splash 和 manifest；mail/model/storage 均有用途。历史建包过程不在本次重新执行。 |
| 5–9 原生运行、交互及状态 | validation/COMMITMENT_CHANGES.md、initial-0.5.3-recording.json；27项合成回归、5项生产界面、8项录像检查。生产包可渲染；独立 card-host 缺 mail/model 服务。完整真实回环未验收，不能称所有业务动作均已验证。 |
| 10–11 展示信息及截图 | 本次将 listing 的旧截图索引改为当前生产包的真实空状态与缺服务失败截图；均已打开核查。合成事项视频另有醒目标注，不能代替最佳真实业务状态截图。 |
| 12 包检查 | 本次 stamp 后 check --allow-unsigned：no-reminder-agent 0.5.3 — PASSED；仅 publisher-signature 未签名警告。宿主工具固定旧版本 0f332112，未宣称最新官方宿主已验收。 |
| 13 审核包与七问 | 本次重新 hub scan，build/review.json 的源码等于当前 main.splash；build/REVIEW-ANSWERS.md 回答全部七问，建议 human-review。 |
| 14 报告及交付 | 仓库首页、SUBMISSION_NOTES.md、演示和本记录说明限制；尚无官方批准，不等于已上架。 |

命令（工作目录为项目根的上一级 octo）：

```powershell
runtime/host-repro/OctoSense-App-Hub/target/release/hub.exe stamp git-repo/bundle
runtime/host-repro/OctoSense-App-Hub/target/release/hub.exe check git-repo/bundle --allow-unsigned
runtime/host-repro/OctoSense-App-Hub/target/release/hub.exe scan git-repo/bundle --packet git-repo/build/review.json
```

本次只改截图索引、包摘要及审核文档，未改应用源码。截图来自 INITIAL-053-RECORDING-001 已保存的原生捕获，无重新模拟在线模型。

测试入口优先考虑 Makepad Studio；已有 card-host 的 Makepad 远程调试接口也可启动、点击、查看帧与状态，官方 Flow 正是允许此路径，不要求 Computer Use。本次未声称已经通过 Studio 启动或完成完整宿主服务测试。下一步应在具备官方 mail/model 服务且凭据存储安全的完整宿主，验证真实 create/update/cancel 和失败/重启；避免新增无关功能。

## 2026-10-06 真实回环补充

以上表格保留10月5日核查历史。当前0.5.4已通过5封真实QQ测试邮件与在线模型的创建、改期、忽略、取消、独立事项回环，以及停用和重启保存核验。修复经27项合成原生回归；重新stamp/check通过（仅未签名警告），scan生成当前源码审核包。[真实验收](REAL_MAIL_0.5.4.md)。真实业务截图、全新环境复现和官方审批仍不能据此宣称完成。
