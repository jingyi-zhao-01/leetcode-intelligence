# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: create-components-with-same-value
# source_path: LeetCode-Solutions-master/Python/create-components-with-same-value.py
# solution_class: Solution3
# submission_id: aba79ab4f40077f93941ee28d17cf0b81e4ce85f
# seed: 2132195813

# Time:  O(n * sqrt(n))
# Space: O(n)

# bfs, greedy

class Solution3(object):
    def componentValue(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        def dfs(u, p, target):
            total = nums[u]
            for v in adj[u]:
                if v == p:
                    continue
                total += dfs(v, u, target)
            return total if total != target else 0

        result = 0
        adj = [[] for _ in xrange(len(nums))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        total = sum(nums)
        for cnt in reversed(xrange(2, len(nums)+1)):
            if total%cnt == 0 and dfs(0, -1, total//cnt) == 0:
                return cnt-1
        return 0