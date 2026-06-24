# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-excellent-pairs
# source_path: LeetCode-Solutions-master/Python/number-of-excellent-pairs.py
# solution_class: Solution
# submission_id: df964041f0f74d7fda9a5b089b369b65765dbfab
# seed: 2809821837

# Time:  O(n + (logn)^2) = O(n)
# Space: O(n + logn) = O(n)

import collections


# bit manipulation, freq table, combinatorics

class Solution(object):
    def countExcellentPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def popcount(x):
            return bin(x)[2:].count('1')

        cnt = collections.Counter(popcount(x) for x in set(nums))
        return sum(cnt[i]*cnt[j] for i in cnt.iterkeys() for j in cnt.iterkeys() if i+j >= k)