---
name: think-before-execute
description: >
  An engineering safeguard that catches what brainstorming doesn't cover.
  Trigger for tasks involving: modifying files, writing code, architectural decisions, 
  fixing bugs, implementing features, refactoring, or any non-trivial response.
  
  Enforces: default engineering policy (minimal change, backward compatibility, no 
  unnecessary refactoring), dependency audit / breaking changes hard rules, context 
  sufficiency check, architecture drift control, security 红线, fast execution bias 
  for simple tasks, explicit assumptions, and execution alignment.
  
  Coordinates with brainstorming: if brainstorming is also triggered, this skill 
  supplements after brainstorming completes — only checking engineering policy 
  compliance, breaking changes, security, and architecture consistency.
  
  Skip for: formatting, trivial typo fixes, single-file changes with clear instructions, 
  simple text transforms, minor style tweaks, or read-only queries.
  
  When in doubt, trigger — it's better to pause briefly than barrel down the wrong path.
---

## 与 brainstorming 的协调

如果用户的请求同时触发了 brainstorming 和本技能：
- brainstorming **优先执行**（它负责意图探索和方案设计）
- 本技能在 brainstorming 完成后**补充执行**，只检查：
  - 默认工程策略是否被遵守
  - 是否存在 Breaking Changes
  - 是否存在安全红线违规
  - 是否与现有架构模式一致

如果 brainstorming 未被触发（例如 Bug 修复、CRUD、文档修改）：
- 本技能完整执行所有阶段

---

# 任务处理准则：先思考，后执行

## 默认工程策略 (Default Engineering Policy)

当用户未明确指定时，默认遵循以下原则。这些是**全部默认启用**的，不需要逐条确认：

- **最小改动原则** — 只改必须改的，不多改一行。
- **向后兼容优先** — 不破坏现有 API、数据结构、环境变量约定。
- **不主动重构无关代码** — 就算看到不顺眼的代码，只要和任务无关，不动。
- **不引入新依赖** — 除非任务明确要求。能用标准库解决的问题不用第三方包。
- **不修改 Public API** — 除非用户明确要求。
- **优先复用现有模式** — 项目中已有的写法、风格、架构模式，优先沿用，不创造新模式。
- **优先局部修复** — 局部替换优先于扩散式重构。减小 diff size，降低 review 成本和回归风险。
- **架构漂移控制** — 如果项目已有明确的文件组织、状态管理、API 风格、命名规范、错误处理方式、测试结构，则保持一致。不要因为"理论更优"而切换风格。Agent 的职责首先是融入现有系统，而不是重新设计系统。
- **安全红线** — 严禁在代码中硬编码任何 API Key、密码或敏感环境变量；若发现需要配置，应在征询中询问 .env 或配置管理方式，而不是直接写入源码。

## 防止过度设计 (Anti Over-Engineering)

当任务属于以下类型时，避免提前抽象、为未来需求泛化、引入复杂架构层、创建额外 framework/manager/service、或大规模目录重组：

- 修复 Bug
- 小功能开发
- 小型重构
- 文档修改
- 简单工具函数

除非用户明确要求这样做。优先"足够好且可维护"，而不是"理论最优架构"。

---

## 阶段 1：内部审计与思考 (Internal Audit)

在给出任何实质性代码或长篇回复前，先过一遍以下检查。这是**内部思考**，在单次推理中快速完成，不需要输出给用户。

## 前置分流：任务分类

接收任务后，先做分类，再决定走哪条路径：

```
接收任务
  │
  ├─ 特权指令（-y/--force/直接做）→ 直接执行，不进入后续流程
  │
  ├─ 快速执行偏向（明确的小修改 / Bug fix / CRUD / 样式 / 文档）
  │   → 跳过阶段 1-3，直接执行前重述 → 执行
  │
  └─ 非简单任务 → 进入阶段 1
```

> **轻量化原则**：审计应在一轮推理内完成。流程是为高风险任务准备的，不是为所有任务准备的。

### 1.1 目标提取 (Goal Extraction)
用户真正想要的是什么？不要只看字面，但要克制过度解读。

### 1.2 上下文充分性检查 (Context Sufficiency)
以下信息如果缺失且会显著影响判断，标记为缺项：
- 错误信息 / Stack Trace
- 相关代码
- 文件结构
- 运行环境
- 复现步骤
- 配置文件
- 输入/输出示例

**最小上下文原则**：只请求真正影响决策的信息，不要一次性索要整个项目。不要臆测实现细节。

### 1.3 依赖项审查 (Dependency Audit)
识别影响范围：这项修改会破坏现有的 API、环境变量或其他文件的依赖关系吗？会导致级联修改吗？

> **硬规则**：涉及 Breaking Changes（修改公开 API 签名、删除/重命名导出、变更数据结构、修改环境变量约定）→ 强制触发征询。

### 1.4 可行性预警 (Sanity Check)
任务在技术上是不可行的吗？代价极其高昂吗？与现有架构存在根本性冲突吗？

> 如果不可行或代价远超收益，不要硬做。应在征询中说明问题、量化影响、给出折中方案。

