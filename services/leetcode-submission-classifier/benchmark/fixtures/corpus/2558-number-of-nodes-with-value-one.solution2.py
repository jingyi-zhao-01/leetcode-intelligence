# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-nodes-with-value-one
# source_path: LeetCode-Solutions-master/Python/number-of-nodes-with-value-one.py
# solution_class: Solution2
# submission_id: 7ae0b5789de104fb010f1c1b1cdc8fa4c2d14410
# seed: 708661423

# Time:  O(q + n)
# Space: O(n)

import collections


# bfs

class Solution2(object):
    def numberOfNodes(self, n, queries):
        """
        :type n: int
        :type queries: List[int]
        :rtype: int
        """
        def iter_dfs():
            result = 0
            stk = [(1, 0)]
            while stk:
                u, curr = stk.pop()
                curr ^= cnt[u]%2
                result += curr
                for v in reversed(xrange(2*u, min(2*u+1, n)+1)):
                    stk.append((v, curr))
            return result

        cnt = collections.Counter(queries)
        return iter_dfs()