# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: compare-sums-of-bitonic-parts
# source_path: LeetCode-Solutions-master/Python/compare-sums-of-bitonic-parts.py
# solution_class: Solution
# submission_id: a4d62c75ca57f2b1ae125f033c99a65a9007dc40
# seed: 1524518406

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def compareBitonicSums(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for i in xrange(len(nums)-1):
            if nums[i] < nums[i+1]:
                total += nums[i]
            elif nums[i] > nums[i+1]:
                total -= nums[i+1]
        return 0 if total > 0 else 1 if total < 0 else -1