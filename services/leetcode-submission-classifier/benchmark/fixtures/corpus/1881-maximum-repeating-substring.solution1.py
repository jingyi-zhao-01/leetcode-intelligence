# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-repeating-substring
# source_path: LeetCode-Solutions-master/Python/maximum-repeating-substring.py
# solution_class: Solution
# submission_id: ca26e43368ffc5e594c26058fc7360c580b06df8
# seed: 2937691678

# Time:  O(n), n is the length of sequence
# Space: O(m), m is the length of word

# optimized kmp solution

class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        def getPrefix(pattern):
            prefix = [-1] * len(pattern)
            j = -1
            for i in xrange(1, len(pattern)):
                while j > -1 and pattern[j + 1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix

        if len(sequence) < len(word):
            return 0

        prefix = getPrefix(word)
        result, count, j, prev = 0, 0, -1, -1
        for i in xrange(len(sequence)):
            while j > -1 and word[j+1] != sequence[i]:
                j = prefix[j]
            if word[j+1] == sequence[i]:
                j += 1
            if j+1 == len(word):     
                count = count+1 if i-prev == len(word) else 1
                result = max(result, count)
                j, prev = -1, i
        return result