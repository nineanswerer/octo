# 0.5.2 单独云分析同意验证

2026-10-04。基于0.5.1来源绑定；开发使用一次可见MiniMax Plan派单，Codex静态修正并独立原生复验。内环回执不是验收结果。

启用按钮只核验账号并保存来源；同意按钮重新核对准备时的唯一账号/地址/INBOX后才读取邮件与分析。拒绝、停用、服务错误及重启清空临时同意与等待来源；迟到回调通过generation失效。不保存或自动恢复同意，不新增服务/权限。

`python runtime/verify_commitment_consent_ui.py --bundle runtime/worktrees/commitment-consent/bundle --output runtime/verification/COMMITMENT-CONSENT-003 --host runtime/host-repro/OctoSense-App-Hub/target/release/card-host.exe`：24项合成原生UI/文件检查通过。包括未准备就确认、准备不读正文/调用模型、显示来源、拒绝、账号变更、停用/重启清除同意，以及创建/更新/忽略/去重、超时、迟到、错误存储回归。模型与邮件响应为合成，不接私人凭据。

`python runtime/verify_task_observer_host.py --bundle git-repo/bundle --output runtime/verification/COMMITMENT-CONSENT-production --host runtime/host-repro/OctoSense-App-Hub/target/release/card-host.exe`：5项未修改生产包原生界面检查通过，缺少mail服务时诚实拒绝。初始截图已目视检查；该宿主不提供mail/model，所以不是实际服务连通验收。

结构化结果：[合成检查](cloud-consent-results.json)、[生产界面](cloud-consent-production-results.json)。本次不宣称真实邮箱/模型质量、OAuth或完整COMMITMENT-001完成。单来源真实业务验收和宿主凭据保护仍待完成。App Hub冻结v0.5.1未改变；本版未提交商店审核。
