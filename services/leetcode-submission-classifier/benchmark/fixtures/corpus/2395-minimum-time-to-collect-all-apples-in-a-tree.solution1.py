# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-time-to-collect-all-apples-in-a-tree
# source_path: LeetCode-Solutions-master/Python/minimum-time-to-collect-all-apples-in-a-tree.py
# solution_class: Solution
# submission_id: e6143fa07eacd2480d5fb6e7ac5071022e6bf43c
# seed: 728320877

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        result = [0, 0]
        s = [(1, (-1, 0, result))]
        while s:
            step, params = s.pop()
            if step == 1:
                par, node, ret = params
                ret[:] = [0, int(hasApple[node])]
                for nei in reversed(graph[node]):
                    if nei == par:
                        continue
                    new_ret = [0, 0]
                    s.append((2, (new_ret, ret)))
                    s.append((1, (node, nei, new_ret)))
            else:
                new_ret, ret = params
                ret[0] += new_ret[0]+new_ret[1]
                ret[1] |= bool(new_ret[0]+new_ret[1])
        return 2*result[0]