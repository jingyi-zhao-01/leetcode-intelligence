# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-special-path
# source_path: LeetCode-Solutions-master/Python/longest-special-path.py
# solution_class: Solution
# submission_id: fcaec6132f318ebd35049c5f71a0c8191f7ee329
# seed: 2136828227

# Time:  O(n + e)
# Space: O(n + e)

import collections


# iterative dfs, two pointers, sliding window, prefix sum

class Solution(object):
    def longestSpecialPath(self, edges, nums):
        """
        :type edges: List[List[int]]
        :type nums: List[int]
        :rtype: List[int]
        """
        def iter_dfs():
            result = [float("inf")]*2
            lookup = collections.defaultdict(lambda: -1)
            prefix = [0]
            stk = [(1, (0, -1, 0, -1))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, p, d, left = args
                    prev_d, lookup[nums[u]-1] = lookup[nums[u]-1], d
                    left = max(left, prev_d)
                    result = min(result, [-(prefix[(d-1)+1]-prefix[left+1]), d-left])
                    stk.append((4, (u, prev_d)))
                    stk.append((2, (u, p, d, left, 0)))
                elif step == 2:
                    u, p, d, left, i = args
                    if i == len(adj[u]):
                        continue
                    stk.append((2, (u, p, d, left, i+1)))
                    v, l = adj[u][i]
                    if v == p:
                        continue
                    prefix.append(prefix[-1]+l)
                    stk.append((3, None))
                    stk.append((1, (v, u, d+1, left)))
                elif step == 3:
                    prefix.pop()
                elif step == 4:
                    u, prev_d = args
                    lookup[nums[u]-1] = prev_d
            return [-result[0], result[1]]
    
        adj = [[] for _ in xrange(len(nums))]
        for u, v, l in edges:
            adj[u].append((v, l))
            adj[v].append((u, l))        
        return iter_dfs()