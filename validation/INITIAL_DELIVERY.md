# 初赛交付独立验证 — 2026-10-03

生产应用0.4.1源码对应87a6066，未修改main.splash、manifest或listing。材料冻结tag为v0.4.1-initial；确切包文件、录像及宿主SHA256见[冻结记录](../release/INITIAL_FREEZE.json)。

外环实际执行，在Octo工作区：

```powershell
python runtime/record_mail_demo.py --bundle git-repo/bundle --output runtime/verification/INITIAL-DELIVERY-001/demo
```

开发录制脚本位于外层工作区；应用使用README中的octocard.bat，不需要脚本或WSL。启动器默认改为本次验证的runtime/host-repro/OctoSense-App-Hub/target/release/card-host.exe，显式OCTO_CARD_HOST仍优先。

原生渲染器源码OctoSense-org/OctoSense-App-Hub，提交0f332112f0b5a379c5bb33790df74b21597190cf。锁定依赖构建命令为cargo build --release --locked -p octosense-card-host -p octosense-app-hub；已执行的环境和指纹见[构建记录](host-build.json)。宿主不随应用包分发；新机器必须取得匹配构建，不能只复制应用便宣称复现环境完整。只验证Windows。

本次12项原生UI/文件检查通过：[结果](INITIAL_DELIVERY_RESULT.json)。ffprobe实测录像122.5秒/H.264/618×1338；保存及失败截图已独立查看。只关闭本次自有子进程。录制输入和失败构造均在隔离目录，不涉及私人邮件。

最终包hub check --allow-unsigned通过：[输出](../release/hub-check.txt)。hub scan只生成7题材料，无外部reviewer，不宣称自动审核通过：[审查包](../release/review.json)、[人工回答](../release/REVIEW_ANSWERS.md)。没有增加功能、权限、密钥或模型调用。

MiniMax Plan在官方锁内接受INITIAL-DELIVERY-001，回执MCP-ad5199de-a6c5-4db4-b0a5-c02af8e5f00e，实时额度96%/49%；只写ACK未完成四份文档。外环拒绝完成声明，独立整理并复验。开发双环不属于作品运行时功能。

限制：录像是本地规则，非已验收实时AI。外部邮箱、后台观察、发送、时机学习和Rinx未实现。正式提交入口和接收回执待确认，不宣称完整Agent自动化或比赛验收通过。
