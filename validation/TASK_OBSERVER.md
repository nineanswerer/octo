# 授权邮箱事项观察 0.5.0 — 验证记录

核心流程：用户连接邮箱并显式启用 → 官方 mail 服务读取单一授权邮箱最近5封 → 官方 model.complete 判断个人事项 → 核对原文证据与截止时间原文 → 保存 observer-state.json 并逐字读回 → 后续邮件更新已有事项、同一邮件不重复分析。

没有固定关键词分类器、预置生产回复、Python 运行时组件、新增原生服务、邮件发送或通知。应用打开时每30秒检查，一次分析一封；重启默认停用。最近5封之外可能遗漏，不能宣称完整邮箱覆盖或系统级后台观察。历史和去重各100条，达上限停止；相对时间保留原文及邮件日期，不转换为确定绝对日期。

## 实际执行的验证

- 真实 Windows card-host 渲染未修改候选代码：5项检查通过，覆盖默认停用、服务缺失、停用及不生成虚假记录。[结果](TASK_OBSERVER_HOST_RESULT.json)。该渲染器没有 mail/model 服务，不能运行完整回环。
- 同一原生渲染器中，仅测试副本替换宿主传输并缩短轮询/超时：16项通过，覆盖创建、更新、无关内容、去重、伪造证据/时间拒绝、模型错误不重试、停用及超时迟到结果、无/多邮箱、重启、保存失败和损坏文件保留。[结果](TASK_OBSERVER_SYNTHETIC_RESULT.json)。
- [合成响应下的记录界面](OBSERVER_SYNTHETIC_RECORD.png)是真实原生界面截图，事项来自合成响应，不证明模型实际理解。
- 官方完整 OctoSense 宿主通过本地测试签名商店安装0.5.0，实际调用mail.accounts返回“没有已授权邮箱”，可见正确停用状态：[结果](TASK_OBSERVER_FULL_HOST_RESULT.json)。说明邮箱服务已接通，不表示已有邮箱或已调用模型。复用了先前本人授权生成的本地测试密钥，没有新建密钥或公开上传。
- 在全新、没有提供商配置的官方完整宿主中，仅将测试副本的邮箱读取替换为合成输入，保留真实model.complete调用：宿主返回no_provider，应用停止、没有保存事项、没有自动重试。[结果](TASK_OBSERVER_MODEL_CONTRACT_RESULT.json)。官方complete/mod.rs先执行request.check及Schema::compile，再检查提供商，因此该结果验证请求格式与schema被接受；没有调用任何模型提供商，不能证明识别质量。

外环命令（开发工作区，测试脚本不作为运行依赖）：

```powershell
python runtime/verify_task_observer_ui.py --bundle runtime/verification/AI-TASK-OBSERVER-001/bundle --output runtime/verification/AI-TASK-OBSERVER-001/ui6 --host runtime/host-repro/OctoSense-App-Hub/target/release/card-host.exe
python runtime/verify_task_observer_host.py --bundle runtime/verification/AI-TASK-OBSERVER-001/bundle --output runtime/verification/AI-TASK-OBSERVER-001/host --host runtime/host-repro/OctoSense-App-Hub/target/release/card-host.exe
```

宿主构建指纹沿用[锁定构建记录](host-build.json)。开发内环任务 MCP-b4ace100-1823-487d-b674-6ca1e4b9a379，派单前Plan剩余95%/49%；第一版因不存在的API和错误去重被拒绝，外环修正后独立复验。没有调用普通API或挪用开发密钥作为应用模型。

## 尚未验收

真实邮箱授权、实际模型识别质量以及两者连通后的完整回环。用户已确认先使用邮箱，实现后本人授权。不能把上述合成16项称为真实AI或初赛通过。新的同版本演示与最终冻结须在真实回环验证后准备；0.4.1录像仍只代表旧草稿原型。

本机已安装候选可在项目根运行 `powershell -NoProfile -File runtime/start_task_observer.ps1`；模型配置运行同脚本加 `-AISetup`。这是本开发工作区已准备的完整宿主入口，不随应用包分发，其他机器须按官方流程安装宿主及加载应用。关闭配置窗口后再启动应用，密码和模型认证仅在宿主页面输入，不发送到聊天或仓库。
