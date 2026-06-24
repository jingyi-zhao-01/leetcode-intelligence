# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: swap-for-longest-repeated-character-substring
# source_path: LeetCode-Solutions-master/Python/swap-for-longest-repeated-character-substring.py
# solution_class: Solution
# submission_id: 52ca7a271ddaf9b91c286573e99769fd4ea2fe77
# seed: 738301774

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        K = 1
        result = 0
        total_count, count = collections.Counter(), collections.Counter()
        left, max_count = 0, 0
        for i in xrange(len(text)):
            total_count[text[i]] += 1
            count[text[i]] += 1
            max_count = max(max_count, count[text[i]])
            if i-left+1 - max_count > K:
                count[text[left]] -= 1
                left += 1
            result = max(result, min(i-left+1, total_count[text[i]]))
        return result