# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-longest-self-contained-substring
# source_path: LeetCode-Solutions-master/Python/find-longest-self-contained-substring.py
# solution_class: Solution5
# submission_id: c4d6c1c7d4977ecce1574627ff860cfadc2638e1
# seed: 2577812363

# Time:  O(n + 26^3 * logn)
# Space: O(n)

import bisect


# hash table, binary search

class Solution5(object):
    def maxSubstringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        def check(l, r):
            return all(l <= left[ord(s[i])-ord('a')] and right[ord(s[i])-ord('a')] <= r for i in xrange(l, r+1))

        left, right = [-1]*26, [-1]*26
        for i, x in enumerate(s):
            x = ord(x)-ord('a')
            if left[x] == -1:
                left[x] = i
            right[x] = i
        result = -1
        for l in left:
            if l == -1:
                continue
            for r in right:
                if r == -1:
                    continue
                if l <= r and result < r-l+1 != len(s) and check(l, r):
                    result = r-l+1
        return result