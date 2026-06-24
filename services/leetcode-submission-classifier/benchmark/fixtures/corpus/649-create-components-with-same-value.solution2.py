# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: create-components-with-same-value
# source_path: LeetCode-Solutions-master/Python/create-components-with-same-value.py
# solution_class: Solution2
# submission_id: 22c386769363849687667922c1bfc41d60ce2ef1
# seed: 3573638936

# Time:  O(n * sqrt(n))
# Space: O(n)

# bfs, greedy

class Solution2(object):
    def componentValue(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        def iter_dfs(target):
            total = nums[:]
            stk = [(1, (0, -1))]
            while stk:
                step, (u, p) = stk.pop()
                if step == 1:
                    stk.append((2, (u, p)))
                    for v in adj[u]:
                        if v == p:
                            continue
                        stk.append((1, (v, u)))
                elif step == 2:
                    for v in adj[u]:
                        if v == p:
                            continue
                        total[u] += total[v]
                    if total[u] == target:
                        total[u] = 0
            return total[0]

        result = 0
        adj = [[] for _ in xrange(len(nums))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        total = sum(nums)
        for cnt in reversed(xrange(2, len(nums)+1)):
            if total%cnt == 0 and iter_dfs(total//cnt) == 0:
                return cnt-1
        return 0