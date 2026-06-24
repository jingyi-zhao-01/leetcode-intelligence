# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-n-th-value-after-k-seconds
# source_path: LeetCode-Solutions-master/Python/find-the-n-th-value-after-k-seconds.py
# solution_class: Solution2
# submission_id: 456deedc3389fb38e63f3bbaf4f2fda0dc05481f
# seed: 1700872382

# Time:  O(n + k)
# Space: O(n + k)

# combinatorics

class Solution2(object):
    def valueAfterKSeconds(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        prefix = [1]*n
        for _ in range(k):
            for i in xrange(1, n):
                prefix[i] = (prefix[i]+prefix[i-1])%MOD
        return prefix[-1]