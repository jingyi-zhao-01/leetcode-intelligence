# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-triangular-sum-of-an-array
# source_path: LeetCode-Solutions-master/Python/find-triangular-sum-of-an-array.py
# solution_class: Solution3
# submission_id: c9e13a62b8c0fdc10ce5ae74eb1be56585ccde26
# seed: 2577664035

# Time:  O(n)
# Space: O(1)

# combinatorics, number theory

class Solution3(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in reversed(xrange(len(nums))):
            for j in xrange(i):
                nums[j] = (nums[j]+nums[j+1])%10
        return nums[0]