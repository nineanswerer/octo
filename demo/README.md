# 历史规则版操作录像

旧`mail-workflow.mp4`对应a39c1a9，保留作历史，不用于本次初赛提交。

## 初赛0.4.1实录

[initial-0.4.1.mp4](initial-0.4.1.mp4)：122.5秒，H.264，618×1338，无音轨。2026-10-03重新录制生产0.4.1代码，应用源码对应87a6066；文件指纹及冻结tag见../release/INITIAL_FREEZE.json。

本次12项原生UI及实际文件检查全部通过：[结果](../validation/INITIAL_DELIVERY_RESULT.json)。两张同版本关键截图：[保存核验](screenshots/initial-saved.png)、[保存失败](screenshots/initial-failure.png)。

本次和历史视频均展示本地规则，不包含模型回复或实时AI生成。以下采集方法和流程同样用于新录像。正式报送和赛事接收回执未完成。

视频连续采集实际 Windows card-host 画面，采样 2 帧/秒、编码为 12 帧/秒；等待期间画面保持，宿主重启期间保留最后捕获画面。不是在线模型录像；应用明确使用本地关键词规则。

操作顺序：空状态 → 空输入 → 无关记录不行动 → 未完成邮件整理 → 修改来源后阻止保存 → 编辑草稿后保存并读回 → 重复保存 → 关闭并重启恢复 → 取消后阻止覆盖 → 清除 → 写入失败提示 → 恢复状态不一致时阻止保存。每项展示约 10 秒。录制时逐项检验界面与实际文件，结果见 `../validation/demo-results.json`。

写入失败由测试在隔离数据目录创建同名空目录触发，不涉及真实用户文件。应用不会发送邮件。

正常截图为 `../bundle/screenshots/01-main.png`；失败截图为 `../bundle/screenshots/02-save-failure.png`。原始逐帧记录保存在开发工作区，不属于应用运行素材。
