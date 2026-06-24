# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-subarrays-with-gcd-equal-to-k
# source_path: LeetCode-Solutions-master/Python/number-of-subarrays-with-gcd-equal-to-k.py
# solution_class: Solution
# submission_id: db4bba53e3eb388cbf0770e243cd49b04f252333
# seed: 3443116083

# Time:  O(nlogr), r = max(nums)
# Space: O(logr)

# dp

class Solution(object):
    def subarrayGCD(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        result = 0
        dp = collections.Counter()
        for x in nums:
            new_dp = collections.Counter()
            if x%k == 0:
                dp[x] += 1
                for g, cnt in dp.iteritems():
                    new_dp[gcd(g, x)] += cnt
            dp = new_dp
            result += dp[k]
        return result