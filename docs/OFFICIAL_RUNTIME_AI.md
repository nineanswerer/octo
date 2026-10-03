# 官方运行时 AI 配置说明

本文档说明如何在 OctoSense 完整宿主中配置 AI 提供商以启用模型服务。

## 核心概念区分

| 场景 | 实际状态 |
| --- | --- |
| 仅渲染型 card-host | 无 AI 服务；应用只能使用本地关键词规则 |
| 本项目已验证的完整 OctoSense 宿主 | 提供 App Hub 与 AI providers 系统应用；仍需配置模型 |
| 已配置 AI 提供商 | `model.complete` 调用实际路由到所选服务商 |

## model.complete 实现位置

官方源码：`apps/ai-providers/host-service/src/complete`

应用调用方式：

OctoScript 调用为 `host.request("model.complete", {task, input, schema, class}, callback)`。
`schema` 必须是受支持的 JSON Schema 对象，`class` 为 `fast` 或 `strong`。
回调读取 `r.data.output` 与 `r.data.meta`；不能把此处的简写当作可执行脚本。

宿主根据用户个人配置（`profiles/_main.json` 中 `config.llm.primary` 和 `config.llm.fallbacks`）选择服务商；应用不暴露凭证或服务商 ID。

## 官方 AI 提供商系统

`os.ai-providers` 系统应用负责配置：

- **family** — 提供商家族（OpenAI 兼容、MiniMax 等）
- **model** — 具体模型 ID
- **route** — API 端点
- **auth** — 认证信息
- **test** — 连接测试
- **save** — 保存配置

支持提供商二维码导入。

## 实际配置步骤

### 1. 安装完整宿主

使用含 `model` 服务和 AI providers 系统应用的完整宿主；单独 card-host 不能提供该服务。
现有入口见 [README](../README.md)，其中 `octocard.bat` 仅是渲染入口，不是完整 AI 启动器。

### 2. 打开 AI 提供商设置

打开宿主的 **AI providers** 系统应用。本项目完整宿主的隔离原生界面已实测显示
**Add model**、**No models yet** 和 **Import code from image**。
该结果只说明测试配置为空，不代表个人其他宿主配置也为空。

### 3. 添加或导入提供商

- 手动填写 family、model、route、auth
- 或使用 QR 码导入已有配置

### 4. 测试连接

使用宿主提供的测试功能验证配置。

### 5. 保存配置

保存后宿主会使用该配置进行 `model.complete` 调用。

### 6. 重启（如有需要）

某些配置变更需要重启宿主使生效。

### 7. 验证应用调用

0.5.0邮箱观察版：先在应用中连接邮箱，再点击“启用观察与 AI 分析”；新邮件会自动交给宿主模型判断，查看事项、原文证据及保存结果。旧0.4.1草稿版才使用“AI 理解并准备草稿”按钮。

## 实际观察与限制

- 宿主的 `model.complete` 调用返回 `no_provider` 表示未配置提供商
- 本地 deepseek-r1:7b 测试可验证调用路径，但不等于官方模型质量验收
- 已核对的公开活动资料提到 MiniMax API / Kimi 开发福利；尚未找到无需账号配置的公共运行时端点。这不排除组织者另外发放配置。
- 模型质量（如原文事实保留、具体步骤建议）需单独验证
- 不要将开发密钥复制到宿主或直接应用 API

## 诊断工具

检查当前配置状态：

```bash
python tools/check_runtime_ai.py --core-dir <OCTOS_APP_CORE_DIR>
```

输出 JSON 格式状态，见工具说明。
`CONFIGURED_UNTESTED` 只证明配置有有效的 primary 字段，不证明认证、网络或生成成功。
缺少 primary 时工具报告 `NO_PRIMARY`；即使存在 fallback 也不表示宿主必然不能调用。

没有模型账号时，需要另行授权的运行时凭证或组织者提供的宿主配置；不能自动挪用开发密钥。
认证在宿主自己的 sheet 中输入，不要发到聊天或提交仓库。
实际验收还包括编辑草稿、用户确认保存、读回核验，以及真实模型用量；看到生成文字不足以通过。
Codex/MiniMax 内外环只用于开发，不是应用必须交付的功能。

## 隐私说明

- 应用不读取模型密钥，不使用开发代理凭证
- AI 响应中的原文证据会逐字核对，但不保证所有事实正确
- 模型用量和费用由宿主配置决定，本应用不承诺免费

## 相关文档

- [隐私](../PRIVACY.md)
- [本地推理测试记录](../validation/AI_LIVE_LOCAL.md)
- [完整接口验证](../validation/AI_COMPLETE.md)
- [官方接口与 provider 路由](https://github.com/OctoSense-org/OctoSense/pull/95)
- [官方 AI providers 源码](https://github.com/OctoSense-org/OctoSense/tree/cf85350129830605d08973befdd8bde6480f6a77/apps/ai-providers)
- [课堂模型配置要求](https://github.com/gosimfoundation/hackathon-agenticapp26/blob/main/docs/courses/2026-09-26/demo-runbook.md)
