# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: constructing-two-increasing-arrays
# source_path: LeetCode-Solutions-master/Python/constructing-two-increasing-arrays.py
# solution_class: Solution
# submission_id: c67c9db9302f2fdeaebc121a4bae89d8b3b4dddc
# seed: 2479920931

# Time:  O(m * n)
# Space: O(min(m, n))

# dp

class Solution(object):
    def minLargest(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        dp = [float("inf")]*(len(nums2)+1)
        dp[0] = 0
        for i in xrange(len(nums1)+1):
            for j in xrange(len(nums2)+1):
                if not i and not j:
                    continue
                curr = float("inf")
                if i-1 >= 0:
                    curr = min(curr, dp[j]+(2 if dp[j]%2 == nums1[i-1]%2 else 1))
                if j-1 >= 0:
                    curr = min(curr, dp[j-1]+(2 if dp[j-1]%2 == nums2[j-1]%2 else 1))
                dp[j] = curr
        return dp[-1]