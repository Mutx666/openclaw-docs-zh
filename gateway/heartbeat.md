# 心跳机制 (Heartbeat)

心跳机制是网关定期触发的 Agent 轮次。它让模型能够主动检查是否有需要处理的事项，而无需你主动发消息。

## 快速上手
- **默认间隔**：通常为 30 分钟。
- **清单文件**：在工作空间创建 \`HEARTBEAT.md\`，列出你希望 Agent 定期检查的任务。
- **通知目标**：默认会发送到你最后使用的频道（\`target: "last"\`）。

## 核心配置
```json
{
  "agents": {
    "defaults": {
      "heartbeat": {
        "every": "30m",
        "target": "last",
        "activeHours": { "start": "08:00", "end": "22:00" }
      }
    }
  }
}
```

## 响应规则 (Contract)
- **HEARTBEAT_OK**：如果 Agent 检查后发现没有重要事项，它必须回复 \`HEARTBEAT_OK\`。网关会拦截这个信号，不会向你发送冗余消息。
- **主动告警**：如果发现问题，Agent 直接返回描述文字，网关会将其推送到你的手机或电脑。

## HEARTBEAT.md 示例
```markdown
# 心跳检查清单
- 扫描收件箱是否有紧急邮件？
- 检查日历，提醒我 1 小时内的会议。
- 如果我已经 8 小时没说话了，发个简单的问候。
```

## 手动唤醒
你可以随时手动触发一次心跳检查：
\`openclaw system event --text "手动检查更新" --mode now\`

## 成本建议
心跳会消耗真实的 Token。建议保持 \`HEARTBEAT.md\` 尽量精简，并考虑为心跳任务指定一个更廉价的模型。
