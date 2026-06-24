# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-three-consecutive-integers-that-sum-to-a-given-number
# source_path: LeetCode-Solutions-master/Python/find-three-consecutive-integers-that-sum-to-a-given-number.py
# solution_class: Solution
# submission_id: 27b996eafd88a7c008bb16f0f8d2a24a96eda334
# seed: 3383325713

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        return [num//3-1, num//3, num//3+1] if num%3 == 0 else []