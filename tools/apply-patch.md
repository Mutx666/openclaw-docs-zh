# apply_patch 工具 (批量打补丁)

\`apply_patch\` 是一个实验性工具，专门为多文件或大规模代码编辑设计。它允许模型通过一种结构化的“补丁”格式一次性修改多个文件，比逐个调用 \`edit\` 更稳定。

## 补丁格式示例
\`\`\`text
*** Begin Patch
*** Add File: notes.txt
+这是一行新内容
*** Update File: src/main.js
@@
-old_function()
+new_function()
*** Delete File: old_script.sh
*** End Patch
\`\`\`

## 启用方式
由于此工具目前处于实验阶段且主要面向 OpenAI 模型，需要手动在配置中开启：
\`\`\`json
{
  "tools": {
    "exec": {
      "applyPatch": {
        "enabled": true
      }
    }
  }
}
\`\`\`

## 注意事项
- **路径**：所有文件路径均相对于工作空间根目录。
- **限制**：目前该工具主要由 OpenAI 系列模型（包括 OpenAI Codex）使用。
- **移动文件**：支持在 \`Update File\` 块中使用 \`*** Move to:\` 指令来重命名或移动文件。
