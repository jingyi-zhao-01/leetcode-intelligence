# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-subsequences-with-odd-sum
# source_path: LeetCode-Solutions-master/Python/number-of-subsequences-with-odd-sum.py
# solution_class: Solution2
# submission_id: c40acf6512a8b145b72739a9c254557efb809d95
# seed: 3011936048

# Time:  O(n)
# Space: O(1)

# combinatorics, fast exponentiation

class Solution2(object):
    def subsequenceCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        dp = [0]*2
        for x in nums:
            dp = [(dp[i]+dp[i^(x%2)]+int(x%2 == i))%MOD for i in xrange(2)]
        return dp[1]