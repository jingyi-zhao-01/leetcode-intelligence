# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-maximum-number-of-string-pairs
# source_path: LeetCode-Solutions-master/Python/find-maximum-number-of-string-pairs.py
# solution_class: Solution
# submission_id: 6b7454f1e8e2e340fe56933fa11479e31d400d69
# seed: 4011850060

# Time:  O(n)
# Space: O(1)

import collections


# freq table

class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        result = 0
        cnt = collections.Counter()
        for w in words:
            result += cnt[w[::-1]]
            cnt[w] += 1
        return result