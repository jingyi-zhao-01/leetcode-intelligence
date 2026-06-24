# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-elements-to-add-to-form-a-given-sum
# source_path: LeetCode-Solutions-master/Python/minimum-elements-to-add-to-form-a-given-sum.py
# solution_class: Solution
# submission_id: 54df75ae33355c0a42beb3978ed0b018fe9c5fe7
# seed: 2991120177

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        return (abs(sum(nums)-goal) + (limit-1))//limit