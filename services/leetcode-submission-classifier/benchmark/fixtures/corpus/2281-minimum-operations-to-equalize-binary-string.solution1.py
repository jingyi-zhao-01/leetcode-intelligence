# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-equalize-binary-string
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-equalize-binary-string.py
# solution_class: Solution
# submission_id: a81a55328becc3f3c7fcb6ac30e6e0f2b3bdc563
# seed: 2005350192

# Time:  O(n)
# Space: O(1)

# math

class Solution(object):
    def minOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b

        zero = s.count('0')
        if len(s) == k:
            return 0 if zero == 0 else 1 if zero == len(s) else -1
        result = float("inf")
        if (k&1) == (zero&1):
            i = max(ceil_divide(zero, k), ceil_divide(len(s)-zero, len(s)-k))
            if (i&1) == 0:
                i += 1
            result = min(result, i)
        if (zero&1) == 0:
            i = max(ceil_divide(zero, k), ceil_divide(zero, len(s)-k))
            if (i&1) == 1:
                i += 1
            result = min(result, i)
        return result if result != float("inf") else -1