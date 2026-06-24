# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: substring-with-concatenation-of-all-words
# source_path: LeetCode-Solutions-master/Python/substring-with-concatenation-of-all-words.py
# solution_class: Solution2
# submission_id: 0e570759b774e1974b278ea754a5808c7894403b
# seed: 4078680226

# Time:  O((m + n) * k), where m is string length, n is dictionary size, k is word length
# Space: O(n * k)

import collections

class Solution2(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result, m, n, k = [], len(s), len(words), len(words[0])
        if m < n*k:
            return result

        lookup = collections.defaultdict(int)
        for i in words:
            lookup[i] += 1                            # Space: O(n * k)

        for i in xrange(m+1-k*n):                     # Time: O(m)
            cur, j = collections.defaultdict(int), 0
            while j < n:                              # Time: O(n)
                word = s[i+j*k:i+j*k+k]               # Time: O(k)
                if word not in lookup:
                    break
                cur[word] += 1
                if cur[word] > lookup[word]:
                    break
                j += 1
            if j == n:
                result.append(i)

        return result