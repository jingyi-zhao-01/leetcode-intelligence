# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-nice-substring
# source_path: LeetCode-Solutions-master/Python/longest-nice-substring.py
# solution_class: Solution
# submission_id: 6d70542b41566ba3092ddf83ca62315cd26f2251
# seed: 1894842516

# Time:  O(26 * n) = O(n)
# Space: O(26 * n) = O(n)

class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        lookup = set(list(s))
        prev = -1
        result = ""
        for i in xrange(len(s)+1):
            if not (i == len(s) or s[i] not in lookup or s[i].swapcase() not in lookup):
                continue
            if prev == -1 and i == len(s):
                return s
            tmp = self.longestNiceSubstring(s[prev+1:i])
            if len(tmp) > len(result):
                result = tmp
            prev = i
        return result