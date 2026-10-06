# 本轮检查与证据边界

- 包来源：master `5960702f933c63d5e53f24c80ddf7e78e16a34cc`；ZIP逐文件与该工作树bundle比较，字节完全一致。未删历史文件、未重新stamp、未改变冻结标签。
- 原生录像：10月5日采集的0.5.3录像；原有8项录像检查、27项合成回归和5项生产UI检查见[原验证](../../validation/COMMITMENT_CHANGES.md)与[采集回执](verification/recording.json)。本轮没有声称重新执行这些业务测试。
- 视频：保留原H.264画面，增加本机Microsoft Huihui离线中文语音；ffmpeg全片解码及ffprobe时长、音视频轨检查。机器结果见[media.json](verification/media.json)、[package.json](verification/package.json)。字幕是场景说明，不是假称真实邮箱测试。
- 截图：8张原采集PNG原样复制；前2张生产包，后6张合成夹具。未放入QQ邮箱地址、旧邮件、授权码、模型密钥或私人截图。
- 真实邮箱与在线模型：**未验收**；Windows邮箱凭据修复的宿主代码不属于这个纯OctoScript应用包，不能用宿主单元测试替代真实业务验收。
- 下载包不是正式商店签名发布，不代表App Hub批准或比赛通过；历史未列入listing的截图仍保留，避免改变包摘要。
- 听感尚需用户播放确认；自动媒体检查能证明文件可解码、有音轨，不能替代听感判断。
