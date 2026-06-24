# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-maximum-non-decreasing-array-length
# source_path: LeetCode-Solutions-master/Python/find-maximum-non-decreasing-array-length.py
# solution_class: Solution
# submission_id: 7654c93701aff976c54a64ddd2d690a296ff804b
# seed: 4175468240

# Time:  O(n)
# Space: O(n)

# dp, greedy, prefix sum, mono stack, two pointers

class Solution(object):
    def findMaximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = prefix = left = 0
        stk = [(0, 0, 0)]
        for right in xrange(len(nums)):
            prefix += nums[right]
            while left+1 < len(stk) and stk[left+1][0] <= prefix:
                left += 1
            last, dp = prefix-stk[left][1], stk[left][2]+1
            while stk and stk[-1][0] >= last+prefix:
                stk.pop()
            stk.append((last+prefix, prefix, dp))
            left = min(left, len(stk)-1)
        return dp