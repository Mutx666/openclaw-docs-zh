# Microsoft Teams 频道插件 (Azure Bot API)

**当前状态**：作为可选插件提供。支持文本、私聊附件及基于 Adaptive Cards 的投票功能。

## 插件安装
\`\`\`bash
openclaw plugins install @openclaw/msteams
\`\`\`

## 必备条件
1. 在 [Azure Portal](https://portal.azure.com/) 创建一个 **Azure Bot** 资源。
2. 获取 **App ID**, **Client Secret** 和 **Tenant ID**。
3. 配置 **Messaging Endpoint** 指向你的网关 URL，后缀为 \`/api/messages\`（默认端口 3978）。
4. 下载或通过 [Teams Developer Portal](https://dev.teams.microsoft.com/apps) 构建 Teams 应用安装包。

## 核心配置
```json
{
  "channels": {
    "msteams": {
      "enabled": true,
      "appId": "你的APP_ID",
      "appPassword": "你的APP_PASSWORD",
      "tenantId": "你的TENANT_ID"
    }
  }
}
```

## 运行机制
- **私聊 (DM)**：自动归入主会话。
- **群聊与频道**：默认处于白名单模式（\`allowlist\`），需在配置中显式允许特定的 Team 或设置 \`groupPolicy: "open"\`。
- **提及触发**：在群聊中默认必须 @机器人。

## 进阶功能
- **Adaptive Cards**：支持发送复杂的卡片交互界面。
- **SharePoint 集成**：若需在群聊中发送文件，需配置 \`sharePointSiteId\` 并赋予 Graph API 权限。

## 常见问题
- **401 错误**：手动测试 Webhook 时出现是正常的，因为缺少 Azure 的 JWT 认证。
- **图片无法显示**：在群组/频道中显示图片通常需要额外的 Microsoft Graph 权限（\`ChannelMessage.Read.All\`）。
