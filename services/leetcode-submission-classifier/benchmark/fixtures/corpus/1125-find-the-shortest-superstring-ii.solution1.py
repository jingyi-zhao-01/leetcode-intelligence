# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-shortest-superstring-ii
# source_path: LeetCode-Solutions-master/Python/find-the-shortest-superstring-ii.py
# solution_class: Solution
# submission_id: af5937f002a1dd7f715b65e14af449739f830231
# seed: 1003865041

# Time:  O(n + m)
# Space: O(n + m)

# kmp algorithm

class Solution(object):
    def shortestSuperstring(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: str
        """
        def getPrefix(pattern):
            prefix = [-1]*len(pattern)
            j = -1
            for i in xrange(1, len(pattern)):
                while j+1 > 0 and pattern[j+1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix

        def KMP(text, pattern):
            prefix = getPrefix(pattern)
            j = -1
            for i in xrange(len(text)):
                while j+1 > 0 and pattern[j+1] != text[i]:
                    j = prefix[j]
                if pattern[j+1] == text[i]:
                    j += 1
                if j+1 == len(pattern):
                    break
            return text+pattern[j+1:]  # modified
    
        result1 = KMP(s1, s2)
        result2 = KMP(s2, s1)
        return result1 if len(result1) < len(result2) else result2