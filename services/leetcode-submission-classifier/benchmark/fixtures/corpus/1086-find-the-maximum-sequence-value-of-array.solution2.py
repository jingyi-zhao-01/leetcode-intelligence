# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-maximum-sequence-value-of-array
# source_path: LeetCode-Solutions-master/Python/find-the-maximum-sequence-value-of-array.py
# solution_class: Solution
# submission_id: d46a422498ded1aa1391cd1d430e100946ea0fc8
# seed: 4154619229

# Time:  O(n * r + r^2)
# Space: O(r)

# bitmasks, prefix sum, dp

class Solution(object):
    def maxValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = [[set() if j else {0} for j in xrange(k+1)] for i in xrange(len(nums)+1)]
        for i in xrange(len(nums)):
            for j in xrange(1, len(left[i+1])):
                left[i+1][j] = set(left[i][j])
                for x in left[i][j-1]:
                    left[i+1][j].add(x|nums[i])
        right = [[set() if j else {0} for j in xrange(k+1)] for i in xrange(len(nums)+1)]
        for i in reversed(xrange(len(nums))):
            for j in xrange(1, len(right[i])):
                right[i][j] = set(right[i+1][j])
                for x in right[i+1][j-1]:
                    right[i][j].add(x|nums[i])
        return max(l^r for i in xrange(k, (len(nums)-k)+1) for l in left[i][k] for r in right[i][k])