# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: replace-all-digits-with-characters
# source_path: LeetCode-Solutions-master/Python/replace-all-digits-with-characters.py
# solution_class: Solution
# submission_id: bed637294859201d4eee6b19f67ae9c00824faa5
# seed: 1726574734

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join(chr(ord(s[i-1])+int(s[i])) if i%2 else s[i] for i in xrange(len(s)))