# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-equalize-binary-string
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-equalize-binary-string.py
# solution_class: Solution2
# submission_id: c6d41653ce9c338807adf986432890668b804277
# seed: 3591605736

# Time:  O(n)
# Space: O(1)

# math

class Solution2(object):
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
        i = max(ceil_divide(zero, k), ceil_divide(len(s)-zero, len(s)-k))
        if (i&1) == 0:
            i += 1
        if ((i*k-zero)&1) == 0:  # (k&1) == (zero&1)
            result = min(result, i)
        i = max(ceil_divide(zero, k), ceil_divide(zero, len(s)-k))
        if (i&1) == 1:
            i += 1
        if ((i*k-zero)&1) == 0:  # (zero&1) == 0
            result = min(result, i)
        return result if result != float("inf") else -1