# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: possible-bipartition
# source_path: LeetCode-Solutions-master/Python/possible-bipartition.py
# solution_class: Solution
# submission_id: 4b006d826e7df0e54c79efe1d02620f8e2737088
# seed: 515757144

# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)

import collections

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        adj = [[] for _ in xrange(N)]
        for u, v in dislikes:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)

        color = [0]*N
        color[0] = 1
        q = collections.deque([0])
        while q:
            cur = q.popleft()
            for nei in adj[cur]:
                if color[nei] == color[cur]:
                    return False
                elif color[nei] == -color[cur]:
                    continue
                color[nei] = -color[cur]
                q.append(nei)
        return True