# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-xor-sum-of-two-arrays
# source_path: LeetCode-Solutions-master/Python/minimum-xor-sum-of-two-arrays.py
# solution_class: Solution2
# submission_id: 4d5f7fb70fd6f5054877dea5bb0ba5dfea19c952
# seed: 1612107288

# Time:  O(n^3)
# Space: O(n^2)

# weighted bipartite matching solution

class Solution2(object):
    def minimumXORSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        dp = [(float("inf"), float("inf"))]*(2**len(nums2))
        dp[0] = (0, 0)
        for mask in xrange(len(dp)):
            bit = 1
            for i in xrange(len(nums2)):
                if (mask&bit) == 0:
                    dp[mask|bit] = min(dp[mask|bit], (dp[mask][0]+(nums1[dp[mask][1]]^nums2[i]), dp[mask][1]+1))
                bit <<= 1
        return dp[-1][0]