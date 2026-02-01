# Telegram 频道插件 (Telegram Bot API)

**当前状态**：生产环境就绪，支持私聊和群组机器人。

## 快速上手
1. 在 Telegram 中私聊 [@BotFather](https://t.me/botfather) 创建新机器人。
2. 获取 Bot Token。
3. 配置 OpenClaw：
   - 环境变量：`TELEGRAM_BOT_TOKEN=...`
   - 或配置文件：`channels.telegram.botToken: "..."`
4. 启动网关，首次私聊进行配对认证。

## 核心功能
- **流式草稿 (Draft Streaming)**：在 Agent 思考时，Telegram 会显示“正在输入”或流式显示草稿内容（需开启私聊话题模式）。
- **HTML 格式化**：输出内容自动转换为 Telegram 支持的 HTML 子集。
- **原生命令**：自动将 `/status`, `/reset` 等命令注册到机器人的菜单栏。

## 群组访问控制
- **隐私模式**：如果机器人不是管理员，可能无法看到所有消息。建议关闭 Privacy Mode 或设为管理员。
- **提及响应**：默认仅响应 @机器人 的消息。

## 交付目标
在定时任务或消息发送工具中，可以直接使用用户 ID 或 `@用户名` 作为目标。
