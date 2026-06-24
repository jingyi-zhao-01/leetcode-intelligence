# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: next-greater-numerically-balanced-number
# source_path: LeetCode-Solutions-master/Python/next-greater-numerically-balanced-number.py
# solution_class: Solution3
# submission_id: fe472f07964371ed20dd9fc0f0d97c7d15c008d7
# seed: 4109476035

# Time:  O(logc) = O(1)
# Space: O(c) = O(1)

import bisect

class Solution3(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # obtained by manually enumerating min number of permutations in each length
        balanced = [1,
                    22,
                    122, 333,
                    1333, 4444,
                    14444, 22333, 55555,
                    122333, 155555, 224444, 666666]
        s = tuple(str(n))
        result = 1224444
        for x in balanced:
            x = tuple(str(x))
            if len(x) < len(s):
                continue
            if len(x) > len(s):
                result = min(result, int("".join(x)))
                continue
            for perm in itertools.permutations(x):  # not distinct permutations
                if perm > s:
                    result = min(result, int("".join(perm)))
        return result