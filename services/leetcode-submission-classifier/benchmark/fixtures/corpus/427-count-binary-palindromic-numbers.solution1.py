# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-binary-palindromic-numbers
# source_path: LeetCode-Solutions-master/Python/count-binary-palindromic-numbers.py
# solution_class: Solution
# submission_id: 7d68222dd28f96b15795fab5630393e0dfb036ac
# seed: 2862881183

# Time:  O(logn)
# Space: O(1)

# bitmasks, combinatorics

class Solution(object):
    def countBinaryPalindromes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def length(n):
            result = 0
            while n:
                result += 1
                n >>= 1
            return result

        def reverse(n, l):
            result = 0
            for i in xrange(l):
                if n&(1<<i):
                    result |= 1<<((l-1)-i)
            return result
    
        l = length(n)//2
        return ((1<<l)-1)+(n>>l)+int(((n>>l)<<l)|reverse(n>>(length(n)-l), l) <= n)