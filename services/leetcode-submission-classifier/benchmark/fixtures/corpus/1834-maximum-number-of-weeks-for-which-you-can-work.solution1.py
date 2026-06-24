# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-weeks-for-which-you-can-work
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-weeks-for-which-you-can-work.py
# solution_class: Solution
# submission_id: 74b98ccbb02c992ceab02ea4acdac5af1030db0e
# seed: 2467301825

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def numberOfWeeks(self, milestones):
        """
        :type milestones: List[int]
        :rtype: int
        """
        total, max_num = sum(milestones), max(milestones)
        other_total = (total-max_num)
        return other_total+min(other_total+1, max_num)