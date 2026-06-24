# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-average-subarray-i
# source_path: LeetCode-Solutions-master/Python/maximum-average-subarray-i.py
# solution_class: Solution
# submission_id: 8b942be2c72a16b6284746330fd94f2f9344cf3c
# seed: 3927545485

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        result = total = sum(nums[:k])
        for i in xrange(k, len(nums)):
            total += nums[i] - nums[i-k]
            result = max(result, total)
        return float(result) / k