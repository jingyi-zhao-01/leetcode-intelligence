# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: partition-array-into-two-equal-product-subsets
# source_path: LeetCode-Solutions-master/Python/partition-array-into-two-equal-product-subsets.py
# solution_class: Solution
# submission_id: b72f6f1c8c7722938a4f70cb37c2f90b663b0d6c
# seed: 2398155919

# Time:  O(n * 2^n)
# Space: O(1)

# bitmasks

class Solution(object):
    def checkEqualPartitions(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        total = 1
        for x in nums:
            total *= x
            if total > target**2:
                return False
        if total != target**2:
            return False
        for mask in xrange(1, 1<<len(nums)-1):
            curr = 1
            for i in xrange(len(nums)):
                if not mask&(1<<i):
                    continue
                curr *= nums[i]
                if curr > target:
                    break
            if curr == target:
                return True
        return False