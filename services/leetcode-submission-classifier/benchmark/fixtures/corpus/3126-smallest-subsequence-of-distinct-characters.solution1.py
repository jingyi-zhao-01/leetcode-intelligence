# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-subsequence-of-distinct-characters
# source_path: LeetCode-Solutions-master/Python/smallest-subsequence-of-distinct-characters.py
# solution_class: Solution
# submission_id: a8e5416ead903bcf28cac7170df6898d7727c94d
# seed: 2511438123

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        count = collections.Counter(text)

        lookup, stk = set(), []
        for c in text:
            if c not in lookup:
                while stk and stk[-1] > c and count[stk[-1]]:
                    lookup.remove(stk.pop())
                stk += c
                lookup.add(c)
            count[c] -= 1
        return "".join(stk)