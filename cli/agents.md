# agents 命令 (Agent 管理)

用于管理相互隔离的 Agent（包括独立的工作空间、认证信息和路由绑定）。

## 常用命令示例
- **列出所有 Agent**：`openclaw agents list`
- **添加新 Agent**：`openclaw agents add work --workspace ~/.openclaw/workspace-work`
- **删除 Agent**：`openclaw agents delete work`
- **设置身份信息**：
  - 从 `IDENTITY.md` 文件加载：`openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity`
  - 手动指定：`openclaw agents set-identity --agent main --name "小爱同学" --emoji "❤️"`

## 身份信息 (Identity)
每个 Agent 的工作空间根目录下可以包含一个 `IDENTITY.md` 文件。身份信息包括：
- **name**：显示名称。
- **theme**：风格主题。
- **emoji**：代表性表情。
- **avatar**：头像路径（支持工作空间相对路径、URL 或 Data URI）。

## 配置示例
```json
{
  "agents": {
    "list": [
      {
        "id": "main",
        "identity": {
          "name": "小爱同学",
          "emoji": "❤️",
          "avatar": "avatars/logo.png"
        }
      }
    ]
  }
}
```
