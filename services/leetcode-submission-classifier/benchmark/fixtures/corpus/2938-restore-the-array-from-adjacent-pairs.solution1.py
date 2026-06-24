# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: restore-the-array-from-adjacent-pairs
# source_path: LeetCode-Solutions-master/Python/restore-the-array-from-adjacent-pairs.py
# solution_class: Solution
# submission_id: c600d9079502215d7cd9ce6b57130fddb54105d5
# seed: 1508382827

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        adj = collections.defaultdict(list)
        for u, v in adjacentPairs: 
            adj[u].append(v)
            adj[v].append(u)
        result = next([x, adj[x][0]] for x in adj if len(adj[x]) == 1)
        while len(result) != len(adjacentPairs)+1:
            result.append(adj[result[-1]][adj[result[-1]][0] == result[-2]])
        return result