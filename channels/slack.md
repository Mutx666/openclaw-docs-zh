# Slack 频道插件 (Socket Mode / HTTP Mode)

**推荐模式**：Socket Mode（无需公网 IP 即可运行）。

## 快速上手
1. 在 [Slack API](https://api.slack.com/apps) 创建 App。
2. 开启 **Socket Mode**。
3. 生成 **App Token** (`xapp-...`) 和 **Bot Token** (`xoxb-...`)。
4. 订阅事件：`message.*`, `app_mention`, `reaction_added` 等。
5. 配置 OpenClaw：
```json
{
  "channels": {
    "slack": {
      "enabled": true,
      "appToken": "xapp-...",
      "botToken": "xoxb-..."
    }
  }
}
```

## 核心特性
- **用户 Token 支持**：可以使用用户级别的 Token (`xoxp-...`) 来读取历史记录、搜索消息或获取成员信息。
- **线程回复**：支持通过 `replyToMode` 配置自动开启线程（Thread）回复，保持频道整洁。
- **交互组件**：支持 Slack 的斜杠命令 (Slash Commands)。

## 限制
- 文件上传上限默认 20 MB。
- 文本内容会自动按 4000 字符进行切片。
