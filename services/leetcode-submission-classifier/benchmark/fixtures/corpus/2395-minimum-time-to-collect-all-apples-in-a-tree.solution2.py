# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-time-to-collect-all-apples-in-a-tree
# source_path: LeetCode-Solutions-master/Python/minimum-time-to-collect-all-apples-in-a-tree.py
# solution_class: Solution2
# submission_id: 35db5f13ba752a572b4d28db8ff4745caf25440e
# seed: 3913040171

# Time:  O(n)
# Space: O(n)

import collections

class Solution2(object):
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
        
        result = [0]
        s = [(1, (-1, 0, result))]
        while s:
            step, params = s.pop()
            if step == 1:
                par, node, ret = params
                tmp = [int(hasApple[node])]
                s.append((3, (tmp, ret)))
                for nei in reversed(graph[node]):
                    if nei == par:
                        continue
                    new_ret = [0]
                    s.append((2, (new_ret, tmp, ret)))
                    s.append((1, (node, nei, new_ret)))
            elif step == 2:
                new_ret, tmp, ret = params
                ret[0] += new_ret[0]
                tmp[0] |= bool(new_ret[0])
            else:
                tmp, ret = params
                ret[0] += tmp[0]
        return 2*max(result[0]-1, 0)