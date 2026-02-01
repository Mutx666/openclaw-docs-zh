# OpenRouter 供应商配置

OpenRouter 提供统一的 API，允许通过一个端点和一组 API Key 调用数百种模型。它是 OpenAI 兼容的。

## 设置方式 (CLI)
\`\`\`bash
openclaw onboard --auth-choice apiKey --token-provider openrouter --token "你的KEY"
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
- **引用格式**：模型 ID 请遵循 \`openrouter/提供商/模型名\` 的格式。
