# Mem0 Recall Lifecycle And Hydration

日期: 2026-06-07

相关背景:

- [003-mem0-session-snapshot-persistence.md](./003-mem0-session-snapshot-persistence.md)
- [002-session-bound-companion-memory-and-failure-events.md](./002-session-bound-companion-memory-and-failure-events.md)
- [services/leetcode-submission-service/ARCHITECTURE.md](../../services/leetcode-submission-service/ARCHITECTURE.md)

## 背景

`003` 已经确定了:

- active session source of truth 留在 submission server 内存里
- session 结束时异步把 snapshot persist 到 Mem0

但在真正把 Mem0 用作题目级历史 recall 时，还需要把下面这些行为说清楚:

- 什么时候 persist
- 什么时候 recall
- recall 用什么过滤条件
- recall 回来以后怎样进入当前 active session
- companion prompt 里应该看到什么，不应该看到什么

如果这些点没有单独定义，后续 agent 很容易犯几类错:

1. 把 Mem0 当成 active session source of truth
2. 用错误的 metadata key 过滤，导致 recall 结果为空
3. 把完整 raw snapshot 重新塞进 companion prompt，造成 prompt 膨胀和误导性推断
4. 把 recall 结果和当前 active session 混为一谈

## 决策

### 1. lifecycle 分成六段: activate, persist, recall, cache, hydrate, mount-hint

`Mem0` 只参与 active session 外围的归档和题目历史补充，不参与实时写时上下文。

完整生命周期如下:

1. `activate`
   - `start_timer` 或 accepted restart 激活新的 active session scope
   - 当前 solve lifecycle 的实时上下文只写入 `src/session/scope.ts`
2. `persist`
   - 当前 session 结束时，把 scope 渲染成一条 `LeetCode Session Record`
   - 异步写入 Mem0
3. `recall`
   - 当前题目的 companion 请求进入时，如果当前 active session 还没有做过 Mem0 hydrate，就按 `title_slug` recall 历史 ended sessions
4. `cache`
   - recall 结果先进入 submission service 进程内的短 TTL cache
   - `start_timer` 预热、companion hydrate、on-mount summary 共用这份 cache
   - 同一题目的并发 recall 只保留一个 in-flight promise
5. `hydrate`
   - recall 结果被整理成一条服务端隐藏消息，写回当前 active session 的 `mem0Recall`
   - 之后 companion prompt 组装时自动注入
6. `mount-hint`
   - 题目重新打开时，客户端可以向 submission service 请求一份短摘要
   - 这份摘要面向 UI 提示，不等同于 companion prompt 注入内容

### 2. persist 只发生在 session end path

当前 Mem0 snapshot persistence 的触发点包括:

- `stop_timer`
- `drop_timer`
- accepted 后 restart 之前对旧 session 的结束
- 被新的 active session 挤掉时的 eviction
- 进程 shutdown 时的 flush

行为约束:

- 每个 ended session 最多 persist 一次
- persist 失败不能阻塞本地 session cleanup
- persist 只吃已经完成的 scope snapshot，不回头再读 Mem0

### 3. recall 永远按题目 slug 取这道题的 ended sessions

recall 是 submission service 的服务端行为，不在 `leetcode.nvim` 里做。

当前过滤约束是:

- `user_id`
- `agent_id`
- `app_id`
- `metadata.record_type = leetcode_session_record`
- `metadata.title_slug = 当前题目的 slug`

其中最重要的实现约束是:

- 过滤 metadata 时使用 snake_case key
- 当前依赖 Mem0 返回的 metadata 规范化结果，而不是本地 camelCase 命名

也就是说，当前 recall 的关键 metadata key 是:

```text
record_type
title_slug
activated_at
ended_at
end_reason
elapsed_minutes
latest_failure_status
```

而不是:

```text
recordType
titleSlug
activatedAt
endedAt
endReason
elapsedMinutes
latestFailureStatus
```

### 4. hydrate 结果属于当前 active session，而不是全局记忆

recall 完成后，服务端不会把结果直接透传给客户端，也不会把 Mem0 结果当成新的 source of truth。

而是:

- 用 `renderRecalledSessionRecords()` 把多条历史 session record 整理成一条隐藏 companion message
- 把这条 message 存到当前 active scope 的 `mem0Recall`
- 标记当前题目在这次 active session 内已经 hydrate 过

这样做的约束是:

- 同一个 active session 内，对同一个 `title_slug` 只 hydrate 一次，除非 session 被清空后重新开始
- hydrate 结果只作为当前题目的补充历史上下文
- active session 清空时，hydrate state 也一起清空

### 5. recall 结果需要一个独立于 active scope 的进程级 cache

只把 `mem0Recall` 挂在当前 active scope 上还不够，因为这只能避免“同一个 session 内”的重复 retrieval。

如果出现下面这些情况:

- 题目重新打开，旧 scope 已经结束
- 先请求了 on-mount summary，后面又打开 companion
- `start_timer` 预热和第一条 companion 请求撞在一起

单纯依赖 active scope 仍然会重复打 Mem0 retrieval。

因此当前增加一层 submission-service 进程内 cache，约束如下:

