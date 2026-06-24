# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-maximum-non-decreasing-array-length
# source_path: LeetCode-Solutions-master/Python/find-maximum-non-decreasing-array-length.py
# solution_class: Solution2
# submission_id: a9cb46983b73b04ae611ac086779079e286fb314
# seed: 1946027218

# Time:  O(n)
# Space: O(n)

# dp, greedy, prefix sum, mono stack, two pointers

class Solution2(object):
    def findMaximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = prefix = prev_prefix = prev_dp = 0
        dq = collections.deque()
        for right in xrange(len(nums)):
            prefix += nums[right]
            while dq and dq[0][0] <= prefix:
                _, prev_prefix, prev_dp = dq.popleft()
            last, dp = prefix-prev_prefix, prev_dp+1
            while dq and dq[-1][0] >= last+prefix:
                dq.pop()
            dq.append((last+prefix, prefix, dp))
        return dp