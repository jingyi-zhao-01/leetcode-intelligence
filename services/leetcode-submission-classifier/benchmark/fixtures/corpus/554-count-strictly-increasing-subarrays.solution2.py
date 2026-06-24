# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-strictly-increasing-subarrays
# source_path: LeetCode-Solutions-master/Python/count-strictly-increasing-subarrays.py
# solution_class: Solution2
# submission_id: 361a6c60b626379c6bb6122146d209919206a646
# seed: 1705257503

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution2(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = left = 0
        for right in xrange(len(nums)):
            if not (right-1 >= 0 and nums[right-1] < nums[right]):
                left = right
            result += right-left+1
        return result