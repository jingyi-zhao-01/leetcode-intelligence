# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: append-characters-to-string-to-make-subsequence
# source_path: LeetCode-Solutions-master/Python/append-characters-to-string-to-make-subsequence.py
# solution_class: Solution
# submission_id: 4a6f5d0764db6be934d7c5f2856f713cdeabf74c
# seed: 3101325827

# Time:  O(n)
# Space: O(1)

# two pointers, greedy

class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        i = -1
        for j, c in enumerate(t):
            for i in xrange(i+1, len(s)):
                if s[i] == c:
                    break
            else:
                return len(t)-j
        return 0