# 网络工具 (Web Tools)

OpenClaw 提供了两个轻量级的网络工具，用于获取外部信息。

## 核心工具
### 1. web_search (网页搜索)
通过第三方 API 搜索互联网。
- **支持供应商**：
  - **Brave Search** (默认)：返回结构化的网页列表（标题、URL、摘要）。
  - **Perplexity**：返回经过 AI 整合后的答案并附带引用来源。
- **配置**：需要在 `openclaw.json` 中配置对应的 API Key。

### 2. web_fetch (网页抓取)
直接抓取指定 URL 的内容。
- **功能**：将 HTML 网页转换为干净的 Markdown 或纯文本。
- **局限性**：它不支持执行 JavaScript。如果网页是重度 JS 渲染或需要登录，请改用 [Browser 浏览器工具](tools/browser.md)。

## 快速配置示例 (Brave Search)
运行命令：
\`\`\`bash
openclaw configure --section web
\`\`\`
或者手动编辑配置文件：
\`\`\`json
{
  "tools": {
    "web": {
      "search": {
        "provider": "brave",
        "apiKey": "你的BRAVE_KEY"
      }
    }
  }
}
\`\`\`

## 进阶功能：Firecrawl
如果你配置了 Firecrawl 的 API Key，\`web_fetch\` 会在常规抓取失败时自动切换到 Firecrawl，利用其强大的绕过反爬机制的能力来获取内容。
