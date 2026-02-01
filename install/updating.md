# 版本更新 (Updating)

OpenClaw 迭代速度非常快。我们建议将更新视为基础架构的维护：更新 -> 检查 -> 重启 -> 验证。

## 推荐方式：重新运行安装脚本
这是最简单的路径，它会自动检测现有安装并执行平滑升级：
```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

## 命令行更新
如果你是通过 npm 或 pnpm 全局安装的：
```bash
npm i -g openclaw@latest
# 或者
pnpm add -g openclaw@latest
```

## 切换更新频道
你可以选择稳定版、测试版或开发版：
- `openclaw update --channel stable` (推荐)
- `openclaw update --channel beta`
- `openclaw update --channel dev`

## 更新后必做
1. **运行医生诊断**：`openclaw doctor`（自动迁移配置并修复潜在错误）。
2. **重启网关**：`openclaw gateway restart`（应用新代码）。
3. **健康检查**：`openclaw health`。

## 回滚 (Rollback)
如果新版本出现问题，你可以安装指定版本号进行回滚：
```bash
npm i -g openclaw@<版本号>
openclaw doctor
openclaw gateway restart
```
