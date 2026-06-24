# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-unique-xor-triplets-i
# source_path: LeetCode-Solutions-master/Python/number-of-unique-xor-triplets-i.py
# solution_class: Solution
# submission_id: 72659606af14dbdab7ce32f1d1065cbc5a1c35f9
# seed: 3354263280

# Time:  O(logn)
# Space: O(1)

# bit manipulation, math

class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 1<<len(nums).bit_length() if len(nums) >= 3 else len(nums)