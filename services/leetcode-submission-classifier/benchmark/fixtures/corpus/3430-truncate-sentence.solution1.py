# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: truncate-sentence
# source_path: LeetCode-Solutions-master/Python/truncate-sentence.py
# solution_class: Solution
# submission_id: 834f8b822f2c6234d1383fb64e83b8abb549b97d
# seed: 888292112

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        for i in xrange(len(s)):
            if s[i] == ' ':
                k -= 1
                if not k:
                    return s[:i]
        return s