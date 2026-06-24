# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: greatest-sum-divisible-by-three
# source_path: LeetCode-Solutions-master/Python/greatest-sum-divisible-by-three.py
# solution_class: Solution
# submission_id: 83e98d134d76d6ee1856de54b92105420cca2f4e
# seed: 155418770

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, 0, 0]
        for num in nums:
            for i in [num+x for x in dp]:
                dp[i%3] = max(dp[i%3], i)
        return dp[0]