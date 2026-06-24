# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-score-using-exactly-k-pairs
# source_path: LeetCode-Solutions-master/Python/maximum-score-using-exactly-k-pairs.py
# solution_class: Solution
# submission_id: 1ee2a7c9b8edfab7c99f2d8c40f1d9bb02a6d6ed
# seed: 2041326777

# Time:  O(n * m * k)
# Space: O(min(n, m) * k)

# dp

class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        NEG_INF = float("-inf")        
        dp = [[NEG_INF]*len(nums2) for _ in xrange(len(nums1))]
        new_dp = [[NEG_INF]*len(nums2) for _ in xrange(len(nums1))]
        for c in xrange(k):
            for i in xrange(c, len(nums1)):
                for j in xrange(c, len(nums2)):
                    new_dp[i][j] = max(
                        new_dp[i][j-1] if j-1 >= c else NEG_INF,
                        new_dp[i-1][j] if i-1 >= c else NEG_INF,
                        (dp[i-1][j-1] if c else 0) + nums1[i]*nums2[j]
                    )
            dp, new_dp = new_dp, dp
        return dp[-1][-1]