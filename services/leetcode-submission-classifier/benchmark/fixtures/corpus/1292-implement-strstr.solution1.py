# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: implement-strstr
# source_path: LeetCode-Solutions-master/Python/implement-strstr.py
# solution_class: Solution
# submission_id: 355aba2b50f7f666ba3f0179d406a611db7d64d3
# seed: 419621636

# Time:  O(n + k)
# Space: O(k)

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        return self.KMP(haystack, needle)

    def KMP(self, text, pattern):
        prefix = self.getPrefix(pattern)
        j = -1
        for i in xrange(len(text)):
            while j > -1 and pattern[j + 1] != text[i]:
                j = prefix[j]
            if pattern[j + 1] == text[i]:
                j += 1
            if j == len(pattern) - 1:
                return i - j
        return -1

    def getPrefix(self, pattern):
        prefix = [-1] * len(pattern)
        j = -1
        for i in xrange(1, len(pattern)):
            while j > -1 and pattern[j + 1] != pattern[i]:
                j = prefix[j]
            if pattern[j + 1] == pattern[i]:
                j += 1
            prefix[i] = j
        return prefix