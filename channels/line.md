# LINE 频道插件 (Messaging API)

**当前状态**：作为可选插件提供。支持私聊、群聊、媒体附件、位置信息及 Flex 消息。

## 插件安装
\`\`\`bash
openclaw plugins install @openclaw/line
\`\`\`

## 快速上手
1. 在 [LINE Developers](https://developers.line.biz/console/) 创建 Provider。
2. 开启 **Messaging API** 频道。
3. 获取 **Channel Access Token** 和 **Channel Secret**。
4. 启用 **Webhook** 并填入网关的 HTTPS 地址，后缀为 \`/line/webhook\`。

## 核心配置
```json
{
  "channels": {
    "line": {
      "enabled": true,
      "channelAccessToken": "你的TOKEN",
      "channelSecret": "你的SECRET",
      "dmPolicy": "pairing"
    }
  }
}
```

## 运行机制
- **私聊 (DM)**：默认使用配对模式（\`pairing\`），首次聊天需批准。
- **消息限制**：单条消息上限 5000 字符。
- **流式响应**：LINE 不支持原生流式输出，OpenClaw 会缓冲完整回复并在发送前显示“加载中”动画。

## 进阶功能 (Rich Messages)
- **Flex Cards**：支持发送自定义结构的卡片。
- **Quick Replies**：支持底部快速回复按钮。
