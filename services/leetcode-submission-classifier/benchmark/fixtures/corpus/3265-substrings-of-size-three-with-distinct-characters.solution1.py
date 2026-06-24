# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: substrings-of-size-three-with-distinct-characters
# source_path: LeetCode-Solutions-master/Python/substrings-of-size-three-with-distinct-characters.py
# solution_class: Solution
# submission_id: a0da62799cc9eb33d4662fe49b417f5ed4564e50
# seed: 2306667251

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        K = 3

        result = 0
        count = collections.Counter()
        for i in xrange(len(s)):
            if i >= K:
                count[s[i-K]] -= 1
                if not count[s[i-K]]:
                    del count[s[i-K]]
            count[s[i]] += 1
            if len(count) == K:
                result += 1
        return result