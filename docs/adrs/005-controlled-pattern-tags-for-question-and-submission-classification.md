# Controlled Pattern Tags For Question And Submission Classification

日期: 2026-06-10

相关背景:

- [services/shared/prisma/schema.prisma](../../services/shared/prisma/schema.prisma)
- [services/leetcode-mcp-service/README.md](../../services/leetcode-mcp-service/README.md)
- [services/leetcode-intelligence-service/README.md](../../services/leetcode-intelligence-service/README.md)

## 背景

当前 `leetcode-qa` 已经有两类核心持久化对象:

- `Question`
- `Submission`

其中:

- `Question.topicTags` 更接近 LeetCode 官方题目标签
- `Submission.thought` / `Submission.mistake` 更接近每次提交后的自然语言复盘

这两层都重要，但它们还不能解决现在越来越明显的一个问题:

> 题刷得越多，归类语言越散，最后很难收敛成一套稳定的模板系统。

具体来说，当前缺的是一套 **受控的、自定义的、可复用的 pattern taxonomy**，用来回答下面几件事:

- 这道题我应该按什么模板理解
- 这道题常见的 approach 是什么
- 这道题主要依赖什么 data structure
- 我这次 submission 实际采用了哪一种解法标签

如果继续只靠自由文本或随手写的 JSON tags，会出现几个问题:

1. 同一个意思会被写成很多近义词，后面很难聚合
2. 一道题可能有多种经典解法，但当前结构没有显式表达“题目可有多个候选解法”
3. 一次具体 submission 采用了哪种模板，和这道题有哪些候选模板，是两种不同语义，不能混在一起
4. 前端 table 可以展示 tags，但如果 tags 本身不受控，只会把混乱可视化，而不会帮助收敛

另外，这里还有一个非常重要的边界:

> `Question` 里的题目元数据是只读事实源，不是给本地学习系统写自定义分类的地方。

也就是说，这次设计必须默认接受下面这个约束:

- `Question` 记录的是外部题库同步过来的 canonical metadata
- 本地的 pattern taxonomy 只能外挂，不能把自定义字段回写到 `Question` 本体

## 决策

### 1. 新增一套受控的 pattern tag 系统

这版在现有 `Question` / `Submission` 基础上，新增一套独立的 pattern tag 表，而不是把所有自定义 tags 继续塞进 `Submission.submissionDetails`。

原因:

- tag 本身需要成为稳定实体，才能做约束、去重、排序、父子层级、统一命名
- 只有独立成表，后面才能让前端/服务端共享同一套 vocabulary

### 2. pattern tag 只收敛三种维度

这版只保留三种受控维度:

- `template`
- `approach`
- `data_structure`

明确不纳入这版 pattern taxonomy 的内容:

- `mistake`
- 自由文本 thought
- 临时性的个人备注

原因:

- `mistake` 更像一次 submission 的局部复盘，不适合作为长期稳定 taxonomy
- `thought` 需要保留表达自由度，继续留在 `Submission.thought`
- 这次的目标是“让刷题知识收敛”，不是把所有复盘内容都结构化

### 3. 第一版只做 submission-level 绑定

pattern tag 第一版只绑定到 `Submission`。

语义是:

- `SubmissionPatternTag`
  表示这次提交 **实际用了** 这些标签，属于解法落地记录

这版不建立 `QuestionPatternTag`。

原因:

- 当前最重要的问题是“每次 submission 实际采用了哪个模板”
- `Question` metadata 是只读事实源，不承担本地学习分类
- 题目级 canonical 分类可以从多次 submission 聚合出来，先不提前固化成一张表

例子:

`Two Sum` 的某一次 submission 可以拥有:

- `template: one-pass-hash`
- `approach: complement-lookup`
- `data_structure: hash-map`

### 4. `Question` 是只读题库实体，自定义分类必须外挂

这次设计默认:

- `Question` 本体只承载只读题库 metadata
- 自定义 pattern taxonomy 不允许直接写回 `Question` 自身字段
- 第一版不为 `Question` 建立 pattern tag 关系表

这意味着:

