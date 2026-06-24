# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-non-decreasing-subarray-from-two-arrays
# source_path: LeetCode-Solutions-master/Python/longest-non-decreasing-subarray-from-two-arrays.py
# solution_class: Solution
# submission_id: c610badb4a7665b451032ba9807fca3b24fc776a
# seed: 2741764612

# Time:  O(n)
# Space: O(1)

# dp

class Solution(object):
    def maxNonDecreasingLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        result = 1
        dp = [1]*2
        for i in xrange(len(nums1)-1):
            dp = [max((dp[0]+1 if nums1[i] <= nums1[i+1] else 1), (dp[1]+1 if nums2[i] <= nums1[i+1] else 1)),
                  max((dp[0]+1 if nums1[i] <= nums2[i+1] else 1), (dp[1]+1 if nums2[i] <= nums2[i+1] else 1))]
            result = max(result, max(dp))
        return result