---
name: cli-token-saving-pattern
description: Use when choosing CLI-first workflows, replacing repeated AI reasoning with deterministic commands, reducing token cost, or designing a toolchain for AI-assisted product development.
---

## 一、 0-1 产品构建：极简 Token 消耗的 CLI 矩阵

为了实现最大化效能，你应当放弃"全家桶"式的 Agent 平台，转而构建一个**"分布式 CLI 插件群"**。

### 1. 市场调研与数据获取阶段


根据 Valyu 官方文档以及其 GitHub 仓库的最新说明，使用 Valyu CLI 替代传统的 Web Search（尤其是通过 MCP 协议挂载的传统搜索工具），在 Token 消耗和时间耗费上有非常明确的数据对比：

`dawid-szewc/perplexity-cli`
    
    - **它是什么**：这是一个由开源社区开发者（Dawid Szewc）维护的轻量级 Python 命令行工具。
        
    - **作用**：它是对 Perplexity API 的封装。通过配置 API Key，你可以直接在终端里向 Perplexity 提问并获取带来源引用的回答，支持流式输出和不同模型（如 `sonar-pro`）的切换。
        
    - **AI 协同**：在自动化脚本中，你可以用它来代替人类去浏览器里查资料，直接将带有精确事实的数据流（stdout）输入给你的开发 Agent。
### 2. 产品定义与规范（PRD/Spec）阶段

- **Google Workspace CLI**: 允许 Agent 直接在你的 Google Docs 或 Sheets 中创建 PRD 原型，无需通过浏览器 GUI。

- **Pandoc**: 终极文档转换原语。将 AI 生成的 Markdown 瞬时转化为 PDF 或 Word，是构建交付文档的标配。


### 3. 技术原型与开发管理

- **gh (GitHub CLI)** ✅ *（真实存在）*：必选。AI 可以通过 `gh issue create` 管理需求池，通过 `gh pr create` 提交代码，Token 消耗极低且原生支持 Agent 工作流。

- **Aider** ✅ *（真实存在）*：开源CLI工具，与Git原生集成。原文声称"比Claude Code节省4.2倍Token"，但未找到对比数据来源。Aider的优势在于Git原生集成和多文件重构能力，而非Token效率。

- **Supabase / Stripe CLI** ✅ *（真实存在）*：用于快速构建后端服务和支付系统。Agent 可以直接通过命令行配置数据库和测试支付钩子。


### 4. 验证与上线阶段

- **Playwright CLI (@playwright/cli)** ✅ *（真实存在）*：Playwright提供命令行工具进行测试录制和运行。原文声称"将快照存为本地YAML"，实际Playwright使用JSON/HTML格式存储trace。
    
- **Vercel / Firebase CLI** ✅ *（真实存在）*：一键部署。让 Agent 负责生产环境的扩缩容和日志监控。


---

## 二、 闭环路径：从"人工实践"到"自动化脚本"

你提到的"实践 -> SOP -> 脚本"是目前最先进的 **"知识固化（Knowledge Distillation）"** 流程。

### 第一步：AI 辅助的 CLI 试错（实践层）

让 AI 在终端直接尝试各种 CLI 命令。

- **痛点：** AI 可能会在命令参数上产生幻觉。

- **对策：** 开启 Aider 的 `watch` 模式。当 AI 执行 `ls` 或 `grep` 报错时，它会自动捕捉错误并修复，这一步是在消耗 Token 换取"正确的路径"。


### 第二步：提取"神经补丁"（SOP 层）

当任务成功后，不要直接关掉对话。对 Agent 发出指令：

> "回顾刚才成功的 `gh` 和 `valyu` 联调流程，为我总结一份 **Markdown SOP**。要求包含所有成功的参数组合和避坑指南。"

### 第三步：SOP 的 Skill 化与脚本化（工具层）

这是最关键的跃迁。

- **自动化：** 让 AI 将上述 SOP 编写成一个 **Bash 脚本** 或 **Python 闭环程序**。

- **收益：** 下次处理同样任务时，你不再需要 Agent 去"思考"和"规划"（高 Token 消耗），而是直接调用这个**"定制化 Skill"**。

