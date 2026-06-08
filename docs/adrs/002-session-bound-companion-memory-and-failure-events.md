# Session-Bound Companion Memory And Failure Events

日期: 2026-06-07

相关背景:

- [001-stateful-failure-analysis-session-aggregation.md](./001-stateful-failure-analysis-session-aggregation.md)
- [services/leetcode-submission-service/ARCHITECTURE.md](../../services/leetcode-submission-service/ARCHITECTURE.md)

## 背景

`leetcode-submission-service` 现在同时承担三类和 LLM 相关的行为:

- `analyze_failure`
- `static analysis`
- 本地 OpenAI-compatible companion chat endpoint

如果这些 flow 各自维护上下文，就会出现两个问题:

1. companion chat 看不到刚刚那次失败和分析结果
2. failure analysis 给出的“最新事实”会被旧的聊天结论覆盖

这在实际调试里已经出现过: `analyze_failure` 已经拿到了新的 `Wrong Answer` 和新的代码快照，但 companion 仍然根据旧 assistant reply 继续回答。

## 决策

### 1. active solve session 由 submission server 单独拥有

真正的 active session 不在 `leetcode.nvim`，而在 submission server。

具体做法:

- 保持 `TimerManager` 作为 solve lifecycle 的单活事实来源
- 在 `src/session/` 下维护和 active session 同生命周期的 in-memory scope
- `start_timer / stop_timer / drop_timer` 决定这份 scope 的创建、切换和清理

### 2. 所有 LLM-based flow 共用同一个 session scope

`companion chat`、`failure analysis`、`static analysis` 都绑定到同一个 active session scope。

当前 scope 至少包含:

- 问题元数据和题面上下文
- 当前 editor code / testcase / filetype
- `companionMemory`
- `latestFailure`
- `lastFailureAnalysis`
- `sessionMemory`

这里的 `sessionMemory` 是服务端维护的 lifecycle memory，不是用户直接输入的聊天历史。

### 3. `analyze_failure` 完成后必须写入最新 failure snapshot

每次 `analyze_failure` 成功后，服务端除了返回即时分析结果，还要把这次失败的“最新快照”写进 session memory。

这条 snapshot 至少包含:

- `event_id`
- `title_slug`
- 最新 `judgeResult`
- 最新 `testcase`
- 最新 static analysis summary
- annotations
- 一个明确语义: 这次 failure update 覆盖当前 failed run 的旧诊断

这样 companion 再次请求时，总能先看到最新失败事实，而不是只看到旧对话。

### 4. companion request 总是先注入 active scope 和 session memory

服务端在构造 companion request 时，不直接把客户端发来的消息原样透传。

而是统一组装成:

1. `Submission Service Active Session`
2. 最新 `sessionMemory` snapshots
3. 用户可见对话历史 `companionMemory`

这样 companion 每次都绑定到服务端 session，而不是只绑定到 chat buffer 自己的历史。

### 5. 每次 failure 生成稳定 `event_id`

`analyze_failure` 每次成功后都会生成一个稳定的 `event_id`，当前实现使用:

```text
failure_<uuid>
```

这个 id 有两个用途:

- 服务端 session scope 内部标识这次 failure update
- 作为客户端把最新 failure event 渲染进当前 companion chat 的桥接键

## 为什么这么做

### 不把 ownership 放在 nvim 侧

因为是否存在 active solve session、哪次 failure 才是“最新事实”、当前 LLM scope 应该包含什么，这些都属于 submission runtime 的职责。

客户端只应该做:

- 上下文桥接
- 渲染
- hook 调度

而不是决定 session truth。

### 不只靠旧聊天记录

仅仅 replay 旧 user/assistant turns 不足以表达 solve lifecycle 中刚刚发生的新 failure。

failure 是一种结构化事件，不只是自然语言对话的一部分。

所以它必须被服务端作为 session memory 显式写入。

## 结果

当前 submission service 形成了下面这条链:

1. `start_timer` 激活 active session
2. companion chat 读取同一个 active session scope
3. `analyze_failure` 完成后写入:
   - `latestFailure`
   - `lastFailureAnalysis`
   - 一条带 `event_id` 的 `sessionMemory` snapshot
4. 后续 companion 请求会自动携带最新 failure snapshot

## 当前边界

- 这些 session / memory 目前只保存在内存里
- 还没有持久化到数据库
- 还没有提供单独的 session summary action
- 还没有做跨 session learner profile

## 后续约束

- 新增任何 LLM-based flow 时，默认接入 `src/session/` scope，而不是各自维护上下文
- 如果客户端需要渲染新的 failure-aware UI，优先复用服务端返回的 `event_id`
- 如果将来做持久化，不要破坏“active session scope 是当前 solve lifecycle source of truth”这个约束
