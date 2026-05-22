产品需求文档（PRD） LeetCode Recall Engine（LRE）
一个面向技术面试的「算法记忆管理系统」

1. 产品背景
目前大部分工程师准备算法面试的流程如下：

刷题 ↓ 看题解 ↓ AC ↓ 继续下一题 ↓ 一个月后忘记 ↓ 面试再次遇到 ↓ 做不出来
最终问题不是：

刷题数量不够

而是：

已经刷过的题无法稳定回忆出来

对于有几年工作经验的工程师来说：

刷过 300~500 题
理解过大部分经典套路
知道 BFS、DFS、DP、Heap
真正的问题是：

知识存储在大脑里 ↓ 没有复习机制 ↓ 快速遗忘 ↓ 面试无法提取
因此需要一个系统：

持续监控知识遗忘情况，并自动安排复习计划。

2. 产品愿景
打造一个类似 Anki 的算法学习系统。

目标不是：

刷更多题
而是：

记住已经刷过的题
帮助用户建立：

长期记忆
Pattern Recognition
面试 Recall 能力
3. 核心目标 G1
降低遗忘率

G2
提升套路识别速度

G3
提高面试通过率

G4
减少重复刷题时间

4. 产品原则 Principle 1
Recall 优于 AC

用户不需要重新写代码，只需要证明：

看到题目 ↓ 能够快速说出解法
即可。

Principle 2
Pattern 优于 Problem

目标不是记住题目，而是记住：

Graph Heap DP Sliding Window
等核心模式。

Principle 3
遗忘驱动学习

不会根据：

多久没刷
决定复习，而是根据：

忘得有多严重
决定复习频率。

5. 用户画像 Persona A：在职跳槽工程师
特征：

3~10 年经验
正在准备大厂面试
已刷题 200+ 以上
痛点：

刷过很多题 ↓ 记不住 Persona B：重返面试市场工程师
特征：

以前刷过很多题 ↓ 几年没面试
痛点：

不知道从哪里开始复习 6. 产品架构 题库 ↓ Pattern 分类 ↓ Recall Engine ↓ Review Scheduler ↓ Weakness Analyzer ↓ Topic Recommendation 7. 核心概念 Problem（题目）
例如：

207 Course Schedule Pattern（模式）
例如：

Graph Topological Sort Cluster（知识簇）
例如：

Graph Cluster 包含： 207 210 269 802 Recall（回忆）
用户看到题目后，不写代码，只需要回答：

属于什么套路 核心数据结构是什么 时间复杂度是什么 为什么这样做 8. Recall 评分系统 5 分
秒出，30 秒内能讲清楚。

4 分
能做出来，但有些细节需要思考。

3 分
记得大方向，实现细节模糊。

2 分
需要提示。

1 分
看答案才能想起来。

0 分
完全忘记。

9. 数据模型 Problem Problem { id title difficulty patterns companyTags frequencyScore lastSolvedAt lastReviewedAt recallScore weight nextReviewAt } Review History Review { problemId reviewedAt recallScore note } Cluster Cluster { name masteryScore failRate priorityScore } 10. Daily Review Engine
每天自动生成：

10~15 道题
组成：

50%
遗忘题：

Recall <= 2 30%
高频面试题：

Google Top 100 Meta Top 100 20%
弱项 Cluster：

DP Graph
示例：

今日任务 8 道遗忘题 4 道高频题 3 道弱项题 11. 权重更新算法 Recall >= 4
说明掌握较好：

降低权重 延长复习间隔
例如：

7天 ↓ 14天 ↓ 28天 Recall == 3
保持当前频率。

Recall <= 2
大幅提高权重：

明天再次出现 12. Cluster 分析引擎
系统维护：

Graph DP Heap Binary Search Sliding Window Backtracking Tree Union Find
等 Cluster。

每个 Cluster 计算：

平均 Recall
例如：

Graph 4.2 遗忘率
例如：

DP 42% 最近复习时间
例如：

Heap 14 天未复习 13. Weekly Review
每周生成一次：

Top Weak Clusters 1. Dynamic Programming 2. Topological Sort 3. Binary Search Top Forgotten Problems 72 Edit Distance 239 Sliding Window Maximum 269 Alien Dictionary 推荐学习主题
例如：

本周重点： Graph 系列 原因： Google 高频 遗忘率高 最近两周 Recall 不佳 14. 公司定制模式 Google Mode
重点：

Graph DP Tree Binary Search Meta Mode
重点：

Array HashMap Tree Graph TikTok Mode
重点：

Heap Interval Binary Search Graph Amazon Mode
重点：

Graph Greedy Heap Sliding Window 15. 面试准备指数
Interview Readiness Score

范围：

0~100
组成：

40%
Recall 能力

30%
Pattern 覆盖率

20%
高频题掌握度

10%
学习连续性

输出：

Google Readiness 87/100 16. Dashboard 首页
显示：

Interview Readiness 今日任务 弱项分析 最近进步趋势 Pattern 页面
显示：

Graph 掌握度：83% 遗忘率：12% 推荐题目： ... Problem 页面
显示：

题目 Pattern 历史 Recall 下次复习时间 17. MVP 范围
第一版实现：

支持
SQLite
Problem 管理
Recall 打分
Daily Queue
Weekly Topic Recommendation
Readiness Score
不支持
在线判题
AI 自动讲题
多人协作
手机 App
18. Phase 2
知识图谱。

例如：

BFS ↓ Topological Sort ↓ Course Schedule
识别：

一个知识点没掌握 会影响哪些题 19. Phase 3
AI 面试官。

自动追问：

为什么用 BFS 为什么不用 DFS 复杂度是多少 还能优化吗 20. 最终目标
用户不再追求：

刷了多少题
而追求：

高频题能否快速回忆 套路是否形成长期记忆 是否达到目标公司的面试水平
最终达到：

用最少时间维持最高面试战斗力

Phase 0：题目导入器
LeetCode History Import

LeetCode History Import ↓ 自动识别历史刷题记录 ↓ 自动打 Pattern Tag ↓ 自动生成初始权重
这样用户不用手工录入 300~500 道历史题目，而是直接开始 Recall Pipeline。