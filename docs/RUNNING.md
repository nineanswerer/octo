# 宿主、安装与无模型查看

应用入口bundle/main.splash，不是独立exe。仅验证Windows。本次使用[官方OctoSense desktop-v0.1.0-rc.2](https://github.com/OctoSense-org/OctoSense/releases/tag/desktop-v0.1.0-rc.2)，宿主提交4ccf8e068399b1da139771a9ed94cef05fa6ae60；没有使用历史0.5.4自编译补丁。

以上为RC2真实五封验收和本轮录屏的宿主范围。RC6下载与摘要核验不等于运行通过，RC6兼容性由Release中的独立报告说明。[0.5.6复现补充](https://github.com/nineanswerer/octo/releases/download/v0.5.6/REPRODUCING_0.5.6.md)为追加资料，不修改固定标签及封存包。

1. 从官方宿主Release安装对应Windows版本，核对官方资产摘要。
2. 从[本应用Release](https://github.com/nineanswerer/octo/releases)取得固定版app.bundle.pack.json，经兼容GitHub证明的App Hub安装。当前应用尚待官方 Hub 准入，默认商店不保证能搜索到。已验安装使用本机开发签名目录，步骤见官方 [提交指南](https://github.com/OctoSense-org/OctoSense-App-Hub/blob/main/docs/SUBMITTING.zh-CN.md)。审核下载包应先 publisher-unpack 到新审查目录，再 publisher-verify --catalog 指向经过 catalog-verify 的官方 catalog-v2.json；源码目录不等于封存包。
3. 在宿主AI Providers配置本人产品模型和额度，本次核实MiniMax中国区MiniMax-M3、无fallback。编程Plan不能代替产品API额度。
4. 宿主邮箱页面连接一个本人测试邮箱，填写对应服务器/端口/TLS/授权码；默认服务器不会自动匹配地址。
5. 应用核验来源后再单独同意云分析。[五封步骤](REAL_MAIL_ACCEPTANCE.md)。

网易126本次可行路径：邮箱设置开启POP3/SMTP，并在宿主登录表单明确选择 **“POP3: inbox only”**；POP3 pop.126.com:995/TLS，SMTP smtp.126.com:465/TLS，用户名完整地址、本人授权码。只改服务器和端口、仍保留IMAP协议，不能得到POP3路径。原RC2官方邮件服务自带POP3，未使用本地邮件兼容适配器。

真实回环保留原授权账号，仅临时切换传输配置，结束后恢复原IMAP；本轮未重新验证登录表单切换过程。原RC2 IMAP缺网易要求的客户端ID，读INBOX可能Unsafe Login并停用；连接成功不代表收信通过。其他供应商或OAuth未作本轮验证。

## 无模型查看

官方App Hub工作区card-host没有完整mail/model服务，只能查看本地UI/存储。Windows设置OCTO_CARD_HOST为既有card-host.exe完整路径，运行octocard.bat。或按其--help指定--bundle及独立--app-data目录。

空目录显示空状态。可将[公开合成预览记录](../demo/preview-state.json)复制到独立测试目录no-reminder-agent/observer-state.json，勿覆盖真实记录。这个路径不读邮箱或分析新邮件，不等于完整宿主验收。

本机复用安装通过，不是全新机器安装。正式包安装状态见[提交记录](../SUBMISSION_NOTES.md)。仓库不附带宿主二进制或个人配置。

请从固定Release下载0.5.6封存包。旧日期目录中的ZIP已从当前默认分支移出；旧标签及历史验证报告只供追溯，不能作为本轮安装或主媒体。
