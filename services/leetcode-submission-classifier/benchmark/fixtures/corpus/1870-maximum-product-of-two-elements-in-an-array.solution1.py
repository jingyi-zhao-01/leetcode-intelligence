# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-product-of-two-elements-in-an-array
# source_path: LeetCode-Solutions-master/Python/maximum-product-of-two-elements-in-an-array.py
# solution_class: Solution
# submission_id: 58c10d8ee90dcee3e9ca6d2b3ec0c46854cb6b00
# seed: 2926707888

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = m2 = 0
        for num in nums:
            if num > m1:
                m1, m2 = num, m1
            elif num > m2:
                m2 = num
        return (m1-1)*(m2-1)