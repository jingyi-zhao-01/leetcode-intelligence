# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-nodes-with-value-one
# source_path: LeetCode-Solutions-master/Python/number-of-nodes-with-value-one.py
# solution_class: Solution3
# submission_id: fe4463e6d0dae8754599ff3b49ddbd97e17c73d1
# seed: 1366628992

# Time:  O(q + n)
# Space: O(n)

import collections


# bfs

class Solution3(object):
    def numberOfNodes(self, n, queries):
        """
        :type n: int
        :type queries: List[int]
        :rtype: int
        """
        def dfs(u, curr):
            curr ^= cnt[u]%2
            return curr+sum(dfs(v, curr) for v in xrange(2*u, min(2*u+1, n)+1))
    
        cnt = collections.Counter(queries)
        return dfs(1, 0)