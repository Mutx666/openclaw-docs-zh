# OpenAI 供应商配置

OpenAI 为 GPT 模型提供开发者 API。OpenClaw 支持通过 API Key 或 Codex 订阅接入。

## 方案 A：OpenAI API Key (平台模式)
适用于直接 API 调用和按量计费。

### 设置方式 (CLI)
\`\`\`bash
openclaw onboard --auth-choice openai-api-key
# 或者非交互式
openclaw onboard --openai-api-key "你的KEY"
\`\`\`

### 配置示例
\`\`\`json
{
  "env": { "OPENAI_API_KEY": "sk-..." },
  "agents": { "defaults": { "model": { "primary": "openai/gpt-5.2" } } }
}
\`\`\`

## 方案 B：OpenAI Code (Codex) 订阅
适用于希望使用 ChatGPT/Codex 订阅余额而非 API 计费的用户。

### 设置方式 (CLI)
\`\`\`bash
# 在向导中选择 Codex OAuth
openclaw onboard --auth-choice openai-codex
# 或者直接登录
openclaw models auth login --provider openai-codex
\`\`\`

## 注意事项
- 模型引用格式固定为 \`provider/model\`（如 \`openai/gpt-5.2\`）。
- 具体的认证重用规则请参考核心概念中的 [OAuth](/concepts/oauth) 部分。
