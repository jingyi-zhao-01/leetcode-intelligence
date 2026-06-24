# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-subarray-ranges
# source_path: LeetCode-Solutions-master/Python/sum-of-subarray-ranges.py
# solution_class: Solution
# submission_id: 6f3768ed45b3dbd10383dd171d3617f3508e46a4
# seed: 618515210

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        stk = []
        for i in xrange(len(nums)+1):
            x = nums[i] if i < len(nums) else float("inf")
            while stk and nums[stk[-1]] <= x:
                j = stk.pop()
                k = stk[-1] if stk else -1
                result += nums[j]*(j-k)*(i-j)
            stk.append(i)
        stk = []
        for i in xrange(len(nums)+1):
            x = nums[i] if i < len(nums) else float("-inf")
            while stk and nums[stk[-1]] >= x:
                j = stk.pop()
                k = stk[-1] if stk else -1
                result -= nums[j]*(j-k)*(i-j)
            stk.append(i)
        return result