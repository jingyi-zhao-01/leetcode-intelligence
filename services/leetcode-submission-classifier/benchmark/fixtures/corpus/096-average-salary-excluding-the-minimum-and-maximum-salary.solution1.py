# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: average-salary-excluding-the-minimum-and-maximum-salary
# source_path: LeetCode-Solutions-master/Python/average-salary-excluding-the-minimum-and-maximum-salary.py
# solution_class: Solution
# submission_id: 24b037720122ddc50bf5332efbffc9a0d6cdd3b6
# seed: 230614536

# Time:  O(n)
# Space: O(1)

# one pass solution

class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        total, mi, ma = 0, float("inf"), float("-inf")
        for s in salary:
            total += s
            mi, ma = min(mi, s), max(ma, s)
        return 1.0*(total-mi-ma)/(len(salary)-2)