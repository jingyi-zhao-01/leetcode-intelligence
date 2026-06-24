# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rotate-array
# source_path: LeetCode-Solutions-master/Python/rotate-array.py
# solution_class: Solution3
# submission_id: fcfcb4e13d33417741daf1644e05cb9a191960bf
# seed: 1060827209

# Time:  O(n)
# Space: O(1)

class Solution3(object):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    def rotate(self, nums, k):
        count = 0
        start = 0
        while count < len(nums):
            curr = start
            prev = nums[curr]
            while True:
                idx = (curr + k) % len(nums)
                nums[idx], prev = prev, nums[idx]
                curr = idx
                count += 1
                if start == curr:
                    break
            start += 1