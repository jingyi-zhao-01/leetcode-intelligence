# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subtree-inversion-sum-ii
# source_path: LeetCode-Solutions-master/Python/subtree-inversion-sum-ii.py
# solution_class: Solution2
# submission_id: f359fd4cd0562a91ed45e1a37592bfbc0b439a49
# seed: 3642612919

# Time:  O(n * k)
# Space: O(n + h * k)

# iterative dfs, tree dp

class Solution2(object):
    def subtreeInversionSum(self, edges, nums, k):
        """
        :type edges: List[List[int]]
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def dfs(u, p):
            dp1, dp2 = [nums[u]]*k, [nums[u]]*k
            for v in adj[u]:
                if v == p:
                    continue
                new_dp1, new_dp2 = dfs(v, u)
                for i in xrange(k//2):
                    dp1[i] = max(dp1[i]+new_dp1[(k-2)-i], dp1[(k-2)-i]+new_dp1[i])
                    dp2[i] = min(dp2[i]+new_dp2[(k-2)-i], dp2[(k-2)-i]+new_dp2[i])
                for i in xrange(k//2, k):
                    dp1[i] += new_dp1[i]
                    dp2[i] += new_dp2[i]
                for i in reversed(xrange(k-1)):
                    dp1[i] = max(dp1[i], dp1[i+1])
                    dp2[i] = min(dp2[i], dp2[i+1])
            dp1.insert(0, max(dp1[0], -dp2[-1]))
            dp2.insert(0, min(dp2[0], -dp1[-1]))
            dp1.pop()
            dp2.pop()
            return dp1, dp2

        adj = [[] for _ in xrange(len(nums))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dp1, _ = dfs(0, -1)
        return dp1[0]