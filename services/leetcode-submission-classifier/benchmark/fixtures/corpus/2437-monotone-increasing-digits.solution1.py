# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: monotone-increasing-digits
# source_path: LeetCode-Solutions-master/Python/monotone-increasing-digits.py
# solution_class: Solution
# submission_id: 0e50849c571a6dd263bbd687f8db06a8e4042a07
# seed: 3983587013

# Time:  O(logn) = O(1)
# Space: O(logn) = O(1)

class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        nums = map(int, list(str(N)))
        leftmost_inverted_idx = len(nums)
        for i in reversed(xrange(1, len(nums))):
            if nums[i-1] > nums[i]:
                leftmost_inverted_idx = i
                nums[i-1] -= 1
        for i in xrange(leftmost_inverted_idx, len(nums)):
            nums[i] = 9
        return int("".join(map(str, nums)))