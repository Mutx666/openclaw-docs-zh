# 配置文件详解 (Configuration)

OpenClaw 从 `~/.openclaw/openclaw.json` 读取可选的 JSON5 格式配置（支持注释和末尾逗号）。如果文件缺失，系统将使用安全的默认设置。

## 为什么需要配置文件？
- **访问控制**：限制谁可以触发机器人（如 `channels.telegram.allowFrom`）。
- **群组管理**：控制群组白名单及提及（@机器人）触发行为。
- **Agent 定制**：设置 Agent 的工作空间、身份信息（名字、Emoji）以及使用的模型。
- **全局设置**：自定义消息前缀、日志等级及心跳间隔。

## 核心配置结构

### 1. Agent 默认设置 (agents.defaults)
控制模型选择、工作空间路径及沙箱行为。
```json5
{
  "agents": {
    "defaults": {
      "workspace": "~/.openclaw/workspace",
      "model": {
        "primary": "google/gemini-3-flash-preview"
      }
    }
  }
}
```

### 2. 频道配置 (channels)
控制各个通讯平台的接入。
- **dmPolicy**: 处理私聊的策略（`pairing` 推荐 / `open` 全部允许 / `allowlist` 白名单）。
- **allowFrom**: 允许私聊的用户 ID 列表。
- **groups**: 允许接入的群组列表（支持使用 `*` 代表全部）。

### 3. 环境与 Substitutions
你可以在配置文件中使用 `${VAR_NAME}` 语法引用环境变量。这在处理敏感 Key 时非常有用。

## 验证与修复
- **严格验证**：OpenClaw 会严格校验配置格式。格式错误会导致网关拒绝启动以确保安全。
- **自愈命令**：运行 `openclaw doctor --fix` 可以自动迁移或修复旧版本的配置错误。

## 动态更新 (RPC)
- **config.get**: 获取当前生效的完整配置。
- **config.patch**: 增量更新配置（不会覆盖未指定的 Key）。
- **config.apply**: 全量覆盖配置并自动重启网关。
