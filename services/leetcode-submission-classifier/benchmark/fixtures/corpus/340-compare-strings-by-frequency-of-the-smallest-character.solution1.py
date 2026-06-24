# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: compare-strings-by-frequency-of-the-smallest-character
# source_path: LeetCode-Solutions-master/Python/compare-strings-by-frequency-of-the-smallest-character.py
# solution_class: Solution
# submission_id: b85dcb58aaf5f5a62307d94c2cf9c4fbca80d582
# seed: 3698827681

# Time:  O((m + n)logn), m is the number of queries, n is the number of words
# Space: O(n)

import bisect

class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        words_freq = sorted(word.count(min(word)) for word in words)
        return [len(words)-bisect.bisect_right(words_freq, query.count(min(query))) \
                for query in queries]