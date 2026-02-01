# skills 命令 (技能管理)

用于查看和检查系统中可用的技能（包括内置技能、工作空间自定义技能以及管理覆盖的技能）。

## 常用操作示例
- **列出所有技能**：`openclaw skills list`
- **列出当前可用的技能**：`openclaw skills list --eligible` (过滤掉缺少依赖项的技能)
- **查看技能详情**：`openclaw skills info <技能名称>`
- **依赖检查**：`openclaw skills check` (扫描系统中缺失的二进制文件或环境依赖)

## 技能来源说明
- **Bundled**：随 OpenClaw 核心包分发的内置技能。
- **Workspace**：存放在 Agent 工作空间 `skills/` 目录下的自定义技能（同名时优先级最高）。
- **Managed**：通过 CLI 独立安装和管理的第三方技能。
