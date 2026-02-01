# Zalo 个人号插件 (非官方)

**当前状态**：实验性阶段。通过 \`zca-cli\` 自动化操控个人 Zalo 账号。

**风险警告**：这是非官方集成，存在封号风险。请自行承担使用风险。

## 必备条件
- 网关机器必须安装并配置好 \`zca-cli\` 命令行工具。
- 确保 \`zca\` 命令在系统环境变量 PATH 中。

## 快速上手
1. 安装插件：\`openclaw plugins install @openclaw/zalouser\`。
2. 运行登录命令扫描 QR 码：\`openclaw channels login --channel zalouser\`。
3. 在 \`openclaw.json\` 中启用频道。
4. 启动网关。

## 核心配置
```json
{
  "channels": {
    "zalouser": {
      "enabled": true,
      "dmPolicy": "pairing"
    }
  }
}
```

## 运行机制
- **技术原理**：后台运行 \`zca listen\` 接收消息，使用 \`zca msg\` 发送回复。
- **ID 发现**：可以使用 \`openclaw directory\` 系列命令来发现联系人和群组的 ID。
- **限制**：文本长度上限约为 2000 字符。

## 常见问题
- **zca 未找到**：请确认 \`zca --version\` 能够正确输出。
- **登录状态丢失**：尝试运行 \`openclaw channels logout --channel zalouser\` 后重新扫码。
