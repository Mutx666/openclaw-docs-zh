# setup 命令 (初始化)

用于初始化 `~/.openclaw/openclaw.json` 配置文件和 Agent 工作空间。

## 常用操作示例
- **基础初始化**：`openclaw setup`
- **指定工作空间路径**：`openclaw setup --workspace ~/my-custom-workspace`
- **通过 setup 启动向导**：`openclaw setup --wizard`

## 功能说明
- **补全缺失文件**：如果你的工作空间中缺少 `SOUL.md` 或 `USER.md` 等引导文件，`setup` 会自动重新生成默认模板。
- **配置生成**：如果网关配置文件不存在，它会创建一个包含安全默认值的初始版本。
