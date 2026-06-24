# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-occurrences-of-a-substring
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-occurrences-of-a-substring.py
# solution_class: Solution2
# submission_id: 197a75ee34db2e9e78ba64c1f0420aa97af88b0a
# seed: 2257095174

# Time:  O(n)
# Space: O(n)

import collections


# rolling hash (Rabin-Karp Algorithm)

class Solution2(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        lookup = {}
        for right in xrange(minSize-1, len(s)):
            word = s[right-minSize+1:right+1]
            if word in lookup:
                lookup[word] += 1
            elif len(collections.Counter(word)) <= maxLetters:
                lookup[word] = 1
        return max(lookup.values() or [0])