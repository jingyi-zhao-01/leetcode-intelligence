# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: abbreviating-the-product-of-a-range
# source_path: LeetCode-Solutions-master/Python/abbreviating-the-product-of-a-range.py
# solution_class: Solution
# submission_id: d0405ee7835dd0b7168fb5db266e8a635e83e31c
# seed: 697128458

# Time:  O(r - l)
# Space: O(1)

import math

class Solution(object):
    def abbreviateProduct(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: str
        """
        PREFIX_LEN = SUFFIX_LEN = 5
        MOD = 10**(PREFIX_LEN+SUFFIX_LEN)
        curr, zeros = 1, 0
        abbr = False
        for i in xrange(left, right+1):
            curr *= i
            while not curr%10:
                curr //= 10
                zeros += 1
            q, curr = divmod(curr, MOD)
            if q:
                abbr = True
        if not abbr:
            return "%se%s" % (curr, zeros)
        decimal = reduce(lambda x, y: (x+y)%1, (math.log10(i) for i in xrange(left, right+1)))
        prefix = str(int(10**(decimal+(PREFIX_LEN-1))))
        suffix = str(curr % 10**SUFFIX_LEN).zfill(SUFFIX_LEN)
        return "%s...%se%s" % (prefix, suffix, zeros)