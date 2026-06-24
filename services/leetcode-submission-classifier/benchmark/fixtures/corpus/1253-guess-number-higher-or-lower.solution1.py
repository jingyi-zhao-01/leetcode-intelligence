# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: guess-number-higher-or-lower
# source_path: LeetCode-Solutions-master/Python/guess-number-higher-or-lower.py
# solution_class: Solution
# submission_id: 51192948b85e4d3c4ef1ea2ec2d7d9aa49137f71
# seed: 2265085712

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) / 2
            if guess(mid) <= 0: # noqa
                right = mid - 1
            else:
                left = mid + 1
        return left