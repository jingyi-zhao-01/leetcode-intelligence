# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: repeated-substring-pattern
# source_path: LeetCode-Solutions-master/Python/repeated-substring-pattern.py
# solution_class: Solution
# submission_id: b3c82aef02965182a78afac9f31d6e552ef0d3b9
# seed: 2297983724

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
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

        prefix = getPrefix(str)
        return prefix[-1] != -1 and \
               (prefix[-1] + 1) % (len(str) - prefix[-1] - 1) == 0

    def repeatedSubstringPattern2(self, str):
        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False

        ss = (str + str)[1:-1]
        return ss.find(str) != -1