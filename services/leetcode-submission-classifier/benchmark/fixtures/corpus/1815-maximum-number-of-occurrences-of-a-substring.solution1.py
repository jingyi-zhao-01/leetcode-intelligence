# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-occurrences-of-a-substring
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-occurrences-of-a-substring.py
# solution_class: Solution
# submission_id: 5ab55afe18c6150d70d49f483b634e7420cc34ba
# seed: 1205891804

# Time:  O(n)
# Space: O(n)

import collections


# rolling hash (Rabin-Karp Algorithm)

class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        M, p = 10**9+7, 113
        power, rolling_hash = pow(p, minSize-1, M), 0

        left = 0
        lookup, count = collections.defaultdict(int), collections.defaultdict(int)
        for right in xrange(len(s)):
            count[s[right]] += 1
            if right-left+1 > minSize:
                count[s[left]] -= 1
                rolling_hash = (rolling_hash - ord(s[left])*power) % M
                if count[s[left]] == 0:
                    count.pop(s[left])
                left += 1
            rolling_hash = (rolling_hash*p + ord(s[right])) % M
            if right-left+1 == minSize and len(count) <= maxLetters:
                lookup[rolling_hash] += 1
        return max(lookup.values() or [0])