# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-subarrays-with-maximum-bitwise-or
# source_path: LeetCode-Solutions-master/Python/smallest-subarrays-with-maximum-bitwise-or.py
# solution_class: Solution
# submission_id: 7b0c7edbf049fae49cb9a1a6b9f18c4a4f044e42
# seed: 1045031901

# Time:  O(n)
# Space: O(1)

# bitmasks, hash table

class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0]*len(nums)
        lookup = [-1]*max(max(nums).bit_length(), 1)
        for i in reversed(xrange(len(nums))):
            for bit in xrange(len(lookup)):
                if nums[i]&(1<<bit):
                    lookup[bit] = i
            result[i] = max(max(lookup)-i+1, 1)
        return result