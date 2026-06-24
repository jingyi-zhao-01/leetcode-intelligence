# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-special-substring-of-length-k
# source_path: LeetCode-Solutions-master/Python/find-special-substring-of-length-k.py
# solution_class: Solution
# submission_id: 965f0fb040b14a2a8414a5e2dd19fbb65067b7fa
# seed: 572062130

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def hasSpecialSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        l = 0
        for i in xrange(len(s)):
            l += 1
            if i+1 == len(s) or s[i] != s[i+1]:
                if l == k:
                    return True
                l = 0
        return False