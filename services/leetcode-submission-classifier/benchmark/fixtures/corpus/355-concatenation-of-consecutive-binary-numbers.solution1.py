# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: concatenation-of-consecutive-binary-numbers
# source_path: LeetCode-Solutions-master/Python/concatenation-of-consecutive-binary-numbers.py
# solution_class: Solution
# submission_id: c5df2b44de14d5e15ddbf5c788803c1ee1b2c9ba
# seed: 671005730

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        result = l = 0
        for i in xrange(1, n+1):
            if i&(i-1) == 0:
                l += 1
            result = ((result<<l)%MOD+i)%MOD
        return result