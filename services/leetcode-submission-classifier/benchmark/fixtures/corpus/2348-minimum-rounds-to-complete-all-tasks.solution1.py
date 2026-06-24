# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-rounds-to-complete-all-tasks
# source_path: LeetCode-Solutions-master/Python/minimum-rounds-to-complete-all-tasks.py
# solution_class: Solution
# submission_id: ab7181259ea6cf85035d8f4cfd1e394639845b15
# seed: 2698797446

# Time:  O(n)
# Space: O(n)

import collections


# math, freq table

class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        cnt = collections.Counter(tasks)
        return sum((x+2)//3 for x in cnt.itervalues()) if 1 not in cnt.itervalues() else -1