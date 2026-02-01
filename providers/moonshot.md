# Moonshot AI (Kimi) 供应商配置

Moonshot (月之暗面) 提供的 Kimi API 具有原生 OpenAI 兼容端点。OpenClaw 支持标准 Kimi API 和专门的 Kimi Coding 接口。

## 设置方式 (CLI)
根据你的 Key 类型选择：
- **标准 Kimi API**：\`openclaw onboard --auth-choice moonshot-api-key\`
- **Kimi Coding**：\`openclaw onboard --auth-choice kimi-code-api-key\`

> **注意**：Moonshot 和 Kimi Coding 是两个独立的供应商。它们的 Key 不通用，API 端点和模型引用格式也不同。

## 模型引用格式
- **Kimi 标准版**：使用 \`moonshot/kimi-k2.5\`。
- **Kimi 编程版**：使用 \`kimi-coding/k2p5\`。

## 支持的模型 ID (Moonshot)
- \`kimi-k2.5\`：标准全能版。
- \`kimi-k2-thinking\`：具备深度思考能力。
- \`kimi-k2-turbo-preview\`：极速版。

## 国内节点
如果你在中国境内服务器运行网关，建议将 \`baseUrl\` 设置为：
\`https://api.moonshot.cn/v1\`
