# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-array-is-sorted-and-rotated
# source_path: LeetCode-Solutions-master/Python/check-if-array-is-sorted-and-rotated.py
# solution_class: Solution
# submission_id: c20dc515c3a2e0e1f94983b220bc113cd2466dfb
# seed: 3981693004

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in xrange(len(nums)):
            if nums[i] > nums[(i+1)%len(nums)]:
                count += 1
                if count > 1:
                    return False
        return True