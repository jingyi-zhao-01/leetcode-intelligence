# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-maximum-non-decreasing-array-length
# source_path: LeetCode-Solutions-master/Python/find-maximum-non-decreasing-array-length.py
# solution_class: Solution3
# submission_id: 4c272302cb412e8c2e2a7e9e81a0bc68f0cc2e70
# seed: 649008573

# Time:  O(n)
# Space: O(n)

# dp, greedy, prefix sum, mono stack, two pointers

class Solution3(object):
    def findMaximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = prefix = left = 0
        stk = [(0, 0, 0)]
        for right in xrange(len(nums)):
            prefix += nums[right]
            left = bisect.bisect_left(stk, (prefix+1, 0, 0))-1
            last, dp = prefix-stk[left][1], stk[left][2]+1
            while stk and stk[-1][0] >= last+prefix:
                stk.pop()
            stk.append((last+prefix, prefix, dp))
        return dp