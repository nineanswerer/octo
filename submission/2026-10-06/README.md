# 南下 · 作品材料集中入口

**一句话：从授权邮件主动识别与你有关的承诺、截止时间、改期和取消，保留原文证据，不催促你。**

例子：邮件说“今天晚上6点前交稿”，记录交稿事项；随后“改成明天中午”，更新同一事项；再说“取消”，保留记录并标记取消，不能当作完成。

[中文讲解视频（约2分6秒）](video/octo-demo-zh.mp4) · [字幕](video/narration.srt) · [应用包下载](bundle/no-reminder-agent-0.5.3.zip) · [文件校验和](SHA256SUMS) · [验证边界](VERIFICATION.md)

这是2026年10月6日整理的补充材料，不改变初赛固定标签，也不表示赛事已接受补交。应用脚本来自 `5960702f933c63d5e53f24c80ddf7e78e16a34cc` 的0.5.3版本；本轮精简旧素材并重新stamp，包摘要与冻结标签不同，脚本未改。App Hub #74仍固定0.5.1、待审核；没有擅自更新该提交。

## 看什么

| 视频时间 | 场景与截图 | 证明范围 |
| --- | --- | --- |
| 00:00 | [生产启动](screenshots/01-production-empty.png) | 默认停用、空状态 |
| 00:15 | [缺少服务](screenshots/02-production-missing-service.png) | 未修改生产包缺mail时明确停止 |
| 00:31.5 | [单独同意分析](screenshots/03-synthetic-consent.png) | 合成来源，明确用途与云分析确认 |
| 00:47 | [创建事项](screenshots/04-synthetic-created.png) | 合成邮件与预设create响应，保存读回 |
| 01:03 | [改期](screenshots/05-synthetic-updated.png) | 同一事项更新、保留历史 |
| 01:19.5 | [取消](screenshots/06-synthetic-cancelled.png) | 取消不代表完成 |
| 01:35.5 | [模型失败](screenshots/07-synthetic-model-failure.png) | 停止观察，不错误去重 |
| 01:51 | [重启](screenshots/08-synthetic-restart.png) | 恢复记录、默认停用 |

前两段是未修改生产包；后六段是明确标注的合成邮件、预设模型响应。全部画面来自10月5日实际原生界面录像，本轮仅增加本机离线中文讲解和字幕，没有重新录制或证明在线模型理解。

## 如何复现

1. 解压应用包，得到 `no-reminder-agent/manifest.json` 和 `main.splash`。它是OctoScript应用，不是独立Windows可执行文件。
2. 按[中文使用说明](../../README.zh-CN.md)配置带官方mail/model服务的完整OctoSense宿主，再加载应用。仓库不附宿主、邮箱凭据或模型密钥。
3. 生产运行先授权邮箱、核验来源，再同意云分析；仅应用打开期间每30秒检查最近5封邮件。缺服务不会伪造成功。
4. 合成录像复现命令与夹具差异见[原采集说明](../../demo/INITIAL_0.5.3.md)。独立card-host只有界面渲染，不能接通邮箱与模型。

真实邮箱和在线AI完整回环仍待验收；不扫描其他应用，不发送邮件、不弹提醒。仅验证Windows，不宣称其他平台已验证。权限与数据说明见[隐私政策](../../PRIVACY.md)。


### 0.5.4 后续修复与真实验收

[当前0.5.4应用包](bundle/no-reminder-agent-0.5.4.zip) · [真实邮件验收](../../validation/REAL_MAIL_0.5.4.md)。0.5.4完成受控真实QQ邮件与在线模型回环；上述0.5.3视频与包保留原始版本及合成说明，不更改初赛冻结标签。
