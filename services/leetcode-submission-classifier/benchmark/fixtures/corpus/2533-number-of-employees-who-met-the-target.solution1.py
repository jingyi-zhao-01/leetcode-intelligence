# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-employees-who-met-the-target
# source_path: LeetCode-Solutions-master/Python/number-of-employees-who-met-the-target.py
# solution_class: Solution
# submission_id: 5c32c2a3274516b8acdd2ed34350f9e549f2b868
# seed: 4282668986

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        return sum(x >= target for x in hours)