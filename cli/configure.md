# configure 命令 (配置修改)

交互式提示符，用于修改现有的凭据、设备绑定和 Agent 默认设置。

## 常用命令示例
- **全量修改**：`openclaw configure` (启动交互式菜单)
- **局部修改**：`openclaw configure --section models --section channels` (仅修改模型和频道部分)

## 功能特性
- **模型白名单**：在模型设置中，你可以勾选哪些模型出现在交互界面（如 Dashboard 或聊天频道）的 `/model` 切换列表中。
- **ID 自动解析**：在设置 Slack/Discord 等频道时，你可以输入频道名称，向导会自动帮你转换成内部使用的 ID。
- **非交互编辑**：对于脚本或自动化操作，建议使用 `openclaw config set|get|unset` 进行直接操作。
