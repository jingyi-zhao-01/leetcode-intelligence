# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: palindromic-substrings
# source_path: LeetCode-Solutions-master/Python/palindromic-substrings.py
# solution_class: Solution
# submission_id: e9bbce0fe13cd00f041a2fd96b0ff997e0826d8c
# seed: 2651236450

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def manacher(s):
            s = '^#' + '#'.join(s) + '#$'
            P = [0] * len(s)
            C, R = 0, 0
            for i in xrange(1, len(s) - 1):
                i_mirror = 2*C-i
                if R > i:
                    P[i] = min(R-i, P[i_mirror])
                while s[i+1+P[i]] == s[i-1-P[i]]:
                    P[i] += 1
                if i+P[i] > R:
                    C, R = i, i+P[i]
            return P
        return sum((max_len+1)//2 for max_len in manacher(s))