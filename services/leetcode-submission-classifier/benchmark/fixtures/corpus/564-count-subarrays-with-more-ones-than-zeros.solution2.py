# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-subarrays-with-more-ones-than-zeros
# source_path: LeetCode-Solutions-master/Python/count-subarrays-with-more-ones-than-zeros.py
# solution_class: Solution2
# submission_id: a118760622b01548eabec18a6e45aafdb8343fbd
# seed: 1327984318

# Time:  O(n)
# Space: O(n)

import collections

class Solution2(object):
    def subarraysWithMoreZerosThanOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7

        lookup = {0:-1}
        dp = [0]*len(nums)
        result = total = 0
        for i, x in enumerate(nums):
            total += 1 if x == 1 else -1
            if total not in lookup:
                if total > 0:
                    dp[i] = i+1
            else:
                j = lookup[total]
                if j != -1:
                    dp[i] = dp[j]
                if x > 0:
                    dp[i] += (i-1)-j
            lookup[total] = i
            result = (result+dp[i])%MOD
        return result