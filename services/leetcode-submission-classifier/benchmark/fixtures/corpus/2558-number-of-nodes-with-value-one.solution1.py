# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-nodes-with-value-one
# source_path: LeetCode-Solutions-master/Python/number-of-nodes-with-value-one.py
# solution_class: Solution
# submission_id: 410f0d46b58db73f89615ac82d5ad4e21bd55146
# seed: 1069675526

# Time:  O(q + n)
# Space: O(n)

import collections


# bfs

class Solution(object):
    def numberOfNodes(self, n, queries):
        """
        :type n: int
        :type queries: List[int]
        :rtype: int
        """
        def bfs():
            result = 0
            q = [(1, 0)]
            while q:
                new_q = []
                for u, curr in q:
                    curr ^= cnt[u]%2
                    result += curr
                    for v in xrange(2*u, min(2*u+1, n)+1):
                        q.append((v, curr))
                q = new_q
            return result

        cnt = collections.Counter(queries)
        return bfs()