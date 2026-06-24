# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: k-radius-subarray-averages
# source_path: LeetCode-Solutions-master/Python/k-radius-subarray-averages.py
# solution_class: Solution
# submission_id: e8e08e04c770773c7f58789fa617ce2483fec95d
# seed: 2142932714

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        total, l = 0, 2*k+1
        result = [-1]*len(nums)
        for i in xrange(len(nums)):
            total += nums[i]
            if i-l >= 0:
                total -= nums[i-l]
            if i >= l-1:
                result[i-k] = total//l
        return result