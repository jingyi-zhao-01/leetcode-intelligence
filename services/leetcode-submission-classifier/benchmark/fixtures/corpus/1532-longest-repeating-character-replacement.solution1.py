# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-repeating-character-replacement
# source_path: LeetCode-Solutions-master/Python/longest-repeating-character-replacement.py
# solution_class: Solution
# submission_id: f61a7d01bc9925b7c542ccffb57c61b4d7841b21
# seed: 2870253358

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result, max_count = 0, 0
        count = collections.Counter()
        for i in xrange(len(s)):
            count[s[i]] += 1
            max_count = max(max_count, count[s[i]])
            if result - max_count >= k:
                count[s[i-result]] -= 1
            else:
                result += 1
        return result