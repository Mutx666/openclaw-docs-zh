# plugins 命令 (插件管理)

用于管理网关插件和扩展。这些插件在网关进程内加载，提供通讯频道、模型供应或自定义工具功能。

## 常用操作
- **列出所有插件**：`openclaw plugins list` (显示已加载和已禁用的插件)
- **查看详情**：`openclaw plugins info <插件ID>`
- **启用/禁用**：
  - `openclaw plugins enable <插件ID>`
  - `openclaw plugins disable <插件ID>`
- **插件体检**：`openclaw plugins doctor`

## 插件安装与更新
- **安装插件**：`openclaw plugins install <NPM包名或本地路径>`
  - 安全提示：安装插件相当于运行外部代码，请仅安装可信来源的插件。
  - 支持格式：NPM 规范、`.zip`, `.tgz` 压缩包。
- **更新插件**：
  - 更新指定插件：`openclaw plugins update <插件ID>`
  - 更新所有插件：`openclaw plugins update --all`
  - *注：仅支持从 NPM 安装的插件更新。*

## 插件清单 (Manifest)
每个插件必须包含 `openclaw.plugin.json` 文件，其中定义了插件的配置架构（Schema）。
