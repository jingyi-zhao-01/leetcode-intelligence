# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-score-after-removals-on-a-tree
# source_path: LeetCode-Solutions-master/Python/minimum-score-after-removals-on-a-tree.py
# solution_class: Solution3
# submission_id: 3186da67bd987ddef077aaeb942d756935d503c5
# seed: 1402279104

# Time:  O(n^2)
# Space: O(n)

# dfs with stack

class Solution3(object):
    def minimumScore(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        def dfs(u, p, result):
            total = nums[u]
            for v in adj[u]:
                if v == p:
                    continue
                total ^= dfs(v, u, result)
            result.append(total)
            return total
                
        adj = [[] for _ in xrange(len(nums))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        total = reduce(lambda x, y: x^y, nums)
        result = float("inf")
        for u, v in edges: 
            left = []
            dfs(u, v, left)
            right = []
            dfs(v, u, right)
            for candidates in (left, right):
                total2 = candidates.pop()
                for x in candidates:
                    a, b, c = total^total2, x, total2^x
                    result = min(result, max(a, b, c)-min(a, b, c))
        return result