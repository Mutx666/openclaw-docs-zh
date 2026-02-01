# 浏览器自动化 (Browser Tool)

OpenClaw 允许 Agent 操控一个专门的浏览器实例。这与你个人的浏览器是隔离的，可以用来抓取网页、自动化操作或测试 UI。

## 核心概念
- **独立配置文件**：Agent 使用名为 `openclaw` 的浏览器配置文件，不会干扰你的日常浏览记录。
- **确定性控制**：Agent 通过“快照（Snapshot）”识别页面元素，并通过 ID 执行点击、输入等操作，而不是使用脆弱的 CSS 选择器。

## 浏览器模式
1. **Managed (托管模式)**：由 OpenClaw 直接启动的 Chromium 实例（无需插件）。
2. **Relay (插件模式)**：通过 Chrome 浏览器插件控制你当前的标签页。

## 常用命令 (CLI)
- **查看状态**：`openclaw browser status`
- **启动浏览器**：`openclaw browser start`
- **打开网页**：`openclaw browser open https://example.com`
- **网页快照**：`openclaw browser snapshot`

## Agent 常用动作
Agent 可以调用以下动作进行自动化：
- **navigate**: 跳转 URL。
- **click**: 点击指定 ID 的元素。
- **type**: 在输入框输入文字。
- **screenshot**: 截取当前页面或特定元素的图片。

## 安全提示
- **敏感数据**：浏览器配置文件可能包含登录后的 Session，请妥善保管 `~/.openclaw` 目录。
- **脚本执行**：默认允许 Agent 在页面执行 JS。如果不放心，可在配置中将 `browser.evaluateEnabled` 设为 `false`。
