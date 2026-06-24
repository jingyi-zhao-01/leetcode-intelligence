# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: score-of-a-string
# source_path: LeetCode-Solutions-master/Python/score-of-a-string.py
# solution_class: Solution
# submission_id: c2a82c7f48f8d4ee6c9f4b857f468a92828b29e8
# seed: 190416011

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(abs(ord(s[i+1])-ord(s[i])) for i in xrange(len(s)-1))