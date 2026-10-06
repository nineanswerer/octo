# 宿主与启动

应用入口为bundle/main.splash，不是独立exe。仅验证Windows。

## 独立渲染器

原录像使用官方[App Hub 0f332112](https://github.com/OctoSense-org/OctoSense-App-Hub/tree/0f332112f0b5a379c5bb33790df74b21597190cf)的card-host。构建包名为octosense-card-host和octosense-app-hub，使用固定依赖工作区。设置OCTO_CARD_HOST指向产物后运行octocard.bat。此入口没有mail/model服务，不能完成正常邮箱业务。[合成测试复现](../demo/INITIAL_0.5.3.md)。

## 完整OctoSense

本机完整宿主固定官方[cf853501](https://github.com/OctoSense-org/OctoSense-Desktop/tree/cf85350129830605d08973befdd8bde6480f6a77)，使用Rust1.95与官方锁定依赖；应用运行不需要WSL或开发代理。

本次在准备好官方工作区后执行的命令：

```powershell
python tools/setup.py --check --cargo
cargo +1.95.0 build --locked --offline --release -p octosense
```

本机构建成功，不是全新机器安装验证。Windows邮箱凭据修复在独立宿主分支，未作为官方更新发布；不能推断上游已提供此修复。完整业务验收与便捷启动仍在准备。仓库不附带宿主二进制、个人配置、签名私钥或凭据。

在宿主通过App Hub安装应用；在AI providers配置本人模型，在宿主邮箱面板授权账户，再在应用核验来源及同意云分析。没有默认公共账号或免费模型。真实业务验收记录尚待补齐；源码构建、缺服务状态与合成演示不能替代它。
