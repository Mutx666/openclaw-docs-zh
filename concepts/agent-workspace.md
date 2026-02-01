# Agent 工作空间 (Agent Workspace)

工作空间是 Agent 的“家”。它是文件工具使用的唯一工作目录，也是 Agent 获取上下文信息的来源。

## 默认位置
- **默认路径**：`~/.openclaw/workspace`
- 它与 `~/.openclaw/` 目录是分开的，后者用于存储配置文件、凭据和会话记录。

## 核心文件映射 (Workspace Map)
以下是工作空间内常见的标准文件及其含义：

- **AGENTS.md**：Agent 的运行指令和内存使用规范。每轮会话开始时都会加载。
- **SOUL.md**：定义 Agent 的人格、语气和行为边界。
- **USER.md**：描述用户是谁以及如何称呼用户。
- **IDENTITY.md**：Agent 的名字、风格倾向和代表性 Emoji。
- **TOOLS.md**：关于本地工具和惯例的说明笔记。
- **HEARTBEAT.md**：心跳任务的简短检查清单。
- **memory/**：按日期生成的每日内存日志（如 `YYYY-MM-DD.md`）。
- **MEMORY.md**：经过整理的长期记忆（仅在私人会话中加载）。

## 安全建议
- **不要提交私钥**：切勿在工作空间内存储 API Key、密码或 OAuth Token。
- **Git 备份**：建议将工作空间初始化为私有 Git 仓库，以便备份和迁移。
- **排除项**：确保 `.gitignore` 文件排除了 `.env`, `*.key` 等敏感文件。

## 迁移工作空间
1. 将仓库克隆到新机器的目标路径。
2. 修改 `openclaw.json` 中的 `agents.defaults.workspace` 指向新路径。
3. 运行 `openclaw setup --workspace` 补全缺失的默认文件。
