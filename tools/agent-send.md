# agent 命令 (主动运行)

\`openclaw agent\` 允许你在不发送聊天消息的情况下，直接触发 Agent 运行一个特定任务。

## 运行行为
- **会话选择**：可以通过 \`--to\` 指定联系人 ID 来自动推导会话上下文，或通过 \`--session-id\` 直接进入指定会话。
- **输出模式**：默认直接在终端打印回复文本。添加 \`--json\` 参数可获取包含元数据的结构化数据。
- **消息交付**：添加 \`--deliver\` 参数，Agent 的运行结果会自动发送到对应的通讯频道（如钉钉或 WhatsApp）。

## 常用命令示例
- **基础运行**：
  \`openclaw agent --to +86138... --message "给我一个状态报告"\`
- **指定 Agent**：
  \`openclaw agent --agent ops --message "总结日志文件"\`
- **带交付的运行**：
  \`openclaw agent --to +86138... --message "生成日报" --deliver --channel dingtalk\`

## 核心参数
- \`--local\`：强制在本地运行模型（不经过网关，需在当前 Shell 中配置 API Key）。
- \`--thinking\`：设置模型的思考等级（仅支持部分模型）。
- \`--verbose\`：是否显示详细的工具执行日志。
