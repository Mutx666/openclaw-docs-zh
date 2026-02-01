# Signal 频道插件 (signal-cli)

**当前状态**：通过外部 CLI 集成实现。网关通过 HTTP JSON-RPC 和 SSE 与 \`signal-cli\` 通信。

## 快速上手
1. 准备一个专门用于机器人的 Signal 号码（推荐）。
2. 安装 \`signal-cli\`（需要 Java 环境）。
3. 配对设备：\`signal-cli link -n "OpenClaw"\`，然后使用手机 Signal 扫码。
4. 配置 OpenClaw 配置文件。

## 核心配置
```json
{
  "channels": {
    "signal": {
      "enabled": true,
      "account": "+8613800000000",
      "cliPath": "signal-cli",
      "dmPolicy": "pairing"
    }
  }
}
```

## 号码模型 (重要)
- **回环保护**：如果你将机器人运行在你的个人 Signal 号码上，它将忽略你发给它（发给自己）的消息。
- **推荐方案**：为了实现“我发消息，机器人回复”，请使用独立的机器人号码。

## 运行机制
- **SSE 监听**：网关以守护进程模式运行 \`signal-cli\`，通过 SSE 实时读取事件。
- **媒体支持**：支持 base64 格式的附件下载，默认上限 8 MB。
- **已读与输入**：支持发送“正在输入”状态和已读回执。

## 常见操作
- **表情回应**：支持通过 \`message\` 工具执行 \`react\` 动作。
- **交付目标**：在 CLI 中发送消息时，目标格式为 \`signal:+86... \` 或 \`uuid:...\`。
