# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-subsequences-with-odd-sum
# source_path: LeetCode-Solutions-master/Python/number-of-subsequences-with-odd-sum.py
# solution_class: Solution
# submission_id: 44fc48ce71c88a0a48e66dd4b4e2c542aed77453
# seed: 1231475685

# Time:  O(n)
# Space: O(1)

# combinatorics, fast exponentiation

class Solution(object):
    def subsequenceCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        # 2^(odd-1)*2^even = 2^(len(nums)-1)
        return pow(2, len(nums)-1, MOD) if any(x%2 for x in nums) else 0