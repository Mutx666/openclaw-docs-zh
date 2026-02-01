# gateway 命令 (网关控制)

`gateway` 是 OpenClaw 的核心 WebSocket 服务。该系列子命令用于运行、管理和探测网关。

## 运行网关
- **本地运行**：`openclaw gateway`
- **后台常驻运行**：`openclaw gateway run`
- **开发模式**：`openclaw gateway --dev` (自动生成临时配置和工作空间)

## 查询与探测
- **状态概览**：`openclaw gateway status` (显示服务运行状态和端口占用)
- **多网关探测**：`openclaw gateway probe` (扫描本地和远程可连接的所有网关)
- **健康检查**：`openclaw gateway health`
- **远程 SSH 连接**：`openclaw gateway probe --ssh user@host` (类似 macOS 应用的 SSH 隧道模式)

## 服务生命周期管理
这些命令用于安装或管理系统级的守护进程（LaunchAgent 或 Systemd）：
- **安装服务**：`openclaw gateway install`
- **启动服务**：`openclaw gateway start`
- **停止服务**：`openclaw gateway stop`
- **重启服务**：`openclaw gateway restart`
- **卸载服务**：`openclaw gateway uninstall`

## 常见参数
- `--port`：修改监听端口（默认 18789）。
- `--bind`：绑定地址模式（loopback / lan / custom）。
- `--token`：设置或覆盖网关安全 Token。
- `--json`：输出机器可读的 JSON 格式（适合脚本调用）。
