# 达尔文.skill

`darwin-skill` 是一个面向 AI Agent 的本地 Skills 进化仓库。

它的目标不是收集更多提示词，而是建立一套 **创建、蒸馏、自进化、筛选、归档和管理 Skills** 的机制，让 Agent 在真实工作中持续判断：

- 哪些复杂但稳定的工作应该 Skill 化
- 哪些重复、繁杂、规则明确的工作应该脚本化
- 哪些 Skills 太粗，需要拆分
- 哪些 Skills 太薄，需要补充触发条件、案例、工具和失败处理
- 哪些 Skills 长期不用，应该归档
- 哪些 Skills 已经失效，应该重构或废弃
- 哪些高频、高价值 Skills 应该进入常驻位

核心原则：

> 用进废退，适者生存，减少上下文浪费。

## 仓库结构

```text
darwin-skill/
├── .codex-plugin/              # Codex 插件描述文件
├── skills/                     # Agent 可加载的核心 Skills
├── scripts/                    # 本地扫描、评分、重构建议脚本
├── registry/                   # Skills 索引、使用记录、演化日志
├── library/                    # 原理层、模型层、方法层、案例层、归档层
├── templates/                  # Skill、审查报告、演化记录模板
├── evals/                      # Skill 效果评估用例
└── docs/                       # 设计文档与机制说明
```

## 四层知识结构

- `library/principles`：原理层，放底层思想、判断原则、认知框架
- `library/models`：模型层，放可迁移的分析模型和任务前判断框架
- `library/methods`：方法层，放可执行 SOP、工作流、检查清单
- `library/cases`：案例层，放具体场景 Skill、脚本和复用样例
- `library/archive`：归档层，放低频、过时或等待重构的内容

## 核心 Skills

- `darwin-skill-manager`：总控 Skill，负责判断何时 Skill 化、脚本化、归档或追问
- `darwin-skill-distiller`：从真实任务中蒸馏可复用 Skill
- `darwin-skill-auditor`：审查 Skill 的质量、粒度、冗余和维护风险
- `darwin-skill-archivist`：处理归档、合并、拆分和退役建议

## 第一阶段目标

1. 扫描用户本地 Skills 和提示词资产
2. 生成 `registry/skills_index.json`
3. 按原理层、模型层、方法层、案例层进行初步归类
4. 标记需要补充、拆分、压缩、脚本化、归档的 Skills
5. 形成第一版 Skills 进化报告
