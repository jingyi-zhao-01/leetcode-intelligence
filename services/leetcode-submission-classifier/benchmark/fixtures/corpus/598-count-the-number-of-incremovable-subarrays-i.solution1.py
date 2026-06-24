# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-incremovable-subarrays-i
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-incremovable-subarrays-i.py
# solution_class: Solution
# submission_id: 98e53635d8bcc900169c0dc1792a8023a77ddf3e
# seed: 1687663510

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for j in reversed(xrange(1, len(nums))):
            if not nums[j-1] < nums[j]:
                break
        else:
            return (len(nums)+1)*len(nums)//2
        result = len(nums)-j+1
        for i in xrange(len(nums)-1):
            while j < len(nums) and not (nums[i] < nums[j]):
                j += 1
            result += len(nums)-j+1
            if not (nums[i] < nums[i+1]):
                break
        return result