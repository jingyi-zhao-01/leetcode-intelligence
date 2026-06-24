# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: array-partition-i
# source_path: LeetCode-Solutions-master/Python/array-partition-i.py
# solution_class: Solution2
# submission_id: 6e8e65d04d490c95ea711b8c8ab3ab25a5b4033d
# seed: 1386382565

# Time:  O(r), r is the range size of the integers
# Space: O(r)

class Solution2(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in xrange(0, len(nums), 2):
            result += nums[i]
        return result