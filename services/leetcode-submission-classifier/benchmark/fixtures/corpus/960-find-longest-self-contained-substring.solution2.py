# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-longest-self-contained-substring
# source_path: LeetCode-Solutions-master/Python/find-longest-self-contained-substring.py
# solution_class: Solution2
# submission_id: 0272b9a2465cd8626d9962ce04840c7d08b72aa2
# seed: 568106100

# Time:  O(n + 26^3 * logn)
# Space: O(n)

import bisect


# hash table, binary search

class Solution2(object):
    def maxSubstringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        def check(left, right):
            for x in idxs:
                if not x:
                    continue
                l = bisect.bisect_left(x, left)
                r = bisect.bisect_right(x, right)-1
                if not (r-l+1 == len(x) or r-l+1 == 0):
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
                if left <= right and right-left+1 != len(s) and check(left, right):
                    result = max(result, right-left+1)
        return result