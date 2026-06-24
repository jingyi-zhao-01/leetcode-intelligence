# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-vowel-substrings-of-a-string
# source_path: LeetCode-Solutions-master/Python/count-vowel-substrings-of-a-string.py
# solution_class: Solution2
# submission_id: 966dd8efa6ddf361e5e45e80f63d7dead76cb7ee
# seed: 3131875213

# Time:  O(n)
# Space: O(1)

import collections

class Solution2(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        VOWELS = set("aeiou")
        k = 5
        def atMostK(word, k):
            cnt = collections.Counter()
            result = left = 0
            for right, c in enumerate(word):
                if c not in VOWELS:
                    cnt = collections.Counter()
                    left = right+1
                    continue
                cnt[c] += 1
                while len(cnt) > k:
                    cnt[word[left]] -=1
                    if not cnt[word[left]]:
                        del cnt[word[left]]
                    left += 1
                result += right-left+1
            return result

        return atMostK(word, k) - atMostK(word, k-1)