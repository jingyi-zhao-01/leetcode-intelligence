# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-palindrome-with-fixed-length
# source_path: LeetCode-Solutions-master/Python/find-palindrome-with-fixed-length.py
# solution_class: Solution2
# submission_id: 21aa57232b149ad0b1a8b5e99736423b6010530b
# seed: 3672607288

# Time:  O(n * l)
# Space: O(1)

# math

class Solution2(object):
    def kthPalindrome(self, queries, intLength):
        """
        :type queries: List[int]
        :type intLength: int
        :rtype: List[int]
        """
        def f(l, x):
            if 10**((l-1)//2)+(x-1) > 10**((l+1)//2)-1:
                return -1
            s = str(10**((l-1)//2)+(x-1))
            return int(s+s[::-1][l%2:])

        return [f(intLength, x) for x in queries]