- **成果：** 你的 Token 消耗将从"逻辑推理级"下降到"函数调用级"。


---

## 三、 连接未来：VCP 作为你的"Agent 协作网关"

你提到的 **VCP (Virtual Computer Platform)** 恰好可以作为这套 CLI 逻辑的**"大脑皮层"**。

在 VCP 的架构下，你可以实现：

1. **持久化 Skill 库：** 你的"女仆团"中，一位 Agent 专门负责将所有成功的 CLI 脚本分类存储在 VCP 的持久化记忆层。

2. **机机协作流：** 当你想构建一个新功能时，PM Agent 调取 VCP 中的 SOP 脚本，分配给开发 Agent 运行 Aider，测试 Agent 运行 Playwright CLI。

3. **Token 路由：** VCP 可以充当"Token 节油器"，根据任务复杂度决定是启动高昂的"推理模型"（o1-pro）去写脚本，还是用廉价模型（DeepSeek-V3）去跑已有的脚本。

---


### 1. 🔍 信息获取与研究

根据 Valyu 官方文档以及其 GitHub 仓库的最新说明，使用 Valyu CLI 替代传统的 Web Search（尤其是通过 MCP 协议挂载的传统搜索工具），在 Token 消耗和时间耗费上有非常明确的数据对比：

#### 1.1 多少 Token？（大幅节省）

- **节省 4 到 32 倍 Token**：Valyu 官方的 GitHub 仓库指出，通过内置的 Agent Skill 直接让 AI 调用 Valyu CLI，由于无需挂载笨重的 MCP Server（Model Context Protocol），**Token 消耗比传统方式便宜 4 到 32 倍**。
    
- **为 LLM 上下文专门优化**：传统的 Web Search 通常是为“人类浏览器”设计的，AI 获取内容时往往需要消化大量无用的 HTML 标签或冗杂的网页文本，造成严重的“上下文污染”（Context pollution）。而 Valyu 充当了“为 AI 优化的搜索抽象层”，在 Agent 环境下（非 TTY 终端），它会自动以极度精简、干净的 **结构化 JSON** 格式输出结果，直接喂给模型做下游推理（Reasoning），从而将单次交互的 Token 压到了极低的水平。
    

#### 1.2 花多久时间？（分级响应）

这取决于你让它执行什么级别的搜索任务：

- **实时响应（秒级）**： 如果你使用基础的 `valyu search`（多源搜索）或 `valyu answer`（AI 问答）和 `valyu contents`（网页内容提取），它是**实时流式输出 (Streaming) 的**。这意味着比起传统“Agent 搜索 -> 获得一堆 URL -> 逐个访问 URL 刮取网页 -> 总结”的漫长工作流，它一步到位直接返回带引用的答案或干净文本。
    
- **深度研究模式（Deep Research，分钟级到小时级）**： 如果让它代替人去执行深度研究和交叉验证，CLI 官方给出了明确的任务预期时间：
    
    - **Fast（快速模式）**：**约 5 分钟**。适合快速查阅和简单问询。
        
    - **Standard（标准模式，默认）**：**约 10-20 分钟**。适合平衡了速度和深度的调研任务。
        
    - **Heavy（重度模式）**：**约 60 分钟**。适合深度的长篇分析和长报告生成。
        
    - **Max（极限模式）**：**约 90 分钟**。用于追求最大深度和最高质量的信息挖掘。

#### 1.3 **`dawid-szewc/perplexity-cli`**
    
    - **它是什么**：这是一个由开源社区开发者（Dawid Szewc）维护的轻量级 Python 命令行工具。
        
    - **作用**：它是对 Perplexity API 的封装。通过配置 API Key，你可以直接在终端里向 Perplexity 提问并获取带来源引用的回答，支持流式输出和不同模型（如 `sonar-pro`）的切换。
        
    - **AI 协同**：在自动化脚本中，你可以用它来代替人类去浏览器里查资料，直接将带有精确事实的数据流（stdout）输入给你的开发 Agent。
        

### 2. 📝 文档与需求管理

