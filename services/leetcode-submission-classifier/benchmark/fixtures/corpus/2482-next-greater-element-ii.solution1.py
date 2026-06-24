# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: next-greater-element-ii
# source_path: LeetCode-Solutions-master/Python/next-greater-element-ii.py
# solution_class: Solution
# submission_id: 2ba895f2c7bd5fa455b316da7911911a6f937074
# seed: 3030696514

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result, stk = [0] * len(nums), []
        for i in reversed(xrange(2*len(nums))):
            while stk and stk[-1] <= nums[i % len(nums)]:
                stk.pop()
            result[i % len(nums)] = stk[-1] if stk else -1
            stk.append(nums[i % len(nums)])
        return result