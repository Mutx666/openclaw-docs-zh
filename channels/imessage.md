# iMessage 频道插件 (imsg)

**当前状态**：通过外部 CLI 集成 (\`imsg\`) 实现。网关通过 stdio 与 \`imsg rpc\` 通信。

## 必备条件
- **macOS** 系统且已登录 iMessage。
- 安装 \`imsg\` 工具：\`brew install steipete/tap/imsg\`。
- 赋予 OpenClaw 和 imsg **完全磁盘访问权限 (Full Disk Access)**（用于访问消息数据库）。

## 快速上手
1. 确保 Mac 上的“信息”应用正常工作。
2. 配置 OpenClaw 指向 \`imsg\` 路径和数据库路径。
3. 启动网关并允许 macOS 弹出的一切自动化和磁盘访问请求。

## 核心配置
```json
{
  "channels": {
    "imessage": {
      "enabled": true,
      "cliPath": "/usr/local/bin/imsg",
      "dbPath": "/Users/你的用户名/Library/Messages/chat.db"
    }
  }
}
```

## 隔离运行 (进阶)
如果你想让机器人使用独立的 Apple ID 发消息：
1. 在 Mac 上创建一个专门的 macOS 用户并登录机器人的 Apple ID。
2. 开启该用户的“远程登录 (SSH)”。
3. 在主用户下使用 SSH 封装脚本调用该用户的 \`imsg\`。

## 运行机制
- **本地数据库轮询**：网关通过读取 \`chat.db\` 获取新消息。
- **发送权限**：首次发送消息时，macOS 会提示“是否允许控制信息应用”，必须点击允许。
- **提及触发**：由于 iMessage 原生不支持“提及”元数据，需在 \`mentionPatterns\` 中配置正则（如 "@小爱"）。

## 交付目标 (CLI)
建议使用 \`chat_id:数字\` 来确保消息发送到正确的对话。
