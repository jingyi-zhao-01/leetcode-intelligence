# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-values-at-indices-with-k-set-bits
# source_path: LeetCode-Solutions-master/Python/sum-of-values-at-indices-with-k-set-bits.py
# solution_class: Solution2
# submission_id: 6d7ff5197b9bac51bf1caaea3deec40ffd2b3e9e
# seed: 2274541586

# Time:  O(C(ceil(log2(n)), k))
# Space: O(1)

# bit manipulation, hakmem-175

class Solution2(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def popcount(x):
            return bin(x)[1:].count('1')
        
        return sum(x for i, x in enumerate(nums) if popcount(i) == k)