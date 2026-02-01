# memory 命令 (语义记忆管理)

用于管理语义记忆的索引和搜索功能。该功能由活动的记忆插件（默认为 `memory-core`）提供。

## 常用操作示例
- **查看记忆状态**：`openclaw memory status`
- **深度检查与索引**：`openclaw memory status --deep --index` (检查向量数据库和嵌入模型可用性，如果需要则重新建立索引)
- **手动触发索引**：`openclaw memory index --verbose`
- **语义搜索测试**：`openclaw memory search "发布清单"` (测试模型是否能搜到相关记忆片段)
- **指定 Agent**：`openclaw memory status --agent main`

## 功能说明
- **增量更新**：系统会监控 Markdown 文件的变化并自动标记为“脏（Dirty）”，在下次运行或手动触发时进行更新。
- **外部路径**：`memory status` 会包含通过 `memorySearch.extraPaths` 配置的所有额外 Markdown 目录。
