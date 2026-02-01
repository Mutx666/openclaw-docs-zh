# Z.AI 供应商配置

Z.AI 是 GLM 系列模型的官方 API 平台。OpenClaw 通过 **zai** 供应商支持 Z.AI 平台。

## 设置方式 (CLI)
\`\`\`bash
openclaw onboard --auth-choice zai-api-key
# 或者非交互式
openclaw onboard --zai-api-key "你的ZAI_KEY"
\`\`\`

## 配置示例
\`\`\`json
{
  "env": { "ZAI_API_KEY": "sk-..." },
  "agents": {
    "defaults": {
      "model": { "primary": "zai/glm-4.7" }
    }
  }
}
\`\`\`

## 技术细节
- **认证方式**：使用标准 Bearer Token 验证 API Key。
- **模型格式**：全部模型均以 \`zai/\` 开头（例如 \`zai/glm-4.7\`）。
