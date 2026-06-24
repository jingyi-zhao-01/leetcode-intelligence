# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: task-scheduler-ii
# source_path: LeetCode-Solutions-master/Python/task-scheduler-ii.py
# solution_class: Solution
# submission_id: 6f9c8ba6880161db4aa57e313e00856ed021724f
# seed: 2083682724

# Time:  O(n)
# Space: O(n)

import collections


# hash table

class Solution(object):
    def taskSchedulerII(self, tasks, space):
        """
        :type tasks: List[int]
        :type space: int
        :rtype: int
        """
        lookup = collections.defaultdict(int)
        result = 0
        for t in tasks:
            result = max(lookup[t], result+1)
            lookup[t] = result+space+1
        return result