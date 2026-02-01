# MiniMax 供应商配置

MiniMax (名灵) 推出了 M2/M2.1 系列模型，特别在多语言编程和移动端开发方面表现出色。

## 推荐方案：MiniMax OAuth (编程计划)
适用于订阅了 MiniMax 编程计划的用户，无需 API Key。

### 设置方式 (CLI)
\`\`\`bash
# 启用插件
openclaw plugins enable minimax-portal-auth
openclaw gateway restart
# 启动向导
openclaw onboard --auth-choice minimax-portal
\`\`\`
向导会提示你选择节点：
- **Global**: 国际用户 (api.minimax.io)
- **CN**: 中国用户 (api.minimaxi.com)

## 方案 B：MiniMax M2.1 API Key
适用于直接调用 MiniMax 的 API 接口。

### 配置方式
通过 \`openclaw configure\` 菜单选择 **Model/auth** -> **MiniMax M2.1**。或者手动在配置中添加：
\`\`\`json
{
  "env": { "MINIMAX_API_KEY": "你的KEY" },
  "models": {
    "providers": {
      "minimax": {
        "baseUrl": "https://api.minimax.io/anthropic",
        "api": "anthropic-messages"
      }
    }
  }
}
\`\`\`

## 模型对比
- **M2.1**: 适合复杂逻辑和长文本处理。
- **M2.1 Lightning**: 极速响应版本，适合简单任务和快速迭代。

## 注意事项
- 模型引用格式为 \`minimax/MiniMax-M2.1\`。
- MiniMax 的 API 兼容 Anthropic (Claude) 协议，OpenClaw 默认使用该协议进行最佳匹配。
