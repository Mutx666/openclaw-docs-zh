# Anthropic (Claude) 供应商配置

Anthropic 构建了 Claude 模型家族。在 OpenClaw 中，你可以通过 API Key 或 Setup-token 进行认证。

## 方案 A：Anthropic API Key
适用于标准 API 访问和按量计费。

### 设置方式 (CLI)
\`\`\`bash
openclaw onboard
# 选择: Anthropic API key
\`\`\`

## 提示词缓存 (Prompt Caching)
OpenClaw 原生支持 Anthropic 的提示词缓存功能，可显著降低长上下文的调用成本。
- **配置参数**：使用 \`cacheRetention\`。
- **选项**：\`none\` (禁用), \`short\` (5分钟), \`long\` (1小时)。

## 方案 B：Claude Setup-token
适用于使用你的 Claude Pro/Max 网页版订阅余额。

### 如何获取？
1. 在任何安装了 Claude Code CLI 的机器上运行：\`claude setup-token\`。
2. 复制生成的 Token。
3. 在网关主机运行：\`openclaw models auth paste-token --provider anthropic\` 并粘贴。

## 故障排除
- **401 错误**：订阅认证可能会过期。请重新运行 \`setup-token\` 流程。
- **找不到 API Key**：认证信息是按 Agent 隔离的。新创建的 Agent 不会自动继承主 Agent 的 Key，需单独配置。
