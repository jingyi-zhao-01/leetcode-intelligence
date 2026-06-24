# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: average-salary-excluding-the-minimum-and-maximum-salary
# source_path: LeetCode-Solutions-master/Python/average-salary-excluding-the-minimum-and-maximum-salary.py
# solution_class: Solution2
# submission_id: f8e2408582470eb07bf7147db4ff5a3ed27e2e21
# seed: 3173400265

# Time:  O(n)
# Space: O(1)

# one pass solution

class Solution2(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        return 1.0*(sum(salary)-min(salary)-max(salary))/(len(salary)-2)