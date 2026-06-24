# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-values-at-indices-with-k-set-bits
# source_path: LeetCode-Solutions-master/Python/sum-of-values-at-indices-with-k-set-bits.py
# solution_class: Solution
# submission_id: c98e0c5af697342e79464e368bb85cc57e382c2c
# seed: 18865004

# Time:  O(C(ceil(log2(n)), k))
# Space: O(1)

# bit manipulation, hakmem-175

class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def next_popcount(n):  # reference: https://massivealgorithms.blogspot.com/2014/06/hakmem-item-175.html
            lowest_bit = n&-n
            left_bits = n+lowest_bit
            changed_bits = n^left_bits
            right_bits = (changed_bits//lowest_bit)>>2
            return left_bits|right_bits

        result = 0 
        i = (1<<k)-1
        while i < len(nums):
            result += nums[i]
            if i == 0:
                break
            i = next_popcount(i)
        return result