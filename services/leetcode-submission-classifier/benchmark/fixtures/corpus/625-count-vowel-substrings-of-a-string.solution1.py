# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-vowel-substrings-of-a-string
# source_path: LeetCode-Solutions-master/Python/count-vowel-substrings-of-a-string.py
# solution_class: Solution
# submission_id: 9c2518a4297e4a69caf068124ae88eeb722ac441
# seed: 3319301844

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        VOWELS = set("aeiou")
        k = 5
        def atLeastK(word, k):
            cnt = collections.Counter()
            result = left = right = 0
            for i, c in enumerate(word):
                if c not in VOWELS:
                    cnt = collections.Counter()
                    left = right = i+1
                    continue
                cnt[c] += 1
                while len(cnt) > k-1:
                    cnt[word[right]] -= 1
                    if not cnt[word[right]]:
                        del cnt[word[right]]
                    right += 1
                result += right-left
            return result

        return atLeastK(word, k)