- **Google Workspace CLI (`gws`)**
    
    - **它是什么**：Google 在 2026 年初开源的基于 Rust 编写的命令行工具。
        
    - **作用**：允许开发者直接在终端中管理和读写 Google Docs、Sheets 和 Drive。
        
    - **AI 协同**：你的产品经理 Agent 可以通过纯文本命令，直接在你的 Google 云盘里创建 PRD（产品需求文档）或读取测试数据表，完全跳过浏览器。
        
- **Pandoc**
    
    - **它是什么**：文档转换界的“瑞士军刀”，极其强大且历史悠久的开源 CLI 工具。
        
    - **作用**：支持在几乎所有标记语言（Markdown、HTML、LaTeX、Word、PDF 等）之间进行完美转换。
        
    - **AI 协同**：AI 默认且最擅长输出 Markdown。配合 Pandoc，你可以用一行脚本将 AI 生成的 Markdown 需求文档瞬间打包成带目录的 PDF 或 Word 文档并发送给客户。
        

### 3. 💻 核心开发与代码管理

- **Aider**
    
    - **它是什么**：目前终端里最强大的 **AI 结对编程 CLI 工具**，也就是你进行“Vibe Coding”的核心引擎。
        
    - **作用**：你只需在终端输入自然语言需求，Aider 会自动理解上下文、修改多个本地代码文件，并**自动帮你进行 Git 提交（Commit）**，且附带规范的提交信息。它与 Git 的原生结合是其最大杀器。
        
- **`gh` (GitHub CLI)**
    
    - **它是什么**：GitHub 官方的命令行工具。
        
    - **作用**：将完整的 GitHub 体验带入终端。
        
    - **AI 协同**：你可以写一个脚本，让 AI 通过 `gh issue list` 读取当前 bug，用 Aider 修复 bug，再通过 `gh pr create` 自动提交 Pull Request。整个研发闭环无需打开任何网页。
        

### 4. ⚙️ 后端服务与测试

- **Supabase / Stripe CLI**
    
    - **它们是什么**：分别是开源 BaaS（后端即服务）平台 Supabase 和支付巨头 Stripe 的官方 CLI 工具。
        
    - **作用**：
        
        - **Supabase CLI**：允许你在本地快速拉起 Postgres 数据库和鉴权服务环境，并在终端执行数据库迁移（Migrations）。
            
        - **Stripe CLI**：允许你在本地终端监听和转发支付相关的 Webhooks 事件，这对于测试“用户付款成功”的逻辑至关重要。
            
- **Playwright CLI (`@playwright/test`)**
    
    - **它是什么**：微软出品的现代 Web 端到端（E2E）测试工具的命令行版本。
        
    - **作用**：不仅能运行测试脚本，还能通过命令行直接录制你在浏览器的操作并生成代码。
        
    - **AI 协同**：非常适合作为 Agent 的“测试员”。AI 可以通过命令行启动无头浏览器（Headless Browser）进行点击和表单填写，验证页面是否跑通，并抓取报错日志。
        

### 5. 🚀 部署与上线

- **Vercel / Firebase CLI**
    
    - **它们是什么**：现代前端和全栈项目最常用的部署工具。
        
    - **作用**：你只需要在项目根目录敲下 `vercel` 或 `firebase deploy`，它们就会自动打包项目、分配域名并推送到全球 CDN 上限。
        
    - **AI 协同**：在 CI/CD 脚本中，当 AI 完成代码并通过测试后，可以触发这两个命令直接将产品发布到生产环境。
        

**总结**： 这套工具链的本质是**“用文本指令驱动一切”**。无论是查资料、写文档、改代码、测功能还是搞部署，统统变成了标准输入（stdin）和标准输出（stdout）。这种模式让人类开发者和 AI 能够以最低的损耗（Token）和最快的速度进行对话与协作。

---
### 一、 文献与个人知识管理 (Zotero 替代/增强层)

我们之前提到过 Zotero 的社区版 CLI，但如果追求更纯粹的极客体验和 Agent 友好度，可以使用下面这款：

