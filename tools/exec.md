# Exec 工具 (命令行执行)

\`exec\` 是 Agent 最核心的工具，允许它在工作空间内运行 Shell 命令。它支持前台同步运行和后台异步运行。

## 参数说明
- **command** (必填)：要运行的 Shell 命令。
- **background** (布尔值)：是否立即转入后台运行。
- **pty** (布尔值)：是否开启虚拟终端（运行交互式 CLI 或编程 Agent 时必选）。
- **host**：执行位置（\`sandbox\` 沙箱 / \`gateway\` 本地网关 / \`node\` 远程节点）。
- **security**：安全模式（\`deny\` 禁用 / \`allowlist\` 白名单 / \`full\` 完全开放）。

## 核心概念

### 1. 执行位置 (Host)
- **sandbox (默认)**：在隔离的 Docker 容器中运行。
- **gateway**：在运行网关的宿主机上直接运行。
- **node**：在已配对的远程节点（如你的 Mac 或手机）上运行。

### 2. 审批机制
如果 Agent 试图在宿主机（gateway）执行敏感命令，系统会弹出审批请求。你可以通过 `/exec` 命令查看或设置当前会话的审批策略。

## 安全建议
- **开启沙箱**：强烈建议为所有 Agent 默认开启沙箱模式。
- **白名单限制**：在 \`openclaw.json\` 中配置 \`tools.exec.safeBins\`，限制 Agent 只能运行特定的安全指令（如 \`ls\`, \`pwd\`, \`cat\`）。

## 常见操作示例
- **查看文件**：\`{"tool": "exec", "command": "ls -la"}\`
- **后台构建**：\`{"tool": "exec", "command": "npm run build", "background": true}\`
- **发送快捷键**：通过 \`process\` 工具向后台进程发送 \`Ctrl+C\` 或 \`Enter\`。
