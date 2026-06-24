# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: x-of-a-kind-in-a-deck-of-cards
# source_path: LeetCode-Solutions-master/Python/x-of-a-kind-in-a-deck-of-cards.py
# solution_class: Solution
# submission_id: ba6937727e874d08f2fb5becd31af73aaf2b9a2b
# seed: 689420189

# Time:  O(n * (logn)^2)
# Space: O(n)

import collections

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(a, b):  # Time: O((logn)^2)
            while b:
                a, b = b, a % b
            return a

        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2