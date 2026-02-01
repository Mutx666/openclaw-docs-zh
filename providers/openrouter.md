# OpenRouter 供应商配置

OpenRouter 提供了一个统一的 API 接口，让你通过一个 Endpoint 和一个 API Key 就能访问市面上几乎所有的主流大模型。

## 设置方式 (CLI)
使用以下命令快速完成认证配置：
\`\`\`bash
openclaw onboard --auth-choice apiKey --token-provider openrouter --token "你的OPENROUTER_KEY"
\`\`\`

## 配置示例
\`\`\`json
{
  "env": { "OPENROUTER_API_KEY": "sk-or-..." },
  "agents": {
    "defaults": {
      "model": { "primary": "openrouter/anthropic/claude-3.5-sonnet" }
    }
  }
}
\`\`\`

## 注意事项
- 模型引用格式固定为 \`openrouter/供应商/模型名\`。
- OpenRouter 的 API 完全兼容 OpenAI 协议，OpenClaw 会自动处理 Base URL 的切换。