- key 仍然按当前 service 身份下的 `title_slug`
- cache 同时缓存:
  - 有结果的 recall
  - `record_count = 0` 的 negative result
- cache 带短 TTL，默认面向“当前编辑会话内复用”，不是长期 source of truth
- 同一个题目的并发 recall 共用一个 promise，避免预热和真正请求同时计费

这层 cache 的职责只是减少 retrieval 次数，不改变当前事实优先级。

### 6. 新写入的 session snapshot 要回填到本地 recall cache

如果一次 `failure_analysis` 或 session end 刚刚成功 persist 了一条新 snapshot，但当前进程已经缓存过这道题的 recall 结果，那么不能继续让 cache 停留在旧状态。

当前约束是:

- persist 成功后，服务端会把刚刚 render 出来的那条 `LeetCode Session Record` 合并进本地 recall cache
- 这条回填记录沿用 session snapshot 的渲染格式和 snake_case metadata
- 这样后续:
  - 同进程内重新打开题目
  - 再请求 on-mount summary
  - 再发 companion 请求

都可以直接看到最新一次 failure/session snapshot，而不用立刻再打一次 Mem0 retrieval

这里的重点是“回填本地 recall cache”，不是把 Mem0 升级成实时上下文源。

### 7. 题目 on-mount 提示复用同一份服务端 recall，不在客户端重建语义

当前新增一个独立 action，用于题目重新打开时取回简短历史提示。

这条链路的约束是:

- `leetcode.nvim` 只负责显示，不负责自己解析 Mem0 raw records
- “之前错在哪里 / 卡在哪里 / 当时怎么想” 仍由 submission service 从 recalled records 里提取
- mount 提示和 companion hidden context 都来自同一次服务端 recall 结果，只是渲染视图不同

### 8. companion prompt 总是把 recall 当作历史摘要，而不是实时事实

当前 companion prompt 组装顺序是:

1. `Submission Service Active Session`
2. `Submission Service Mem0 Recall`
3. 当前 session 的 `sessionMemory`
4. 当前 chat 的 `companionMemory`

其中 `Mem0 Recall` 的职责是:

- 告诉 companion 这道题之前经历过多少次 ended session
- 提供每次 session 的时间、结束原因、最近 failure status
- 提供一小段可控长度的历史代码摘录

`Mem0 Recall` 不应该做的事:

- 取代当前 active session scope
- 重新注入完整 raw snapshot
- 把历史截断文本伪装成当前确定事实
- 把历史题面/长代码/整段对话全部 replay 回 prompt

因此当前 recall 渲染策略是:

- 保留结构化 session-level 摘要
- 保留 `Recalled Code Excerpt`
  - 优先取 `Last Submitted Code`
  - 没有时退回 `Final Editor Code`
- 不再把完整 `Session Snapshot` 原样放进 companion prompt

### 9. recall 和当前 active session 的职责边界必须保持清楚

当前 active session scope 仍然保存:

- 当前题面
- 当前 editor code
- 当前 testcase
- 最新 failure
- 最新 static analysis
- 当前 companion 对话

Mem0 recall 只补充:

- 过去这道题发生过什么
- 历史 ended sessions 中保留下来的有限证据

如果当前事实和历史 recall 冲突，优先级永远是:

1. 当前 active session scope
2. 当前 session memory / latest failure snapshot
3. Mem0 recall
4. 旧 companion 对话

## 为什么这么做

### 不让 Mem0 接管实时上下文

因为实时 solve lifecycle 需要:

- 单活
- 低延迟
- 明确 ownership
- 可控 cleanup

这些都应该继续由 submission service 的 in-memory scope 负责。

### 不把 recall 变成 raw snapshot replay

因为完整 raw snapshot 虽然信息多，但在 companion prompt 里有三个明显副作用:

1. prompt 变长
2. 模型容易把截断文本脑补成确定事实
3. 历史代码、题面和旧对话会污染当前问题判断

所以 recall 需要的是“可控摘要 + 小段关键代码”，不是“整段 session dump”。

## 结果

当前 `Mem0` 在 submission service 里的职责已经明确成两层:

1. session end archive
   - session 结束时异步落一条完整 record 到 Mem0
2. title-level historical recall
   - 当前题目第一次 companion 请求时，取回历史 ended sessions
   - recall 结果先进入服务端短 TTL cache
   - hydrate 成一条隐藏服务端消息
   - 注入当前 active session 的 prompt 组装链

## 当前边界

- recall 目前只在 companion 请求前 hydrate，还不是所有动作都会主动触发
- recall 仍然按 `title_slug` 聚合，不区分更细的 event 类型
- 当前没有做多轮动态 re-recall
- 当前没有做历史 session 的自动聚合总结，只是结构化摘要加小段代码摘录
- 进程级 recall cache 只优化本地重复 retrieval，不提供跨进程一致性保证

## 后续约束

- 修改 Mem0 persistence、recall、hydrate、prompt injection 行为时，先读本 ADR 和 `003`
- 不要把 Mem0 recall 直接下放到 `leetcode.nvim`
- 不要把 Mem0 recall 偷偷升级成 active session source of truth
- 如果未来需要更强的跨 session intelligence，单独设计 summary/indexing 机制，不要回退到 raw snapshot replay
