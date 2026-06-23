# Current UI Requirements

这份文档只记录 `leetcode.nvim` 这个 fork 当前已经落地的 UI / 产品功能。
不是 roadmap，也不是未来设计稿；后面如果 UI 行为变了，再直接改这里。

## 1. Product Goal

- 在 Neovim 里完成 LeetCode 题目浏览、做题、运行、提交和结果回看。
- 把编辑器内做题流程和外部 submission service / CodeCompanion 串起来。
- 尽量让“题目上下文、历史提交、失败记忆、类似题回忆”都留在当前题目的工作区里。

## 2. Main User Flows

### 2.1 Menu / Entry

用户需要能从插件菜单进入这些入口：

- `Problems`: 打开题库列表
- `Random`: 随机打开一题
- `Daily`: 打开每日一题
- `Statistics`: 查看个人统计页
- `Cookie`: 更新或删除登录 cookie
- `Cache`: 手动刷新本地缓存

### 2.2 Question Workspace

打开题目后，UI 需要提供一个题目工作区，至少包括：

- 题目代码 buffer
- 题面 description split
- console 区域，用来编辑 testcase 和看运行结果
- info / hints popup
- 可选 submissions side panel

题目工作区里需要支持这些行为：

- 打开题面
- 在题面里显示题号、标题、链接、是否 Premium
- 显示题目内容
- 可切换是否显示统计信息
- 显示难度、likes / dislikes、通过率
- 有 hints 时给出提示标记
- 可选渲染题面里的图片

### 2.3 Solve Loop

用户在题目页里需要能完成完整做题闭环：

- 运行 / 测试当前代码
- 提交当前代码
- 查看运行结果
- 查看 testcase
- 把最近一次失败返回的 testcase 重新带回 testcase 输入区
- 切换焦点到 testcase pane 或 result pane
- 重置当前题目的代码模板
- 拉取最近一次提交的代码并回填到当前 buffer
- 打开当前题目的 LeetCode 网页

### 2.4 Multi-question / Multi-language

当前 UI 需要支持：

- 切换当前题目的语言模板
- 查看并切换当前已经打开的题目 tab
- 在已有题目 tab 和 description buffer 丢失后恢复视图

## 3. Submission Panel

当 `description.submissions.enabled = true` 时，题面下方需要有一个 side panel。

这个 panel 目前有 3 个 tab：

- `历史提交`
- `历史记忆`
- `类似题`

### 3.1 历史提交

需要展示最近若干次提交 / 测试记录，并至少包含：

- 提交时间
- 是否测试提交
- 提交结果
- 耗时（如果服务端有）

### 3.2 历史记忆

需要展示当前题目的历史 session 回忆信息，并至少包含：

- 历史记录数
- session 结束原因
- 最近 failure status
- distinct mistakes 数量
- failure summary
- stuck points
- thought process

### 3.3 类似题

需要展示历史上可回忆的类似题，并至少包含：

- 题目 slug
- 难度
- 相似度分数（如果服务端有）
- 为什么相似
- failure summary
- stuck points
- thought process

## 4. Stats / Account UI

统计页当前需要提供这些能力：

- 展示 solved / calendar 等个人统计信息
- 查看语言统计
- 查看 skills（非中文环境）
- 手动刷新统计数据

## 5. CodeCompanion Bridge

当前 UI 需要提供 `:Leet companion` 入口，把当前题目的上下文挂到 CodeCompanion chat。

chat 打开时需要注入的上下文至少包括：

- 题目标题 / slug / 难度
- 题面内容
- tags / hints
- 当前 testcase
- 当前编辑器里的代码

bridge 还需要支持：

- 按 `title_slug` 绑定当前题目的 chat
- 同一道题新的 failure event 到来时，把 failure context 挂到已有 chat
- 在服务端忘记加 fenced code block 时，尽量自动补 fence 方便高亮

具体 session / failure-event 行为，以 `docs/adrs/001-codecompanion-session-failure-event-bridge.md` 为准。

## 6. Hook-based External Integration

当前 fork 的产品范围不只是本地 UI，还包括把关键做题事件暴露成 hooks，方便外部服务接管持久化。

当前需要保留的 hook 入口：

- `problem_description_open`
- `timer_start`
- `timer_stop`
- `question_leave`
- `on_test_result`
- `upload_test_result`
- `upload_submit_result`

这些 hooks 需要允许外部集成做的事包括：

- 启动 / 停止题目 session timer
- 保存 test / submit 结果
- 拉取历史提交
- 拉取历史记忆和类似题摘要
- 在题目关闭时做清理

## 7. UX Expectations

当前 UI 应该保持这些体验特征：

- 题目上下文尽量围绕“当前题”聚合，而不是散到多个无关窗口
- 历史提交、历史记忆、类似题尽量直接贴着题面展示
- 外部服务不可用时，UI 要给出明确但轻量的错误提示
- 不把 provider / model ownership 放进这个 repo；这里仍然只是 UI 和 context bridge

## 8. Non-goals

当前 UI 不负责：

- 自己实现 LLM provider 管理
- 自己维护 submission memory 的最终真相
- 把服务端分析逻辑搬回 Lua 侧重建一遍
