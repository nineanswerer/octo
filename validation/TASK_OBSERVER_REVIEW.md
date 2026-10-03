# 0.5.0 应用包人工自审

本记录为Codex外环源码审查，不是组织者或App Hub维护者接受证明。hub scan已生成7题，未调用外部reviewer。

1. 源码poll使用mail.accounts/sync/list/message，analyze调用model.complete，persist写入并逐字读回；列表描述注明真实回环待授权。未声称全系统或后台持续监视。
2. productivity类别适合事项记录，只有Windows实测。跨平台未验收。
3. storage用于observer-state.json；mail用于宿主授权账户及收件读取；model用于结构化语义判断。无network.hosts、无自行联网、无新宿主服务。mail上游权限包含发送，当前代码无发送调用，隐私文档明确说明。
4. 界面不模仿登录页，不收集密码或API密钥，认证由mail.add_account宿主页处理。
5. task中包含对模型的受限任务说明，邮件本身被标为不可信输入，不能扩大权限；响应只形成本地记录，不调工具。不是隐藏的系统指令或外部操作授权。
6. 没有针对私人个体的攻击或侮辱文字。测试使用合成地址和内容。
7. 路由建议human-review：预检通过，16项合成控制检查、5项未改代码渲染器检查、完整宿主无授权账户场景已通过；真实邮箱与模型效果、同版本录像及正式接收尚待完成，不能自行标为比赛通过。
