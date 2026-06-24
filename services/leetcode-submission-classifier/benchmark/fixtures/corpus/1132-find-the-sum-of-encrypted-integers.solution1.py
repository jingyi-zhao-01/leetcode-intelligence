# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-sum-of-encrypted-integers
# source_path: LeetCode-Solutions-master/Python/find-the-sum-of-encrypted-integers.py
# solution_class: Solution
# submission_id: 9583d76611992bd8d0c91fc6301c04da0b68865e
# seed: 2563012748

# Time:  O(nlogr)
# Space: O(1)

# array

class Solution(object):
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def f(x):
            mx = base = 0
            while x:
                mx = max(mx, x%10)
                x //= 10
                base = 10*base+1
            return mx*base

        return sum(f(x) for x in nums)