# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: palindrome-pairs
# source_path: LeetCode-Solutions-master/Python/palindrome-pairs.py
# solution_class: Solution
# submission_id: 79e2eb1893adacdc3a414e63ebe37e6f031bbb82
# seed: 1630942162

# Time:  O(n * k^2), n is the number of the words, k is the max length of the words.
# Space: O(n * k)

import collections

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
 
        res = []
        lookup = collections.defaultdict(dict)
        for i, word in enumerate(words):
            lookup[len(word)][word] = i

        for i in xrange(len(words)):
            for j in xrange(len(words[i]) + 1):
                if j in lookup and is_palindrome(words[i], j, len(words[i])-1):
                    suffix = words[i][:j][::-1]
                    bucket = lookup[len(suffix)]
                    if suffix in bucket and bucket[suffix] != i:
                        res.append([i, bucket[suffix]])
                if j > 0 and len(words[i])-j in lookup and is_palindrome(words[i], 0, j-1):
                    prefix = words[i][j:][::-1]
                    bucket = lookup[len(prefix)]
                    if prefix in bucket and bucket[prefix] != i:
                        res.append([bucket[prefix], i])
        return res