# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-x-value-of-array-i
# source_path: LeetCode-Solutions-master/Python/find-x-value-of-array-i.py
# solution_class: Solution
# submission_id: 29153dd12066461914bc9b339c09802fa951043c
# seed: 1802288198

# Time:  O(n * k)
# Space: O(k)

# dp

class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = [0]*k
        dp = [0]*k
        for x in nums:
            new_dp = [0]*k
            new_dp[x%k] += 1
            for i, c in enumerate(dp):
                new_dp[i*x%k] += c
            for i, c in enumerate(new_dp):
                result[i] += c 
            dp = new_dp
        return result