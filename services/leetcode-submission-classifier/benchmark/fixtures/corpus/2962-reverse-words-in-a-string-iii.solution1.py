# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-words-in-a-string-iii
# source_path: LeetCode-Solutions-master/Python/reverse-words-in-a-string-iii.py
# solution_class: Solution
# submission_id: df81e6869fdbaa23bda6da3ff28147367057292b
# seed: 141298740

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverse(s, begin, end):
            for i in xrange((end - begin) // 2):
                s[begin + i], s[end - 1 - i] = s[end - 1 - i], s[begin + i]

        s, i = list(s), 0
        for j in xrange(len(s) + 1):
            if j == len(s) or s[j] == ' ':
                reverse(s, i, j)
                i = j + 1
        return "".join(s)