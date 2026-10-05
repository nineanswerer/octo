# 初赛0.5.3原生演示

[播放视频](initial-0.5.3.mp4) · [改期与历史截图](screenshots/initial-0.5.3-updated.png) · [模型失败截图](screenshots/initial-0.5.3-failure.png) · [生产包缺服务截图](screenshots/initial-0.5.3-production.png)

2026-10-05采集，约126.5秒，无音轨，带中文界面说明。连续采集Windows原生card-host实际画面，每秒2帧，编码H.264每秒12帧；重启瞬间保留最后画面。对应本仓库0.5.3应用源码，生产包SHA256和测试改动见[采集记录](../validation/initial-0.5.3-recording.json)，最终固定标签见[文件指纹](../release/INITIAL_0.5.3.json)。

## 看什么

1. 未修改生产包：默认停用、暂无事项。
2. 未修改生产包：独立card-host缺少mail服务，显示失败并停止，不伪造记录。
3. 合成测试包：先核验来源，再单独同意云分析；同意前没有正文/模型请求。
4. 合成邮件“今天晚上6点前交稿。”；预设create模型响应，记录事项与原文出处并保存读回。
5. 合成邮件“交稿改为明天中午。”；预设update响应，更新同一事项并保留旧期限历史。
6. 合成邮件“这次交稿取消。”；预设cancel响应，保留记录与历史，取消不代表完成。
7. 合成no_provider模型错误：停止观察，未处理消息不记入去重列表。
8. 关闭并重开：恢复已有事项，默认停用，需要重新同意。

## 证据边界

**后六段的邮箱和模型响应均为合成测试夹具，不是在线AI理解或私人邮箱实测。** 画面标题和副标题持续标明这一点。应用界面、状态处理、证据校验、实际JSON写入与读回、取消历史及重启是真实执行。8项采集时独立UI/文件检查通过；原有27项合成回归与5项未修改生产界面检查见[验证文档](../validation/COMMITMENT_CHANGES.md)。

测试包只改宿主请求适配、测试定时器和两个披露标签；业务处理源码来自0.5.3。测试包、夹具不加入正式bundle。未接私人邮箱、不调用在线模型、不使用开发MiniMax密钥，不产生模型费用。

真实邮箱授权与在线模型完整回环、语义质量仍待验收；本录像不能代替这些工作。正式运行需要带官方mail/model服务的完整宿主，[使用说明](../README.zh-CN.md)。独立渲染器仅展示界面和缺服务失败。

可复验采集脚本在tools/repro/；在本仓库内按[宿主构建记录](../validation/BUILD_HOST.md)准备runtime/host-repro对应的四个官方源码目录并构建hub/card-host，然后运行：

```powershell
python tools/repro/record_commitment_demo.py --bundle bundle --output runtime/initial-053-repro --host runtime/host-repro/OctoSense-App-Hub/target/release/card-host.exe
```

输出目录必须是新的隔离目录；不要覆盖已有用户数据。脚本仅使用Python标准库并生成PNG帧及检查结果。用FFmpeg按2帧/秒输入编码即可生成视频。旧0.4.1及更早录像仅为历史。
