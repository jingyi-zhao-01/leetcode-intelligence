# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-alternating-xor-partitions
# source_path: LeetCode-Solutions-master/Python/number-of-alternating-xor-partitions.py
# solution_class: Solution
# submission_id: a3aadb61b6b12196f04eb16b0a029a985a781b1b
# seed: 2536616938

# Time:  O(n)
# Space: O(1)

# dp

class Solution(object):
    def alternatingXOR(self, nums, target1, target2):
        """
        :type nums: List[int]
        :type target1: int
        :type target2: int
        :rtype: int
        """
        MOD = 10**9+7
        vals = [0, target1, target1^target2, target2]
        dp = [0]*len(vals)
        dp[0] = 1
        prefix = 0
        for i in xrange(len(nums)-1):
            new_dp = dp[:]
            prefix ^= nums[i]            
            for j in xrange(len(vals)):
                if vals[j] != prefix:
                    continue
                new_dp[j] = (new_dp[j]+dp[(j-1)%len(dp)])%MOD
            dp = new_dp
        prefix ^= nums[-1]
        result = 0
        for i in xrange(len(vals)):
            if vals[i] != prefix:
                continue
            result = (result+dp[(i-1)%len(dp)])%MOD
        return result