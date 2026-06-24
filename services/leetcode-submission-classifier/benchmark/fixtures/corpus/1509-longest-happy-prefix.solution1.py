# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-happy-prefix
# source_path: LeetCode-Solutions-master/Python/longest-happy-prefix.py
# solution_class: Solution
# submission_id: 05b7bd884f95964386cc3710c520feb9a9caaa58
# seed: 3808661858

# Time:  O(n)
# Space: O(n)

# kmp solution

class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        def getPrefix(pattern):
            prefix = [-1]*len(pattern)
            j = -1
            for i in xrange(1, len(pattern)):
                while j != -1 and pattern[j+1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix
        
        return s[:getPrefix(s)[-1]+1]