# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-triangular-sum-of-an-array
# source_path: LeetCode-Solutions-master/Python/find-triangular-sum-of-an-array.py
# solution_class: Solution2
# submission_id: c3436865a3bf5060118f74cbc4d88de541cc3f7b
# seed: 4264509085

# Time:  O(n)
# Space: O(1)

# combinatorics, number theory

class Solution2(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nCr = 1
        for i in xrange(len(nums)):
            result = (result+nCr*nums[i])%10
            nCr *= (len(nums)-1)-i
            nCr //= i+1
        return result