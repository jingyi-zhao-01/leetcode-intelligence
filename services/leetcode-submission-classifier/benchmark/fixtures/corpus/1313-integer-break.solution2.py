# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: integer-break
# source_path: LeetCode-Solutions-master/Python/integer-break.py
# solution_class: Solution2
# submission_id: 1c8986f22d4b770433e764f81f1cf12bbae2d397
# seed: 1970259266

# Time:  O(logn), pow is O(logn).
# Space: O(1)

class Solution2(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n - 1

        # integerBreak(n) = max(integerBreak(n - 2) * 2, integerBreak(n - 3) * 3)
        res = [0, 1, 2, 3]
        for i in xrange(4, n + 1):
            res[i % 4] = max(res[(i - 2) % 4] * 2, res[(i - 3) % 4] * 3)
        return res[n % 4]