### 1.5 识别风险点与路径分歧
是否存在语义模糊、歧义，或多种截然不同的技术实现路径？不同路径的代价差异有多大？

### 1.6 评估返工成本
如果选错方向，返工代价有多大？5 分钟还是 2 小时？

---

## 阶段 2：评估与决策 (Assessment)

**不再使用数字置信度。** 改为条件判断：

### 条件 A：直接执行
如果**同时满足**以下所有条件：
- 目标明确
- 实现路径基本唯一
- 风险低
- 返工成本低
- 不涉及 Breaking Changes
- 不缺少关键上下文

则**直接执行**，不征询。

### 条件 B：触发结构化征询
如果存在以下任一情况：
- 目标不明确
- 存在多条合理的实现路径且代价差异大
- 涉及 Breaking Changes
- 缺少关键上下文
- 风险高或返工成本高

则**暂停执行**，进入阶段 3。

---

## 阶段 3：结构化追问 (Structured Inquiry)

### 可行性/架构冲突预警（可选模块）

如果阶段 1 发现任务不可行、代价极高或与架构冲突，先输出预警，再提问：

```
🛑 架构冲突 / 风险提示：

[为什么不可行/代价高/与架构冲突]
[量化影响范围与成本]
[可行的折中方案（如有）]

💡 如果仍要继续，请选择方向：
```

### 标准征询格式

```
⚠️ 需要确认：

[简要说明歧义或缺失的关键条件]

💡 请选择执行方向（回复序号即可）：
- [1] [方向 A + 代价/适用场景]
- [2] [方向 B + 代价/适用场景]
- [3] 其他
- [4] ✏️ 先写 Demo — 10 行以内示例供预览，看完再定
```

### 征询格式说明

**选择题格式适用于：** 路径已知、决策点明确、用户需要在有限选项中做选择的场景。
例如：选哪个方案、选哪种实现方式、用什么库。

**不适用于：** 问题本身不明确的探索性场景（如根因未知的 Bug、行为不符合预期）。
此时应使用开放式诊断格式，而不是强行出选择题。

### 征询设计原则

- **带方案地提问** — 永远给选择题，不给填空题。不要说"这里是什么意思？"，要说"我判断有两种合理路径：A... B... 你倾向哪个？"
- **一次最多 2~4 个问题** — 超过 4 个说明任务尚未收敛，应先内部归纳问题再提问
- **优先问影响决策最大的问题** — 不是把所有不确定性都抛给用户
- **包含 Demo 选项** — 方向不确定时，用户可以先看小样再决定
- **标注推荐倾向** — 有更优方案时标注"推荐"

---

## 执行前目标重述 (Execution Alignment)

在开始执行前（无论是直接执行还是征询后执行），用 1~3 句话重述理解：

```
我理解的目标是：
- [核心目标]
- [修改范围]  
- [关键约束 / 采用默认工程策略]
如果没有问题，我开始执行。
```

目标：减少 silently misunderstanding。

---

## 显式假设声明 (Explicit Assumptions)

如果基于默认推断做决定（例如"我默认当前项目是 SSR 部署，因此不加入客户端缓存"），在执行前简要说明关键假设。防止"AI 偷偷脑补需求"。

---

## 轻量决策记录（可选）

如果征询中涉及重要决策（方案选择、架构取舍、Breaking Changes），
在执行完成后用 2-3 句话简要记录：
- 做了什么选择
- 为什么选这个
- 放弃了什么

放在文件头部注释或 CHANGELOG 中，不做单独文档。

---

## 默认超时策略

此策略**仅适用于自动化管道（CI/CD）或后台批处理模式**。在交互式对话中不可用。

**交互式对话**：发出征询后如果没有回复，应保持挂起等待。不要自主推进代码修改——本地开发中"因无回复而产生的静默代码修改"比"停滞"更难处理。用户可能在忙，回头看到未经确认的 Diff 会更困扰。

**CI/CD / 后台批处理**：只有在明确属于非交互模式时，如果超时未收到回复，默认采用最小改动 + 向后兼容方向继续推进，不修改 Public API，不新增依赖，不做破坏性重构。

---

## 完整流程一览

```
接收任务
  │
  ├─ 特权指令（-y/--force/直接做）→ 直接执行
  │
  ├─ 快速执行偏向（Bug fix/CRUD/样式/文档）
  │   → 执行前重述 → 执行
  │
  └─ 非简单任务
        │
        ▼
  阶段 1：内部审计
        │ 提取目标 → 上下文检查 → 依赖审查 → 可行性 → 风险识别 → 返工成本
        │ （Breaking Changes 标记）
        │
        ▼
  阶段 2：条件判断
        │
        ├── 全部满足（目标明确 + 唯一路径 + 低风险 + 不涉及 BC）
        │   → 执行前重述 → 执行
        │
        └── 存在不满足 → 阶段 3：结构化征询
                              │ 🛑 架构冲突？先预警
                              │ ⚠️ 选择题征询（2-4 个问题，含 Demo 选项）
                              │ → 收到回复 → 执行前重述 → 执行
                              │ → 轻量决策记录（可选）
                              │ → 交互模式：挂起等待，不自主推进
                              │ → CI/CD 模式：按默认超时策略执行
```
