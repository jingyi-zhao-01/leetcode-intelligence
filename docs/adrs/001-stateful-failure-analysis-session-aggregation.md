# Stateful Failure Analysis Session Aggregation

日期: 2026-05-27

相关背景: [docs/architecture/README.md](../architecture/README.md)

## 为什么要做

现在 `analyze_failure` 只解决单次失败。

它能告诉我这一次哪里错了，但回答不了这些更有价值的问题:

- 这一整个 session 到底反复暴露了什么问题
- 我是不是一直在犯同一种错
- 这次失败是新问题，还是前面问题换了个表面形式又出现
- 这次 session 暴露的是语法不熟、边界条件不稳，还是调试方式有问题

我想要的不是每次失败都多一条注释，而是 session 结束后能看到一个更像“复盘”的东西。

## 这版先怎么定义

- session 就是一次 `start_timer` 到 `stop_timer`
- 只看当前 session，不做跨 session 长期画像
- 先保持现有 `analyze_failure` 不变，继续给即时反馈
- 新增一层 session 内的 stateful 聚合

这样做的原因很简单: 现在 submission service 本来就是单 active timer、内存态优先，这个 feature 顺着现有模型长出来最自然。

## 核心决策

### 1. 聚合什么

每次 `analyze_failure` 成功后，除了返回当前结果，还要把这次结果挂到当前 session 上。

session 里至少保留两层东西:

1. 原始快照
内容包括 summary、annotations、时间、题目、必要的 submission / testcase 信息。

2. 归一化后的 mistake signals
也就是把单次分析里的描述，整理成更稳定的标签，比如:

- `syntax_fluency`
- `boundary_condition`
- `wrong_api_usage`
- `index_management`
- `debugging_strategy_gap`

这些标签不是给用户直接看的底层实现细节，而是为了后面能聚合“重复问题”。

### 2. 最后产出什么

我希望 session summary 至少能回答下面几件事:

- 这次 session 的主要问题是什么
- 哪几类错误重复出现了
- 为什么这些错误会重复出现
- 有没有 1 到 3 个代表性例子
- 下一次尝试最值得先改什么

不需要一开始就设计得特别重，但输出最好是 structured 的，而不是只有一大段 free text。

一个大概的 shape:

```json
{
  "title_slug": "two-sum",
  "attempt_count": 4,
  "failure_count": 3,
  "session_overview": "This session repeatedly exposed weak Python syntax fluency and unstable boundary handling.",
  "recurring_patterns": [
    {
      "tag": "syntax_fluency",
      "count": 2,
      "evidence": ["invalid loop form", "wrong indexing syntax"]
    }
  ],
  "repeated_error_explanations": [
    {
      "tag": "syntax_fluency",
      "why_it_repeated": "The fixes changed local lines, but the underlying language construct was still not solid."
    }
  ],
  "improvement_actions": [
    "Rewrite the core loop once from memory before retrying.",
    "Check empty-input and final-index cases before submit."
  ]
}
```

字段名后面可以调整，但信息层次大概就这样。

### 3. API 怎么放

现有 `analyze_failure` 不改语义，继续做单次分析。

session 级 summary 单独给一个 action，更清晰一些。

建议:

- `get_session_failure_summary`

我不想把它直接塞进 `get_active_sessions`，因为 timer 信息和复盘信息不是一回事，混在一起后面会越长越乱。

### 4. 状态放哪里

这版先放内存里，直接跟着 active timer 走。

原因:

- 现在 timer 本来就是内存态
- 这版目标是当前 session 复盘，不是长期学习画像
- 先把 summary shape 跑顺，比一开始上数据库更重要

所以这版不强依赖持久化。

如果以后这个输出稳定了，再考虑:

- 只持久化最终 session summary
- 或者再单独设计 failure history 表

### 5. 为什么不直接复用 `Submission.mistake`

因为它太弱了，只是一个 string。

它可以勉强塞一句总结，但表达不了:

- 多次 attempt 的证据
- 重复出现的 pattern
- 哪些错误是新出现，哪些是重复出现
- 代表性例子和结构化 next actions

所以它不适合做这件事的主数据结构。

## 实现方向

我倾向于这样拆:

- `timer.ts`: 扩展 session state，让它顺手带着 failure aggregation state
- 新增一个聚合模块，比如 `failureAggregation.ts`
- `failureAnalysis.ts` / `staticAnalysis.ts`: 继续只负责单次分析，不承担 session state
- `server.ts`: 在 `analyze_failure` 成功后把结果 append 到当前 session，同时暴露 `get_session_failure_summary`

summary 的生成方式也尽量简单一点:

- 每次 `analyze_failure` 后更新轻量的 normalized signals
- 真正要看 session summary 时，再按当前 state 生成最终总结

这样不会每次失败都做一遍完整的 session 级总结。

## 这版先不做什么

- 不做跨 session learner profile
- 不回填历史 submissions
- 不为了这个 feature 先上新表
- 不改现有单次 failure analysis parser 的约束
- 不追求特别“聪明”的教学诊断，先把重复错误归纳清楚

## 验收标准

做到下面这些，我觉得这版就算成立:

1. `start_timer` 后会创建新的 failure aggregation state。
2. 一个 session 里多次 `analyze_failure` 会不断累积证据。
3. 可以通过 `get_session_failure_summary` 拿到结构化复盘结果。
4. 结果里至少有 recurring patterns、为什么重复、以及 next actions。
5. `stop_timer` / `drop_timer` / 进程重启后，这些 state 会清空。
6. 现有依赖 `analyze_failure` 的地方不用跟着重写。

## 实现时要重点测什么

- session 生命周期对不对: start / stop / drop / restart
- 同类错误是否真的会被聚到一起
- test submission 要不要排除，至少这版默认应该排除
- 没有 active session 或 evidence 太少时，summary 返回是不是足够自然

一个基本手工流程就是:

1. `start_timer`
2. 连续做几次失败分析
3. `get_session_failure_summary`
4. 看 summary 能不能正确说出“重复犯错”的模式
5. `stop_timer`
6. 再次查询时确认状态已经清掉

## 后续可能会做

- 把最终 session summary 持久化
- 在 client 上做一个轻量 preview
- 以后再把多个 session 串起来，做长期学习画像
