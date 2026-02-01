# onboard 命令 (新手引导)

交互式的新手配置向导，用于设置本地网关或连接远程网关。

## 常用命令示例
- **标准向导**：`openclaw onboard`
- **快速入门**：`openclaw onboard --flow quickstart` (最小化提示，自动生成 Token)
- **手动高级模式**：`openclaw onboard --flow manual` (开放所有参数配置)
- **连接远程网关**：`openclaw onboard --mode remote --remote-url ws://<主机地址>:18789`

## 流程说明
- **QuickStart**：最适合初学者，几秒钟内完成基础配置。
- **Manual**：允许自定义监听端口、绑定地址、安全认证及具体的通讯频道设置。
- **Dashboard**：配置完成后，运行 `openclaw dashboard` 即可在浏览器中开始第一次对话。
