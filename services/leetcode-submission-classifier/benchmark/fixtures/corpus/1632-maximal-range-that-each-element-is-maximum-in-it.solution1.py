# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximal-range-that-each-element-is-maximum-in-it
# source_path: LeetCode-Solutions-master/Python/maximal-range-that-each-element-is-maximum-in-it.py
# solution_class: Solution
# submission_id: 94248464841631d7a55f438fb9e84d10ed2207e1
# seed: 2276623018

# Time:  O(n)
# Space: O(n)

# mono stack

class Solution(object):
    def maximumLengthOfRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0]*len(nums)
        stk = [-1]
        nums.append(float("inf"))
        for i, x in enumerate(nums):
            while stk[-1] != -1 and nums[stk[-1]] < x:
                j = stk.pop()
                result[j] = (i-1)-stk[-1]
            stk.append(i)
        return result