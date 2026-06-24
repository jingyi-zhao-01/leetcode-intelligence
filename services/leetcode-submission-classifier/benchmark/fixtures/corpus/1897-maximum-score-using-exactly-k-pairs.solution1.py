# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-score-using-exactly-k-pairs
# source_path: LeetCode-Solutions-master/Python/maximum-score-using-exactly-k-pairs.py
# solution_class: Solution
# submission_id: ba3f1ccb0a2f7910ac974c1cd9589b28d66d175d
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
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        dp = [[NEG_INF]*(k+1) for _ in xrange(len(nums2)+1)]
        for j in xrange(len(nums2)+1):
            dp[j][0] = 0
        new_dp = [[NEG_INF]*(k+1) for _ in xrange(len(nums2)+1)]
        for i in xrange(len(nums1)):
            for j in xrange(len(nums2)+1):
                new_dp[j][0] = 0
            for j in xrange(len(nums2)):
                score = nums1[i]*nums2[j]
                for c in xrange(min(i+1, j+1, k)):
                    new_dp[j+1][c+1] = max(
                        new_dp[j][c+1],
                        dp[j+1][c+1],
                        dp[j][c]+score
                    )
            dp, new_dp = new_dp, dp
        return dp[-1][-1]