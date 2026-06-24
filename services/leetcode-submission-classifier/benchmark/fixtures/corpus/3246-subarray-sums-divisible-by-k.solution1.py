# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subarray-sums-divisible-by-k
# source_path: LeetCode-Solutions-master/Python/subarray-sums-divisible-by-k.py
# solution_class: Solution
# submission_id: 24e8524539624d54665df042d5e6f3c62699fd97
# seed: 1177081738

# Time:  O(n)
# Space: O(k)

import collections

class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        count = collections.defaultdict(int)
        count[0] = 1
        result, prefix = 0, 0
        for a in A:
            prefix = (prefix+a) % K
            result += count[prefix]
            count[prefix] += 1
        return result