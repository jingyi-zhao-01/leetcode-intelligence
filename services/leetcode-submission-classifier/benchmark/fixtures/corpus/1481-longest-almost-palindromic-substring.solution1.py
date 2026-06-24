# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-almost-palindromic-substring
# source_path: LeetCode-Solutions-master/Python/longest-almost-palindromic-substring.py
# solution_class: Solution
# submission_id: e212f1604a3cf4be69f6b95fd74db1f86cc02b98
# seed: 1507865949

# Time:  O(n^2)
# Space: O(1)

# two pointers

class Solution(object):
    def almostPalindromic(self, s):
        """
        :type s: str
        :rtype: int
        """
        def expand(left, right):
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left, right

        result = 0
        for i in xrange(2*len(s)-1):
            left, right = expand(i//2, (i+1)//2)
            for left, right in ((left-1, right), (left, right+1)):
                l, r = expand(left, right)
                result = max(result, min((r-l+1)-2, len(s)))
        return result