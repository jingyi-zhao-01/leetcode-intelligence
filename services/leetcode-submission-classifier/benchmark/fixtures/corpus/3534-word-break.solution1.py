# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: word-break
# source_path: LeetCode-Solutions-master/Python/word-break.py
# solution_class: Solution
# submission_id: 63880f36497482240b0ea47646258c8267188e9c
# seed: 3829461084

# Time:  O(n * l^2)
# Space: O(n)

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s)

        max_len = 0
        for string in wordDict:
            max_len = max(max_len, len(string))

        can_break = [False for _ in xrange(n + 1)]
        can_break[0] = True
        for i in xrange(1, n + 1):
            for l in xrange(1, min(i, max_len) + 1):
                if can_break[i-l] and s[i-l:i] in wordDict:
                    can_break[i] = True
                    break

        return can_break[-1]