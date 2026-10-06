# 官方运行时AI配置

完整OctoSense宿主提供model.complete，独立card-host没有模型服务。官方接口入口见[AI-SERVICES](https://github.com/OctoSense-org/OctoScript-App-Design-Flow/blob/main/docs/AI-SERVICES.md)。官方接口不是无需配置的公共免费模型。

在宿主AI providers打开Add model，选择提供商、模型、端点并在宿主自己的输入框配置凭据，测试连接后保存。应用只请求宿主model服务，不接收模型密钥。不要把密钥写入应用包、截图、聊天或仓库。

应用请求使用task/input/schema/class，回调读取data.output并校验字段与原文证据。自动观察只在单独同意云分析后开始；失败停止，不伪造事项。本人配置的提供商会收到邮件内容及相关上下文，数据与费用规则见[隐私](../PRIVACY.md)。

先用仅含测试内容的邮箱。真实验收须核对创建、改期、无关事项忽略、取消、保存读回和重启状态，[验收步骤](REAL_MAIL_ACCEPTANCE.md)。当前完整业务仍未验收，不用合成夹具替代。

[宿主版本与启动](RUNNING.md) · [中文说明](../README.zh-CN.md)。
