# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: special-array-i
# source_path: LeetCode-Solutions-master/Python/special-array-i.py
# solution_class: Solution
# submission_id: bf6e55c5d69707a53bc54f39e7854a88e779b11c
# seed: 921735503

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return all(nums[i]&1 != nums[i+1]&1 for i in xrange(len(nums)-1))