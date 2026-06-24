# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: time-needed-to-inform-all-employees
# source_path: LeetCode-Solutions-master/Python/time-needed-to-inform-all-employees.py
# solution_class: Solution2
# submission_id: b8b7603d08f540bdee09fdbee2160955228ba0fc
# seed: 1299301928

# Time:  O(n)
# Space: O(n)

import collections


# dfs solution with stack

class Solution2(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        def dfs(informTime, children, node):
            return (max(dfs(informTime, children, c)
                        for c in children[node])
                    if node in children
                    else 0) + informTime[node]

        children = collections.defaultdict(list)
        for child, parent in enumerate(manager):
            if parent != -1:
                children[parent].append(child)
        return dfs(informTime, children, headID)