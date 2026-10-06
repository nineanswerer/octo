# 0.5.3 取消与变更历史

2026-10-04。新增cancel模型动作、active/cancelled事项状态及最多20条非递归变更前快照。更新和取消保留旧标题、期限、原文证据及出处；取消保留原事项编号/标题/期限，当前证据与出处改为取消消息。取消不等于完成；update/cancel不得修改已取消事项；历史达到上限停止，不清空或标为已处理。旧记录缺少status/history可恢复，损坏新字段拒绝并保留文件。

独立Windows原生UI与实际文件结果核验通过；合成数据不证明在线模型理解。

命令：`python runtime/verify_commitment_changes_ui.py --bundle runtime/worktrees/commitment-changes/bundle --output runtime/verification/COMMITMENT-CHANGES-008 --host runtime/host-repro/OctoSense-App-Hub/target/release/card-host.exe`。27项合成原生UI/文件检查通过，包含创建、改期历史、取消、历史上限、不可恢复取消、重启、旧记录迁移、异常字段保留及原有去重/证据/超时/失败回归。邮件和模型响应均为合成，不是模型语义质量证明。

未修改生产包另通过5项原生界面检查：`python runtime/verify_task_observer_host.py --bundle git-repo/bundle --output runtime/verification/COMMITMENT-CHANGES-production --host runtime/host-repro/OctoSense-App-Hub/target/release/card-host.exe`。card-host不提供mail/model，不能据此宣称真实回环通过。

结果：[合成原生](commitment-changes-results.json)、[生产包](commitment-changes-production-results.json)。已验证的行为与尚未完成的工作分开：补充要求独立字段、不同承诺的可靠语义关联、乱序消息控制、用户纠正/忽略、真实邮箱和模型质量仍待完成。新create是否错误复活旧承诺目前依赖模型提示，不声称有确定性语义拦截。App Hub #74固定v0.5.1不变，本版仅本地及用户仓库开发。