- 不新增 `Question.customTags`
- 不重载 `Question.topicTags`
- 不把自定义 pattern 分类塞回 `Question.content` 或其他 metadata 字段
- 不新增 `QuestionPatternTag`

### 5. 保留现有 Question / Submission 作为主实体

这次不重做 `Question` 和 `Submission` 的主结构。

已有字段继续保留原职责:

- `Question.topicTags`
  保留官方题型 / 题面语义标签
- `Submission.thought`
  保留自然语言解题思路
- `Submission.mistake`
  保留自然语言复盘
- `Submission.submissionDetails`
  仍可放一些与平台返回或分析过程相关的辅助元数据

pattern tag 系统是增量挂接，不替代这些字段。

### 6. 支持受控 vocabulary，而不是开放式自由打标签

这版 pattern tag 的核心目标不是“用户可以随时造新 tag”，而是:

- 先维护一套小而稳定的 canonical tag set
- 让后续 submission 尽量复用已有 tag
- 只有当某个新模式确实反复出现时，再显式加入 taxonomy

初始 template seed 必须以 canonical algorithm skeleton 为单位，而不是以某一道 classic problem 的具体解法为单位。

自动分类器应该只选择 `isActive = true` 的可执行子模板，例如 `hash-map-lookup`、`prefix-sum`、`sliding-window`、`tree-dfs`、`dynamic-programming`。

Classic problems 只能作为 template metadata 里的 examples / anchors，不能反过来变成 template key。

例如:

- 好: `hash-map-lookup`
- 好: `two-pointers`
- 好: `tree-dfs`
- 不好: `two-sum-complement-map`
- 不好: `same-tree-dual-recursion`
- 不好: `word-search-grid-backtracking`

因此这版默认约束是:

- 每个 tag 必须有唯一 `key`
- 每个 tag 必须归属于一个 `dimension`
- tag 允许有 `parent-child` 层级，用于做轻量 taxonomy 收束

例如:

- `template: sliding-window`
  - `approach: expand-shrink-window`
- `template: monotonic-stack`
  - `data_structure: stack`

### 7. template 必须记录来源，但来源不是 pattern dimension

为了支持后续 LLM 生成 template，同时保持 seed vocabulary 可治理，`PatternTag` 需要显式记录来源。

这里刻意不把来源塞进 `PatternTagDimension`。

语义区别是:

- `dimension`
  表示这个 tag 在解题 taxonomy 中扮演的角色，例如 `template` / `approach` / `data_structure`
- `source`
  表示这个 tag 是怎么进入系统的

`source` 当前只允许:

- `seeded`
  由 seed 脚本 provision 的受控模板
- `manually_created`
  用户手工加入并接受维护的模板
- `llm_generated`
  LLM 基于 submission / question context 提议或生成的模板

约束:

- seed 脚本只能创建、更新、停用 `source = seeded` 的模板
- seed 脚本不能删除或停用 `manually_created` / `llm_generated` 模板
- LLM 生成的模板仍然必须满足 template metadata contract，不能绕过 `description`、`whenToUse`、`whenNotToUse`、`signals`、`pseudocode`、`invariants`、`defaultComplexity`

### 8. 允许题目多解，但第一版按 submission 收敛

为了避免“加了 tag table 以后反而更发散”，这版约束每次 submission 的标签数量。

建议约束:

- 每个 `Submission`
  - `template`: 最多 `1`
  - `approach`: 最多 `1-2`
  - `data_structure`: 最多 `2`

这些约束的目标是逼迫每次提交做取舍，而不是把所有可能性都挂上去。

### 9. data structure tags 走固定受控空间

`data_structure` 不应该由 LLM 或自由输入随意创建。

这类 tag 用来表达一次 submission 主要依赖哪些基础结构，因此必须来自 seeded fixed tag space。

当前规则:

- `data_structure` tags 由 seed 脚本 provision
- key 使用 `ds-*` namespace，避免和 canonical template key 冲突
- UI 只允许从 active fixed tags 里选择
- LLM generated template 可以在 metadata 里引用 data structure 名称，但不能自动创建新的 `data_structure` tag

