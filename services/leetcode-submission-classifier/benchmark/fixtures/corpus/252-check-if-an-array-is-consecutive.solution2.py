# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-an-array-is-consecutive
# source_path: LeetCode-Solutions-master/Python/check-if-an-array-is-consecutive.py
# solution_class: Solution2
# submission_id: dc7650f02d0bec98562c96e0c603a02680ae9ef8
# seed: 227089664

# Time:  O(n)
# Space: O(n)

# hash table

class Solution2(object):
    def isConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        return all(nums[i]+1 == nums[i+1] for i in xrange(len(nums)-1))