# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-special-path-ii
# source_path: LeetCode-Solutions-master/Python/longest-special-path-ii.py
# solution_class: Solution2
# submission_id: d1469b42e291f792506b3e52dd594fbdba999e25
# seed: 694366949

# Time:  O(n + e)
# Space: O(n + e)

import collections


# iterative dfs, two pointers, sliding window, prefix sum

class Solution2(object):
    def longestSpecialPath(self, edges, nums):
        """
        :type edges: List[List[int]]
        :type nums: List[int]
        :rtype: List[int]
        """
        def dfs(u, p, d, left):
            prev_d, lookup[nums[u]-1] = lookup[nums[u]-1], d
            new_left = left[:]
            curr = prev_d
            for i in xrange(len(new_left)):
                if curr > new_left[i]:
                    curr, new_left[i] = new_left[i], curr
            result[0] = min(result[0], [-(prefix[(d-1)+1]-prefix[new_left[1]+1]), d-new_left[1]])
            for v, l in adj[u]:
                if v == p:
                    continue
                prefix.append(prefix[-1]+l)
                dfs(v, u, d+1, new_left)
                prefix.pop()
            lookup[nums[u]-1] = prev_d
    
        adj = [[] for _ in xrange(len(nums))]
        for u, v, l in edges:
            adj[u].append((v, l))
            adj[v].append((u, l))
        lookup = collections.defaultdict(lambda: -1)
        prefix = [0]
        result = [[float("inf"), float("inf")]]
        dfs(0, -1, 0, [-1]*2)
        return [-result[0][0], result[0][1]]