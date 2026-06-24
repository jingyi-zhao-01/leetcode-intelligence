# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rotate-array
# source_path: LeetCode-Solutions-master/Python/rotate-array.py
# solution_class: Solution2
# submission_id: da7082a71cb312d476912b1bb1d154c77ecca311
# seed: 3296235432

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    def rotate(self, nums, k):
        def apply_cycle_permutation(k, offset, cycle_len, nums):
            tmp = nums[offset]
            for i in xrange(1, cycle_len):
                nums[(offset + i * k) % len(nums)], tmp = tmp, nums[(offset + i * k) % len(nums)]
            nums[offset] = tmp

        k %= len(nums)
        num_cycles = gcd(len(nums), k)
        cycle_len = len(nums) / num_cycles
        for i in xrange(num_cycles):
            apply_cycle_permutation(k, i, cycle_len, nums)