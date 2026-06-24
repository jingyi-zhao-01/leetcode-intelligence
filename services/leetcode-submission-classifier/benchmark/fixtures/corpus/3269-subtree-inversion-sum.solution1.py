# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subtree-inversion-sum
# source_path: LeetCode-Solutions-master/Python/subtree-inversion-sum.py
# solution_class: Solution
# submission_id: 095909eb3147e441fd0a4c3da9a9267492d788ef
# seed: 486959971

# Time:  O(n)
# Space: O(n)

# iterative dfs, tree dp

class Solution(object):
    def subtreeInversionSum(self, edges, nums, k):
        """
        :type edges: List[List[int]]
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def iter_dfs():
            dp = []
            ret = [0]*3
            stk = [(1, (0, -1, ret))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, p, ret = args
                    dp.append([0]*2)
                    ret[:] = [nums[u], 0, 0]
                    stk.append((4, (u, p, ret)))
                    stk.append((2, (u, p, ret, 0)))
                elif step == 2:
                    u, p, ret, i = args
                    if i == len(adj[u]):
                        continue
                    v = adj[u][i]
                    stk.append((2, (u, p, ret, i+1)))
                    if v == p:
                        continue
                    new_ret = [0]*3
                    stk.append((3, (u, p, new_ret, ret, i)))
                    stk.append((1, (v, u, new_ret)))
                elif step == 3:
                    u, p, new_ret, ret, i = args
                    ret[0] += new_ret[0]
                    ret[1] += new_ret[1]
                    ret[2] += new_ret[2]
                elif step == 4:
                    u, p, ret = args
                    ret[1] = max(ret[1], dp[-1][1]-2*ret[0])
                    ret[2] = max(ret[2], dp[-1][0]+2*ret[0])
                    dp.pop()
                    if len(dp)-k >= 0:
                        dp[len(dp)-k][0] += ret[1]
                        dp[len(dp)-k][1] += ret[2]
            return ret[0]+ret[1]

        adj = [[] for _ in xrange(len(nums))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return iter_dfs()