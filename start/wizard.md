# 配置向导 (Onboarding Wizard)

向导是设置 OpenClaw 的推荐方式。它会引导你完成本地网关或远程连接、频道（如钉钉、微信）、技能以及工作空间的初始化。

## 启动命令
```bash
openclaw onboard
```

## 向导主要步骤
1. **模型与认证**：配置你的 AI 模型（如 Anthropic, OpenAI, Gemini 或 OpenCode）。
2. **工作空间**：选择 Agent 的家目录并生成引导文件（如 `SOUL.md`）。
3. **网关设置**：配置端口（默认 18789）、绑定地址及安全 Token。
4. **通讯频道**：配置 Telegram, WhatsApp, Discord 等插件。
5. **守护进程**：在 Linux 上安装 systemd 服务，或在 macOS 上安装 LaunchAgent，确保系统重启后自动运行。

## 常见模式
- **QuickStart (快速模式)**：保持默认设置，最快完成配置。
- **Advanced (高级模式)**：逐项手动控制所有参数。

## 重新配置
如果你想修改现有的设置，可以使用：
```bash
openclaw configure
```

## 多 Agent 管理
如果你需要添加具有独立工作空间和会话的第二个 Agent：
```bash
openclaw agents add <名字>
```
