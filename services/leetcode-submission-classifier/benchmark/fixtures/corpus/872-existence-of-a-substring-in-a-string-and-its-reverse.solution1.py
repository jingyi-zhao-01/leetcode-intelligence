# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: existence-of-a-substring-in-a-string-and-its-reverse
# source_path: LeetCode-Solutions-master/Python/existence-of-a-substring-in-a-string-and-its-reverse.py
# solution_class: Solution
# submission_id: 9fe45a03c38bbbf97ab335cc17c8c5e41ca8f9c3
# seed: 3273891077

# Time:  O(n)
# Space: O(min(n, 26^2))

# hash table

class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = [[False]*26 for _ in xrange(26)]
        for i in xrange(len(s)-1):
            lookup[ord(s[i])-ord('a')][ord(s[i+1])-ord('a')] = True
        return any(lookup[ord(s[i+1])-ord('a')][ord(s[i])-ord('a')]  for i in xrange(len(s)-1))