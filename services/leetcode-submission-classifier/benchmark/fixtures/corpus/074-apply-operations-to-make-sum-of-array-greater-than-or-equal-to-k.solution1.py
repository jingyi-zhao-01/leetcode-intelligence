# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k
# source_path: LeetCode-Solutions-master/Python/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k.py
# solution_class: Solution
# submission_id: 9d102d6196face0e8aefe631b99833719c251b09
# seed: 353590841

# Time:  O(logn)
# Space: O(1)

# math

class Solution(object):
    def minOperations(self, k):
        """
        :type k: int
        :rtype: int
        """
        # reference: https://stackoverflow.com/questions/15390807/integer-square-root-in-python
        def isqrt(n):
            a, b = n, (n+1)//2
            while b < a:
                a, b = b, (b+n//b)//2
            return a

        def ceil_divide(a, b):
            return (a+b-1)//b
    
        x = isqrt(k)
        return (x-1)+(ceil_divide(k, x)-1)