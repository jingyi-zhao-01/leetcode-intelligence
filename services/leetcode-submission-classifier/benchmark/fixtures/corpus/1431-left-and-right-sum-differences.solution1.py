# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: left-and-right-sum-differences
# source_path: LeetCode-Solutions-master/Python/left-and-right-sum-differences.py
# solution_class: Solution
# submission_id: 8a7e3d9e9076d76ed48bae88835905b387e0d697
# seed: 187878573

# Time:  O(n)
# Space: O(1)

# prefix sum

class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = sum(nums)
        result = []
        curr = 0
        for x in nums:
            curr += x
            result.append(abs((curr-x)-(total-curr)))
        return result