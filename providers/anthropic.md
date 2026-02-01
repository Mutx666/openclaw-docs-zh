# Anthropic (Claude) 供应商配置

Anthropic 开发了 Claude 系列模型。OpenClaw 支持通过 API Key 或 Setup-token 接入。

## 方案 A：Anthropic API Key
适用于标准 API 访问和按量计费。

### 设置方式 (CLI)
\`\`\`bash
openclaw onboard --anthropic-api-key "你的KEY"
\`\`\`

### 提示词缓存 (Prompt Caching)
OpenClaw 原生支持 Anthropic 的缓存功能，可显著降低长对话的费用：
- **short**: 5 分钟缓存（API Key 模式下的默认值）。
- **long**: 1 小时缓存（需要开启 beta 标志）。

## 方案 B：Claude setup-token
适用于希望使用你的 **Claude Pro 订阅** 额度的用户。

### 如何获取 Token
在任何安装了 \`claude-code\` 的机器上运行：
\`\`\`bash
claude setup-token
\`\`\`
然后将生成的 Token 粘贴到 OpenClaw 网关：
\`\`\`bash
openclaw models auth paste-token --provider anthropic
\`\`\`

## 故障排除
- **401 错误**：Claude 订阅认证可能会过期。请重新运行 \`setup-token\` 流程。
- **找不到 Key**：认证信息是按 Agent 隔离的。如果你新建了 Agent，需要为它单独配置一次 Key。
