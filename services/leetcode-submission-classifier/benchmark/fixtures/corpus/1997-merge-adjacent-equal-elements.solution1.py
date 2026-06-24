# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: merge-adjacent-equal-elements
# source_path: LeetCode-Solutions-master/Python/merge-adjacent-equal-elements.py
# solution_class: Solution
# submission_id: 2b8b2502aa0167427b9ad7b95c02e5ed37ac93b4
# seed: 3414532765

# Time:  O(n)
# Space: O(1)

# stack, simulation

class Solution(object):
    def mergeAdjacent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for x in nums:
            while result and result[-1] == x:
                result.pop()
                x *= 2
            result.append(x)
        return result