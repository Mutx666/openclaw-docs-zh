# GLM 系列模型配置

GLM (General Language Model) 是由智谱 AI 等团队开发的一个模型家族。在 OpenClaw 中，你通过 **zai** 供应商来访问 GLM 模型。

## 设置方式 (CLI)
使用以下命令配置 Z.AI API Key：
\`\`\`bash
openclaw onboard --auth-choice zai-api-key
\`\`\`

## 配置示例
\`\`\`json
{
  "env": { "ZAI_API_KEY": "你的KEY" },
  "agents": {
    "defaults": {
      "model": { "primary": "zai/glm-4.7" }
    }
  }
}
\`\`\`

## 支持的模型
- **zai/glm-4.7**：目前最新且性能最强的版本。
- **zai/glm-4.6**：稳定版本。

## 更多详情
关于 zai 供应商的详细配置参数（如 \`baseUrl\` 切换等），请参考 [Z.AI 供应商指南](/providers/zai)。
