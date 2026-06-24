# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: simplified-fractions
# source_path: LeetCode-Solutions-master/Python/simplified-fractions.py
# solution_class: Solution
# submission_id: df8cfd6cfe4421486fa8eaedff558c0f0262a61b
# seed: 3841666574

# Time:  O(n^2 * logn)
# Space: O(n^2)

import fractions

class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lookup = set()
        for b in xrange(1, n+1):
            for a in xrange(1, b):
                g = fractions.gcd(a, b)
                lookup.add((a//g, b//g))
        return map(lambda x: "{}/{}".format(*x), lookup)