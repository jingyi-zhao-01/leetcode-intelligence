# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-longest-self-contained-substring
# source_path: LeetCode-Solutions-master/Python/find-longest-self-contained-substring.py
# solution_class: Solution
# submission_id: 298f301aa718c2486713248889bbe9b8038dc83c
# seed: 3754763918

# Time:  O(n + 26^3 * logn)
# Space: O(n)

import bisect


# hash table, binary search

class Solution(object):
    def maxSubstringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        def check(left, right):
            for x in idxs:
                if not x or x[-1] < left or x[0] > right or (left <= x[0] and x[-1] <= right):
                    continue
                i = bisect.bisect_left(x, left)
                if i != len(x) and x[i] <= right:
                    return False
            return True

        idxs = [[] for _ in xrange(26)]
        for i, x in enumerate(s):
            idxs[ord(x)-ord('a')].append(i)
        result = -1
        for x in idxs:
            if not x:
                continue
            left = x[0]
            for y in idxs:
                if not y:
                    continue
                right = y[-1]
                if left <= right and result < right-left+1 != len(s) and check(left, right):
                    result = right-left+1
        return result