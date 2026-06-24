# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rotate-string
# source_path: LeetCode-Solutions-master/Python/rotate-string.py
# solution_class: Solution2
# submission_id: 78534f72db0791691d501e2ad405e9de2d70754e
# seed: 3955127479

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        def strStr(haystack, needle):
            def KMP(text, pattern):
                prefix = getPrefix(pattern)
                j = -1
                for i in xrange(len(text)):
                    while j > -1 and pattern[j + 1] != text[i]:
                        j = prefix[j]
                    if pattern[j + 1] == text[i]:
                        j += 1
                    if j == len(pattern) - 1:
                        return i - j
                return -1

            def getPrefix(pattern):
                prefix = [-1] * len(pattern)
                j = -1
                for i in xrange(1, len(pattern)):
                    while j > -1 and pattern[j + 1] != pattern[i]:
                        j = prefix[j]
                    if pattern[j + 1] == pattern[i]:
                        j += 1
                    prefix[i] = j
                return prefix

            if not needle:
                return 0
            return KMP(haystack, needle)

        if len(A) != len(B):
            return False
        return strStr(A*2, B) != -1