例子:

- `ds-array`
- `ds-hash-map`
- `ds-stack`
- `ds-heap`
- `ds-linked-list`
- `ds-tree`
- `ds-graph`
- `ds-trie`
- `ds-disjoint-set`

## 推荐数据模型

### `PatternTag`

受控 tag 主表。

建议字段:

- `id`
- `key`
- `label`
- `dimension`
- `source`
- `description`
- `parentId`
- `isActive`
- `sortOrder`
- `createdAt`
- `updatedAt`

其中:

- `key` 用于程序和 API 识别
- `label` 用于 UI 展示
- `dimension` 当前只允许:
  - `template`
  - `approach`
  - `data_structure`
- `source` 当前只允许:
  - `seeded`
  - `manually_created`
  - `llm_generated`
- `parentId` 用于可选的轻量层级收束

### `SubmissionPatternTag`

提交级 pattern tag 关系表。

建议字段:

- `id`
- `submissionId`
- `patternTagId`
- `createdAt`

这里不强制增加更多元信息，先保持关系表轻量。

如果以后需要表达 “这次 submission 的主模板是哪一个”，可以后续再补:

- `isPrimary`
- `source`
- `confidence`

但这版先不做。

## 为什么不只用 JSON

一个看起来更轻的做法是:

- 在 `Submission.submissionDetails` 里放 `patternTags: string[]`
- 在 `Question` 本体上也额外挂 `customTags: string[]`

这版明确不这么做，原因是:

1. 很难控制命名漂移
2. 很难限制 tag 维度
3. 很难表达父子层级
4. 很难做全局重命名、停用、合并
5. `Question` metadata 本身是只读的，这种做法和现有边界冲突
6. 前端过滤和聚合可以做，但 taxonomy 本身不会收敛

JSON 仍然可以承载辅助信息，但不应该继续承载 canonical pattern vocabulary。

## 为什么不把 mistake 纳入 pattern tag

这版明确把 `mistake` 排除在受控 taxonomy 之外。

原因:

- `mistake` 往往是 submission-specific，而不是 problem-solving taxonomy 的稳定组成
- 同一类 mistake 的描述往往强依赖上下文，很难在早期就收敛成一套不拧巴的词表
- 现在更重要的是先让“模板 / 思路 / 数据结构”这三层收束

因此:

- 结构化 taxonomy: `template / approach / data_structure`
- 复盘文本: 继续使用 `Submission.mistake`

## 结果

采用这套模型后，系统会同时拥有三种层次:

1. `Question.topicTags`
   - 官方题型和题面主题
2. `SubmissionPatternTag`
   - 这次提交实际采用的受控解法分类

这样前端 submissions table 才能真正支持下面这些查询:

- 我这次提交采用了哪个模板
- 最近刷过的题里，哪些都收敛到同一个 `template`
- 哪些 submission 虽然官方题目 tag 不同，但实际采用了同一个模板

## 当前边界

- 这版 ADR 只定义 pattern taxonomy，不定义完整的 Next.js 页面实现
- 这版不定义 tag editing UI，只定义持久化模型和收敛原则
- 这版不处理自动打 tag，先假设 tags 由人工维护或半自动补全
- 这版不引入新的“mistake taxonomy”
- 这版不引入题目级 `QuestionPatternTag`

## 后续约束

- 如果后续新增 pattern tag 维度，需要单独说明为什么不能继续收敛在现有三维里
- 不要把 `Question.topicTags` 偷偷演化成自定义 pattern tag 的替代品
- 不要往 `Question` 本体新增本地学习系统专用 metadata，除非先推翻“Question 是只读事实源”这个前提
- 不要重新引入 `QuestionPatternTag`，除非先证明 submission 聚合不能满足题目级分类需求
- 不要把自由文本 `thought` / `mistake` 误当成 canonical taxonomy
- 如果前端允许创建 tag，默认必须走受控 vocabulary，而不是任意输入直接落库
- 不允许通过 template generator 自动扩展 `data_structure` tag space；如果确实缺基础结构，需要先显式更新 seed
