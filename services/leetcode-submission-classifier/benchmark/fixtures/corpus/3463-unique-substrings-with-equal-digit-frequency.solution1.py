# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: unique-substrings-with-equal-digit-frequency
# source_path: LeetCode-Solutions-master/Python/unique-substrings-with-equal-digit-frequency.py
# solution_class: Solution
# submission_id: 83a308770fea4bdd086cc22522c60197dafd9b6e
# seed: 4158546580

# Time:  O(n^2)
# Space: O(n^2)

import collections


# rolling hash

class Solution(object):
    def equalDigitFrequency(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9+7
        D = 27
        lookup = set()
        for i in xrange(len(s)):
            cnt = collections.Counter()
            h = max_cnt = 0
            for j in xrange(i, len(s)):
                d = ord(s[j])-ord('0')+1
                h = (h*D+d)%MOD
                cnt[d] += 1
                max_cnt = max(max_cnt, cnt[d])
                if len(cnt)*max_cnt == j-i+1:
                    lookup.add(h)
        return len(lookup)