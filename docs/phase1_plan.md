# 第一阶段执行计划

## 目标

把现有 `04-skills` 和 `提示词工程` 资产纳入达尔文机制，形成可扫描、可分类、可审查、可迁移、可归档的本地 Skills 仓库。

## 任务拆分

### 1. 资产盘点

- 输入：本地 skills / prompts 目录。
- 工具：`scripts/scan_skills.py`。
- 输出：`registry/skills_index.json`。
- 检查项：文件长度、标题结构、frontmatter、触发描述、四层分类、生命周期状态、建议动作。

### 2. 四层分类

- `library/principles`：长期有效的判断原则、工程红线、执行准则。
- `library/models`：可迁移的思考框架、分析模型、工作范式。
- `library/methods`：可执行 SOP、流程、清单、操作规范。
- `library/cases`：具体案例、工程样例、场景化经验。

### 3. 达尔文核心 Skill

- `darwin-skill-manager`：总控，负责判断 skill 化、脚本化、归档、追问和调度子 skill。
- `darwin-skill-distiller`：从真实任务中蒸馏可复用 skill。
- `darwin-skill-auditor`：审查 skill 质量、冗余、粒度、触发条件和维护风险。
- `darwin-skill-archivist`：提出归档、合并、拆分、退役建议。

### 4. 第一批迁移资产

- `before_analyese.md` -> `library/principles`
- `03_项目三层规训框架.md` -> `library/models`
- `06_vibe-coding-CLI-token节省范式.md` -> `library/models`
- `08_vibe-coding流水线构建与Skill蒸馏.md` -> `library/methods`
- `09_vibe-coding-Harness工程规范.md` -> `library/cases`
- `18_行研信源获取SOP.md` -> `library/methods`

### 5. 迭代节奏

每轮只处理一小批资产：

1. 先扫描，生成客观指标。
2. 再审查，判断保留、拆分、扩写、脚本化或归档。
3. 最后迁移，写入四层结构并更新索引。

## 当前状态

- 已定位 `04-skills` 目录，并扫描 51 个 Markdown 资产。
- 已定位 `提示词工程` 目录，并扫描 34 个 Markdown 资产。
- 当前索引共纳入 85 个资产。
- 第一批迁移保留原文，后续再用 distiller 压缩为标准 Skill 或 reference。
