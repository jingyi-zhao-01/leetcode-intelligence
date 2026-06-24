# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-square-streak-in-an-array
# source_path: LeetCode-Solutions-master/Python/longest-square-streak-in-an-array.py
# solution_class: Solution2
# submission_id: 56642f8fae06fa318b15cd3ab6b6238ed05cbd8d
# seed: 1604720576

# Time:  O(nlogn)
# Space: O(n)

# hash table

class Solution2(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = collections.defaultdict(int)
        nums.sort()
        result = -1
        for x in nums:
            sqrt_x = int(x**0.5)
            if sqrt_x**2 == x:
                dp[x] = dp[sqrt_x]+1
            else:
                dp[x] = 1
            result = max(result, dp[x])
        return result if result != 1 else -1