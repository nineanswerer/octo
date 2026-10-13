# 合成复现夹具，固定0.5.6核心

这里是受控测试源码，不是待安装的产品包。完整原函数区域与v0.5.6逐字一致（CRLF规范化），仅添加合成host.request队列、合成数据及诊断UI；manifest只授予storage，无真实邮件/模型服务。使用本机构建的App Hub原生card-host，保留runner摘要于结果JSON；不是未修改官方RC6整应用复现。

在单独测试profile中执行，不复制生产登录配置。可用已有原生card-host运行：

```powershell
card-host.exe --bundle validation/controlled-0.5.6/lifecycle --app-data controlled-test-data --allow-unsigned --remote 11595
```

点击“Run pure helper checks”，等待47秒，查看results_label全部true和status_label超时停用。探针使用真正30/45秒计时器；不会等待外部服务。请求与结果时间线见[lifecycle JSON](../lifecycle-fixed-0.5.6.json)。

保存失败夹具需先在同一个独立测试数据目录中创建目录`controlled-test-data/no-reminder-lifecycle-savefailure-test/observer-state.json`（不要在生产应用目录创建）。再以`--bundle validation/controlled-0.5.6/savefailure`和相同`--app-data`运行，点击测试按钮；六个结果应true，status_label说明保存失败、未报告成功。文件名与目录冲突触发真实fs.write错误，内存初值全为合成记录。

两个夹具使用不同测试app id，仅在其专用jail内写文件。不要将两份manifest当作产品manifest；不下载或替换官方宿主，不开启真实mail/model，不自动安装本应用。没有原生开发runner时可查看源码与JSON，不能称已运行复现。
