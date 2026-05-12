# Text Transform 脚本族

## 目标

把第三阶段中“应脚本化”的 13 个提示词资产，拆成：

- 可直接确定性实现的本地文本工具
- 需要模板化或未来再接入 LLM 的语言生成任务

## 当前已实现

`scripts/text_transform.py`

支持：

- `remove-urls`
- `normalize-whitespace`
- `markdown-toc`

示例：

```bash
python3 scripts/text_transform.py --input note.md remove-urls
python3 scripts/text_transform.py --input note.md markdown-toc --max-level 3
python3 scripts/text_transform.py --input note.md --output clean.md normalize-whitespace
```

## 13 个 scriptable 资产的设计归类

### 已纳入第一批 deterministic CLI

- `002_内容处理/003_Remove_URLs.md` -> `remove-urls`
- `002_内容处理/001_Generate_table_of_contents.md` -> `markdown-toc`

### 建议后续做模板化或半自动化

- `001_提示词基础/002_Summarize.md`
- `001_提示词基础/003_Make_longer.md`
- `001_提示词基础/004_Make_shorter.md`
- `001_提示词基础/005_Fix_grammar_and_spelling.md`
- `001_提示词基础/006_Translate_to_Chinese.md`
- `001_提示词基础/007_Emojify.md`
- `002_内容处理/002_Generate_glossary.md`
- `002_内容处理/004_Rewrite_as_tweet.md`
- `002_内容处理/005_Rewrite_as_tweet_thread.md`
- `006_应用场景/006_简易待办事项.md`
- `006_应用场景/007_Dataview插件示例.md`

## 设计原则

1. 能确定性执行的，优先 CLI。
2. 依赖语义判断和风格生成的，保留为模板或后续接 LLM。
3. Skill 负责判断何时调用脚本，脚本负责稳定加工文本。
4. 后续若继续扩展，优先补：
   - `glossary-extract`
   - `todo-normalize`
   - `markdown-dataview-snippet`
