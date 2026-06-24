# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-subarrays-having-even-product
# source_path: LeetCode-Solutions-master/Python/number-of-subarrays-having-even-product.py
# solution_class: Solution
# submission_id: 6e78e48c4eeb2e4ec8bdc2d8f06e4650431c8699
# seed: 820152244

# Time:  O(n)
# Space: O(1)

# dp, math

class Solution(object):
    def evenProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = (len(nums)+1)*len(nums)//2
        cnt = 0
        for x in nums:
            cnt = cnt+1 if x%2 else 0
            result -= cnt
        return result