# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-sub-arrays-with-odd-sum
# source_path: LeetCode-Solutions-master/Python/number-of-sub-arrays-with-odd-sum.py
# solution_class: Solution
# submission_id: 638f7941adbd14c3d4dc87094c4e36e404d91b95
# seed: 1783550099

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        result, accu = 0, 0
        dp = [1, 0]
        for x in arr:
            accu ^= x&1
            dp[accu] += 1
            result = (result + dp[accu^1]) % MOD
        return result