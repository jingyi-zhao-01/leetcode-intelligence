# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sorting-three-groups
# source_path: LeetCode-Solutions-master/Python/sorting-three-groups.py
# solution_class: Solution
# submission_id: fc96b59cbe12db88745fe404926654a1309e9e24
# seed: 1871651332

# Time:  O(k * n) = O(n)
# Space: O(k) = O(1)

# dp

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 3

        dp = [0]*k
        for x in nums:
            dp[x-1] += 1
            for i in xrange(x, len(dp)):
                dp[i] = max(dp[i], dp[i-1])
        return len(nums)-dp[-1]