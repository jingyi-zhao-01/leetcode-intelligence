# Mem0 Session Snapshot Persistence

日期: 2026-06-07

相关背景:

- [002-session-bound-companion-memory-and-failure-events.md](./002-session-bound-companion-memory-and-failure-events.md)
- [services/leetcode-submission-service/ARCHITECTURE.md](../../services/leetcode-submission-service/ARCHITECTURE.md)

## 背景

`leetcode-submission-service` 已经把当前 solve lifecycle 的上下文统一收敛到 `src/session/` 里的 active in-memory scope。

这解决了当前 session 内的上下文一致性问题，但有一个明显边界:

- session 一结束，当前 agent memory 会被清空
- 之前的失败结果、static analysis、companion 对话不会留下服务端外部记录
- 之后如果要做跨 session recall、训练数据回放、外部 memory search，就没有统一出口

这次需求不是把 active session 搬到外部，而是:

> 每个 LeetCode session 结束时，把这一段 session record persist 到 Mem0。

## 决策

### 1. active session source of truth 仍然留在 submission server 内存里

Mem0 不是当前 solve lifecycle 的实时上下文来源。

当前实时上下文仍然由 submission server 的 in-memory session scope 持有，继续服务于:

- companion chat
- static analysis
- failure analysis
- failure event rendering

也就是说:

- 当前 session 的读写: 走 `src/session/scope.ts`
- session 结束后的归档: 走 Mem0

### 2. 只在 session end lifecycle 上做 snapshot persistence

Mem0 写入发生在 session 结束时，而不是每次聊天或每次 failure 都直接同步外部写入。

当前结束点包括:

- `stop_timer`
- `drop_timer`
- `Accepted` 后的 timer restart
- 被新的 active session 挤掉时的 eviction
- 服务进程退出时的 shutdown flush

这样可以保证:

- request path 仍然轻
- current session memory 不依赖外部可用性
- 每个 solve lifecycle 都有一个完整的结束快照

### 3. Mem0 用 session-scoped ids 保存记录，但运维侧只需要提供 API key

每次 session snapshot 持久化时，提交给 Mem0 的顶层实体 id 至少包含:

- `user_id`
- `agent_id`
- `app_id`
- `run_id`

其中 `run_id` 当前格式为:

```text
leetcode-session:<titleSlug>:<activatedAt>
```

这样同一个用户下，不同 session 会自然分开。

这些 id 由 submission service 内部自动推导:

- `user_id`: 默认取当前 OS username
- `agent_id`: 默认取 `leetcode-submission-service`
- `app_id`: 默认取 `leetcode-qa`

因此当前接入 Mem0 时，运维侧只需要配置:

```text
MEM0_API_KEY
```

### 4. 当前使用 raw snapshot 模式，而不是让 Mem0 重新概括

这次持久化的目标是“保留 session record”，而不是只抽象出少量长期偏好。

因此当前实现使用:

```text
infer: false
```

并把完整但截断过的 session snapshot 作为一条消息写入 Mem0。

snapshot 至少包含:

- 题目元数据
- 当前 editor code / 提交代码
- testcase
- 最新 LeetCode failure
- static analysis summary / annotations
- service session memory
- companion conversation
- session end reason / elapsed minutes

### 5. Mem0 持久化失败不能阻塞本地 session cleanup

如果 Mem0 调用失败:

- 服务端仍然会结束当前 session
- 当前 agent memory 仍然会被清空
- 失败只进入日志，不回滚本地 lifecycle

这保证 active session cleanup 的行为不会依赖外部 memory provider。

## 为什么这么做

### 不把 Mem0 变成实时上下文源

当前 companion / failure 流需要的是强一致、低延迟、服务端本地可控的 session scope。

如果直接让 Mem0 成为 active context source，就会重新引入:

- 网络依赖
- eventual consistency
- 生命周期 ownership 混乱

### 不在每个事件上立即写外部 memory

因为 failure analysis、companion turn、editor context 本来就高频变化。

把 Mem0 放在 session end snapshot 上，能保留完整记录，同时避免把运行时设计成一条外部写放大的链。

## 结果

当前服务端形成两层 memory:

1. in-memory active session scope
   - 当前 solve lifecycle source of truth
   - 供 companion/static/failure 实时使用
2. Mem0 session snapshot
   - session 结束后异步归档
   - 供未来 recall / audit / cross-session intelligence 使用

### 6. companion 打开当前题目时，按 `title_slug` recall 这道题的历史 session records

当新的 active session 建立，或者 companion 第一次绑定到当前题目时，服务端可以按 `title_slug` 从 Mem0 取回这道题之前结束过的 session records。

这里的 retrieval 约束是:

- retrieval 仍然是服务端行为，不下放到 `leetcode.nvim`
- 只把 recall 结果当成补充上下文，不替代当前 active session scope
- recall 范围按当前用户 + service ids + `title_slug` 过滤，避免混入别的题目

这样 companion 在刚打开一题时，就能先看到:

- 之前这道题经历过哪些 session
- 每次 session 大致如何结束
- 之前出现过哪些 failure/status
- 这道题之前积累过哪些有价值的 solve context

## 当前边界

- 当前 recall 只按 `title_slug` 拉 session-level records，还不是更细粒度的 event replay
- 当前 snapshot 是按 session end 粒度写入，不是 event sourcing
- 当前仍然没有本地持久化的 session replay 表

## 后续约束

- 新增外部 memory/retrieval 时，不能破坏“active session scope 仍然在 submission server 内存里”这个前提
- Mem0 recall 必须作为补充上下文，而不是替代当前 session scope
- 如果以后需要更细粒度事件流，再单独设计 event persistence，不要偷偷改变 session snapshot 的职责
