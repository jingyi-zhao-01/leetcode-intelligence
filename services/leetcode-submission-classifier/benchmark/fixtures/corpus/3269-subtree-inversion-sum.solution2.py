# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subtree-inversion-sum
# source_path: LeetCode-Solutions-master/Python/subtree-inversion-sum.py
# solution_class: Solution2
# submission_id: 82f9af4e987706cf19826e3132a3981b87907a0e
# seed: 2789777142

# Time:  O(n)
# Space: O(n)

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
            dp.append([0]*2)
            total, pos, neg = nums[u], 0, 0
            for v in adj[u]:
                if v == p:
                    continue
                new_total, new_pos, new_neg = dfs(v, u)
                total += new_total
                pos += new_pos
                neg += new_neg
            pos = max(pos, dp[-1][1]-2*total)
            neg = max(neg, dp[-1][0]+2*total)
            dp.pop()
            if len(dp)-k >= 0:
                dp[len(dp)-k][0] += pos
                dp[len(dp)-k][1] += neg
            return total, pos, neg

        adj = [[] for _ in xrange(len(nums))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dp = []
        total, pos, neg = dfs(0, -1)
        return total+pos