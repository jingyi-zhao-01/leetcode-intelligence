# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-odd-numbers-in-an-interval-range
# source_path: LeetCode-Solutions-master/Python/count-odd-numbers-in-an-interval-range.py
# solution_class: Solution
# submission_id: e90567e298b8ccc3e8c3fa32fc9734f1076b44b9
# seed: 2841002729

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        return (high+1)//2 - ((low-1)+1)//2