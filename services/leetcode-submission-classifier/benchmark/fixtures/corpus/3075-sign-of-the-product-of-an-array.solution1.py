# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sign-of-the-product-of-an-array
# source_path: LeetCode-Solutions-master/Python/sign-of-the-product-of-an-array.py
# solution_class: Solution
# submission_id: 436d1ef3e5e1f0138ac12d85e4a8a65fbd833fb1
# seed: 4164421778

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = 0
        for x in nums:
            if not x:
                return 0
            if x < 0:
                flag ^= 1
        return -1 if flag else 1