# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-words-in-a-string-ii
# source_path: LeetCode-Solutions-master/Python/reverse-words-in-a-string-ii.py
# solution_class: Solution
# submission_id: 2e78f297154b327532be8ff3591d89bf40e19a8c
# seed: 4222294384

# Time: O(n)
# Space:O(1)

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        def reverse(s, begin, end):
            for i in xrange((end - begin) / 2):
                s[begin + i], s[end - 1 - i] = s[end - 1 - i], s[begin + i]

        reverse(s, 0, len(s))
        i = 0
        for j in xrange(len(s) + 1):
            if j == len(s) or s[j] == ' ':
                reverse(s, i, j)
                i = j + 1