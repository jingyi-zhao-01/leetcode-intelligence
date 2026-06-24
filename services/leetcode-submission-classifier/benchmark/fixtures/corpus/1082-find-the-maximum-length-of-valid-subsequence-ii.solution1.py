# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-maximum-length-of-valid-subsequence-ii
# source_path: LeetCode-Solutions-master/Python/find-the-maximum-length-of-valid-subsequence-ii.py
# solution_class: Solution
# submission_id: 823f6bf5d7982e913c525d46c5ee0a838429c3eb
# seed: 3639415468

# Time:  O(n * k)
# Space: O(k)

# dp

class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        for i in xrange(k):
            dp = [0]*k
            for x in nums:
                dp[x%k] = dp[(i-x)%k]+1
            result = max(result, max(dp))
        return result