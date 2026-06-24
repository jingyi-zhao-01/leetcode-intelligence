# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-subarrays-having-even-product
# source_path: LeetCode-Solutions-master/Python/number-of-subarrays-having-even-product.py
# solution_class: Solution2
# submission_id: 715277519d2e61153900191874a7cf529257b300
# seed: 2217810589

# Time:  O(n)
# Space: O(1)

# dp, math

class Solution2(object):
    def evenProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = cnt = 0
        for i, x in enumerate(nums):
            if x%2 == 0:
                cnt = i+1
            result += cnt
        return result