# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subarray-with-elements-greater-than-varying-threshold
# source_path: LeetCode-Solutions-master/Python/subarray-with-elements-greater-than-varying-threshold.py
# solution_class: Solution
# submission_id: 73370772d416c75cec210b3c91eda3afab6deb82
# seed: 2293963439

# Time:  O(n)
# Space: O(n)

# mono stack

class Solution(object):
    def validSubarraySize(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        stk = [-1]
        for i in xrange(len(nums)+1):
            while stk[-1] != -1 and (i == len(nums) or nums[stk[-1]] >= nums[i]):
                if nums[stk.pop()]*((i-1)-stk[-1]) > threshold:
                    return (i-1)-stk[-1]
            stk.append(i)
        return -1