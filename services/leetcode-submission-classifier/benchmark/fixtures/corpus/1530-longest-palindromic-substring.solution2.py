# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-palindromic-substring
# source_path: LeetCode-Solutions-master/Python/longest-palindromic-substring.py
# solution_class: Solution2
# submission_id: 89a51117025018708202ba59b2c8d52989a4248a
# seed: 2545512882

# Time:  O(n)
# Space: O(n)

class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return (right-left+1)-2
        
        left, right = -1, -2
        for i in xrange(len(s)):
            l = max(expand(s, i, i), expand(s, i, i+1))
            if l > right-left+1:
                right = i+l//2
                left = right-l+1
        return s[left:right+1] if left >= 0 else ""