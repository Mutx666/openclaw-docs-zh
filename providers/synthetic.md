# Synthetic 供应商配置

Synthetic 提供了兼容 Anthropic (Claude) 协议的接口。OpenClaw 将其注册为 **synthetic** 供应商。

## 快速设置
1. 设置环境变量 \`SYNTHETIC_API_KEY\`。
2. 运行配置向导：
\`\`\`bash
openclaw onboard --auth-choice synthetic-api-key
\`\`\`

默认模型会自动设为：\`synthetic/hf:MiniMaxAI/MiniMax-M2.1\`。

## 配置示例
\`\`\`json
{
  "env": { "SYNTHETIC_API_KEY": "sk-..." },
  "models": {
    "providers": {
      "synthetic": {
        "baseUrl": "https://api.synthetic.new/anthropic",
        "api": "anthropic-messages"
      }
    }
  }
}
\`\`\`

## 支持的模型预览 (部分)
Synthetic 支持多种通过 HuggingFace (hf) 桥接的模型：
- **MiniMax-M2.1**
- **Kimi-K2-Thinking**
- **DeepSeek-V3**
- **Qwen3-Coder**

## 注意事项
- **Base URL**：OpenClaw 会自动在 URL 后追加 \`/v1\`，因此配置时请使用 \`https://api.synthetic.new/anthropic\`。
- **费用**：在该供应商下，目前许多模型的 Cost 均标记为 0。
