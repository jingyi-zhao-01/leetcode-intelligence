# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-segments-in-a-string
# source_path: LeetCode-Solutions-master/Python/number-of-segments-in-a-string.py
# solution_class: Solution
# submission_id: 2826b8ec6b9fb95c33a7ec80e08046b71517c0c6
# seed: 219766650

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = int(len(s) and s[-1] != ' ')
        for i in xrange(1, len(s)):
            if s[i] == ' ' and s[i-1] != ' ':
                result += 1
        return result

    def countSegments2(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len([i for i in s.strip().split(' ') if i])