- **Papis (`papis`)**
    
    - **定位**：一个高度可扩展的、基于命令行的文献和文档管理器。
        
    - **为什么适合 Agent**：与 Zotero 底层的 SQLite 复杂表结构不同，Papis 将每篇文献作为一个单独的文件夹管理，包含 PDF 本身和一个基于 YAML/JSON 的元数据文件（`info.yaml`）。
        
    - **工作流协同**：AI 极度擅长解析和生成 YAML。你可以让 Agent 通过命令行自动抓取 arxiv 的论文，Papis 负责下载并生成标准化的 YAML 标签。随后，Agent 可以用简单的脚本将这些结构化的文献元数据，直接以 Markdown 格式分类注入到你 Obsidian 的 PARA 目录树中，实现文献库与本地笔记的无缝联动。
        

### 二、 数据分析与处理 (Excel/BI 工具的 CLI 平替)

在进行大数据量清洗或基础分析时，启动 Jupyter Notebook 或复杂的数据分析平台往往大材小用，以下工具是终端里的利器：

- **DuckDB CLI (`duckdb`)**
    
    - **定位**：专为分析型查询（OLAP）打造的极速内存/本地数据库 CLI。
        
    - **为什么适合 Agent**：它是“数据分析界的 SQLite”。不需要配置服务端，直接在命令行里对 CSV、Parquet 甚至 JSON 文本写 SQL 语句。DuckDB 在 Apple Silicon M4 这类现代 ARM 架构芯片上，凭借其底层的向量化执行引擎，处理数 GB 的宽表数据过滤和聚合几乎是瞬间完成的。AI 只需要负责写出正确的 SQL 字符串，剩下极其吃计算资源的数据拉取工作全部由 CLI 秒级完成。
        
- **VisiData (`vd`)**
    
    - **定位**：终端里的超级电子表格与数据探索工具。
        
    - **为什么适合 Agent**：支持从 CSV、Excel 到 SQLite 数据库等几乎所有表格数据格式。虽然它是面向人类交互的 TUI（终端用户界面），但它支持通过 `.vd` 脚本重放所有操作。Agent 可以写一段批处理脚本，用 VisiData 瞬间完成几十个表格的数据清洗和去重运算。
        
- **`jq` / `yq`**
    
    - **定位**：JSON 和 YAML 数据的命令行处理器。
        
    - **作用**：数据管道中的“瑞士军刀”。在处理网络请求返回的层级极深的数据时，用它配合 AI，可以用极低的 Token 提取出业务真正需要的核心字段。
        

### 三、 画图与系统设计 (Figma/Visio 的 CLI 方案)

Figma 是纯视觉的，AI 很难直接在终端里“拖拽”像素。因此，在 Agent 工作流中，画图的终极解法是 **“图表即代码（Diagrams as Code）”**。

- **Mermaid CLI (`mmdc`)**
    
    - **定位**：Mermaid 语法的官方命令行渲染工具。
        
    - **为什么适合 Agent**：主流的大模型（如 o1, Claude）都已被“喂”过海量的 Mermaid 语法。当你需要设计一个顶层业务架构或多智能体协同流程时，你只需要让 AI 输出一段 Mermaid 语法的 Markdown 文本。接着，通过执行类似 `mmdc -i input.mmd -o output.png` 的命令，瞬间在本地生成精美的流程图或时序图，完全不需要打开任何画图软件。
        
- **D2 (Declarative Diagramming)**
    
    - **定位**：新一代的声明式图表语言及 CLI。
        
    - **特点**：语法比 Mermaid 更现代、更接近自然语言，且排版引擎极其强悍。AI 生成 D2 脚本的成功率极高，生成的架构图视觉效果可以直接用于高规格的汇报幻灯片。
        
- **Graphviz (`dot`)**
    
    - **定位**：最老牌的图形可视化软件。
        
    - **应用场景**：如果你的 Agent 正在分析一段复杂的代码逻辑，或是梳理底层数据库的关联关系，生成 `.dot` 文件并用 Graphviz 渲染成网络拓扑图，是业界极其成熟的自动化流程。
        

**总结构建思路：** 将这些 CLI 工具集成到你的自动化脚本链条中。让 AI 扮演**“逻辑大脑”**（只输出紧凑的指令、SQL、或 Mermaid 代码），而让这些 CLI 扮演**“高性能执行手”**。这样既能保证极低的大模型 Token 开销，又能利用本地算力获得极高的执行效率。
