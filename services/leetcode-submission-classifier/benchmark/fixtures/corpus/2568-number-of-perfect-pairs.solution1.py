# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-perfect-pairs
# source_path: LeetCode-Solutions-master/Python/number-of-perfect-pairs.py
# solution_class: Solution
# submission_id: d432ed7afd49c913305a57c33a21a7bcdfd708fc
# seed: 1826738086

# Time:  O(nlogn)
# Space: O(1)

# sort, two pointers, math

class Solution(object):
    def perfectPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)):
            nums[i] = abs(nums[i])
        nums.sort()
        result = left = 0
        for right in xrange(len(nums)):
            while not (nums[right]-nums[left] <= nums[left]):
                left += 1
            result += (right-left+1)-1
        return result