# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: time-needed-to-inform-all-employees
# source_path: LeetCode-Solutions-master/Python/time-needed-to-inform-all-employees.py
# solution_class: Solution
# submission_id: a76a672f7d6389a0435602dbd79ee36b84565383
# seed: 3480825594

# Time:  O(n)
# Space: O(n)

import collections


# dfs solution with stack

class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        children = collections.defaultdict(list)
        for child, parent in enumerate(manager):
            if parent != -1:
                children[parent].append(child)

        result = 0
        stk = [(headID, 0)]
        while stk:
            node, curr = stk.pop()
            curr += informTime[node]
            result = max(result, curr)
            if node not in children:
                continue
            for c in children[node]:
                stk.append((c, curr))
        return result