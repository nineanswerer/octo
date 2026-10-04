# 0.5.1 邮箱来源绑定验证

日期：2026-10-04，北京时间。此版本仍为纯 OctoScript 应用；不是网页邮箱登录完成证明。

## 改动与结果

首次明确启用时，核验唯一授权邮箱并保存账号、地址、INBOX；之后每次观察都重新核对账号。同步、列表和正文读取均传明确来源，拒绝返回其他文件夹。重启默认停用。旧 schema1 和缺失、损坏来源字段可以恢复历史事项，只有再次明确启用才保存 schema2；异常历史记录保留原文件。

MiniMax Plan 内环实现，Codex 外环审查及独立原生复验。最初18项基础测试通过后，新增迁移测试发现实际恢复失败；两次修复后完整29项检查通过。没有将内环 ACK 的完成声明直接当作验收。

原生 card-host 界面与存储检查使用合成邮箱和模型响应：[29项结果及源文件/宿主二进制 SHA-256](mail-source-results.json)。覆盖首次启用、明确服务参数、去重/更新/忽略、虚构证据拒绝、模型失败、超时、停止后迟到响应、空/多账号、重启、存储失败、历史迁移、缺失/损坏/空来源、非数组账号、错误文件夹、观察期间账号变化。真实邮箱、真实模型质量和 OAuth 登录没有在此测试中验证。

未修改的生产 bundle 另通过 [5项原生 card-host 检查](mail-source-native-host-results.json)：默认停用、无 mail 服务时明确停止、不生成假事项、停止状态可见、连接仍走宿主授权接口。card-host 本身不提供 mail/model 服务，此组不是完整宿主连通验收。实际界面截图已更新到 bundle/screenshots/09-observer-source.png。hub stamp 后 check --allow-unsigned 返回 PASSED；未签名仍有发布者签名警告，不等于商店发布或赛事通过。

本开发工作区实际运行的独立命令（辅助脚本不随应用包分发）：

```powershell
python runtime/verify_mail_source_ui.py --bundle runtime/worktrees/mail-consent/bundle --output runtime/verification/MAIL-SOURCE-005 --host runtime/host-repro/OctoSense-App-Hub/target/release/card-host.exe
python runtime/verify_task_observer_host.py --bundle git-repo/bundle --output runtime/verification/MAIL-SOURCE-005-production --host runtime/host-repro/OctoSense-App-Hub/target/release/card-host.exe
runtime/host-repro/OctoSense-App-Hub/target/release/hub.exe stamp git-repo/bundle
runtime/host-repro/OctoSense-App-Hub/target/release/hub.exe check git-repo/bundle --allow-unsigned
```

## 尚未完成

文件夹选择与正文预览、单独云分析授权、Windows 邮箱凭据加密验收、Gmail/Outlook OAuth。当前 INBOX 限定只约束本应用请求，不缩小供应商 token 权限。Windows 宿主凭据存储修复尚未通过验收，此前不接入私人邮箱凭据。实际初赛接收由赛事方决定。
