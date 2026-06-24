# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-binary-palindromic-numbers
# source_path: LeetCode-Solutions-master/Python/count-binary-palindromic-numbers.py
# solution_class: Solution2
# submission_id: 6f804fc5b82e205834131eba4539a3fb7f8ab628
# seed: 50635286

# Time:  O(logn)
# Space: O(1)

# bitmasks, combinatorics

class Solution2(object):
    def countBinaryPalindromes(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = map(int, bin(n)[2:])
        l = len(s)//2
        return ((1<<l)-1)+(n>>l)+int(s[:len(s)-l]+s[:l][::-1] <= s)