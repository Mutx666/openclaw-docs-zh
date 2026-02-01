# OpenCode Zen 供应商配置

OpenCode Zen 是由 OpenCode 团队精心挑选并推荐的编程模型列表。它通过 **opencode** 供应商提供托管式模型访问。

## 设置方式 (CLI)
\`\`\`bash
openclaw onboard --auth-choice opencode-zen
# 或者非交互式
openclaw onboard --opencode-zen-api-key "你的OPENCODE_KEY"
\`\`\`

## 配置示例
\`\`\`json
{
  "env": { "OPENCODE_API_KEY": "sk-..." },
  "agents": {
    "defaults": {
      "model": { "primary": "opencode/claude-opus-4-5" }
    }
  }
}
\`\`\`

## 注意事项
- **状态**：目前处于 Beta 测试阶段。
- **计费**：按请求计费，需在 OpenCode 仪表盘添加支付信息。
- **别名支持**：环境变量 \`OPENCODE_ZEN_API_KEY\` 与 \`OPENCODE_API_KEY\` 均可。
