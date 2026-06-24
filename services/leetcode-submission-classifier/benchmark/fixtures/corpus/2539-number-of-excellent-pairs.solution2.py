# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-excellent-pairs
# source_path: LeetCode-Solutions-master/Python/number-of-excellent-pairs.py
# solution_class: Solution2
# submission_id: 66a22c7adcc65339065179e7a1dd012235019dbf
# seed: 3118101364

# Time:  O(n + (logn)^2) = O(n)
# Space: O(n + logn) = O(n)

import collections


# bit manipulation, freq table, combinatorics

class Solution2(object):
    def countExcellentPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def popcount(x):
            return bin(x)[2:].count('1')

        sorted_cnts = sorted(popcount(x) for x in set(nums))
        result = 0
        left, right = 0, len(sorted_cnts)-1
        while left <= right:
            if sorted_cnts[left]+sorted_cnts[right] < k:
                left += 1
            else:
                result += 1+2*((right-1)-left+1)
                right -= 1
        return result