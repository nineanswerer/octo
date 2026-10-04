# 官方仓库更新复核（2026-10-04）

只读核查了本项目引用的十个官方仓库默认分支；没有合并上游、切换工作树或升级当前运行依赖。以下为核查时的固定提交，后续 main 可能变化。

| 仓库 | 最新提交 | 相对本机参考 |
|---|---|---|
| 赛事 hackathon-agenticapp26 | 0db87b58 | 有更新 |
| OctoScript-App-Design-Flow | a5a87d3c | 有更新 |
| OctoSense-Desktop | 127ae4bd | 有更新 |
| OctoSense-App-Hub | e014fa9c | 有更新 |
| OctoLoop / octoscode | eff53121 | 一致 |
| Rinx | f18869e4 | 有更新 |
| Makepad | c155f61d | 有更新 |
| OctoScript | f67cb843 | 有更新 |
| Octoscript-Makepad | 2cc5ef37 | 有更新 |
| octos | dde76555 | 有更新 |

“有更新”仅指提交不同；不是升级后已构建或验收。

## 对当前作品直接有用的更新

1. **官方已实现新邮件触发 Agent 的流程。** 邮箱授权与 Agent 许可后，宿主持久保存新邮件事件，调用模型判定，发布卡片或明确跳过；不需要用户逐封提示。队列、账号绑定、撤销与退避处理已有源码，优先研究复用，避免重造这些机制。该实现属于系统 Mail 的宿主集成，不能假定普通商店应用可直接调用系统 Agent 接口。现有 Windows 宿主尚未升级验收。通知行为也不能自动套用到“无提醒”作品。[固定版本中文说明](https://github.com/OctoSense-org/OctoSense-Desktop/blob/127ae4bd5a5476f0b813179868e61f80748a044e/docs/mail-agent-events.zh-CN.md)
2. **新增模型驱动开发与验证教程。** 完成取决于最终源码的原生输入、截图、状态和文件证据；工具成功或模型自己的 ACK 不等于验收。教程区分桌面、Android、模型视觉传递与真实服务验证，与本项目目前独立复验原则一致。[中文教程](https://github.com/OctoSense-org/OctoScript-App-Design-Flow/blob/a5a87d3c3ff305768ae46bc5f6689abb48115cc4/docs/MODEL-VALIDATION.zh-CN.md)
3. **App Hub 增加结构准入。** 检查运行入口、图片可解码、SVG 外部引用、文件数量/深度/大小和文本格式；不会执行应用业务。当前0.5.1使用已有二进制通过预检，不等于最新 e014fa9c 门禁已经跑过，须另建隔离验证环境。[固定准入源码](https://github.com/OctoSense-org/OctoSense-App-Hub/blob/e014fa9c596cdbd95de5cf9fb2a6b4fc2b781d17/crates/app-hub/src/admission.rs)
4. **存储授权写入教程与门禁。** 使用 fs 需 storage capability；本作品已声明。框架版本也有更新，须按官方锁文件成套核对，不单独混用各仓库最新 HEAD。

## 登录和赛制边界

所查最新 Mail 文档仍让用户在宿主登录面板连接账号；新事件功能不是 Gmail/Outlook OAuth 教程，也没有消除本作品 Client ID 注册前置条件。最新 vault 的 Windows 路径仍未提供所需加密实现；本机隔离修复继续验收。

赛事最新提交与旧版本的 competition-schedule.md、app-hub-submission.md 差异为空：初赛仍为 **10月4日23:59，北京时间**。此结论限于该官方仓库，不能替代未取得的群内最新通知。[固定赛程](https://github.com/gosimfoundation/hackathon-agenticapp26/blob/0db87b582438f0f01534435b8537e8c89bcd303d/docs/competition-schedule.md)

执行顺序：保留已验证0.5.1 → 完成 Windows 凭据存储与来源隐私边界 → 在隔离环境评估新版官方邮件事件机制和新 Hub 门禁 → 依据实际接口选择最小复用方案 → 完成网页授权与真实业务验收。初赛包继续保持纯 OctoScript，不将开发双环或宿主扩展塞入应用包。
