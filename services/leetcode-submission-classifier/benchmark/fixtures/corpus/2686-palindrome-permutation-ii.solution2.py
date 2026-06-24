# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: palindrome-permutation-ii
# source_path: LeetCode-Solutions-master/Python/palindrome-permutation-ii.py
# solution_class: Solution2
# submission_id: b727baaf18bc311bdfe48099c07f9d248b681c77
# seed: 4157802850

# Time:  O(n * n!)
# Space: O(n)

import collections
import itertools

class Solution2(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cnt = collections.Counter(s)
        mid = tuple(k for k, v in cnt.iteritems() if v % 2)
        chars = ''.join(k * (v / 2) for k, v in cnt.iteritems())
        return [''.join(half_palindrome + mid + half_palindrome[::-1]) \
                for half_palindrome in set(itertools.permutations(chars))] if len(mid) < 2 else []