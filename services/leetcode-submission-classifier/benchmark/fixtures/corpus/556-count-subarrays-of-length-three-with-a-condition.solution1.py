# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-subarrays-of-length-three-with-a-condition
# source_path: LeetCode-Solutions-master/Python/count-subarrays-of-length-three-with-a-condition.py
# solution_class: Solution
# submission_id: 2e0b3eca6682df48c30585f3a44e75d481882ea2
# seed: 1236693192

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum((nums[i-1]+nums[i+1])*2 == nums[i] for i in xrange(1, len(nums)-1))