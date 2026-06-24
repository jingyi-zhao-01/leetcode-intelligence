# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: first-bad-version
# source_path: LeetCode-Solutions-master/Python/first-bad-version.py
# solution_class: Solution
# submission_id: 1990b04d9b7843ea760029ad9284903b545a2eab
# seed: 588047756

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) / 2
            if isBadVersion(mid): # noqa
                right = mid - 1
            else:
                left = mid + 1
        return left