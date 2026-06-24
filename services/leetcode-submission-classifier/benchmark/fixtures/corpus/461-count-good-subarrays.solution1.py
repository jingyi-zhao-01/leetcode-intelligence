# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-good-subarrays
# source_path: LeetCode-Solutions-master/Python/count-good-subarrays.py
# solution_class: Solution
# submission_id: 6eb27a923c5c2235a44d9eda56d3d78f5a47e67f
# seed: 2142999826

# Time:  O(n)
# Space: O(n)

# combinatorics, mono stack

class Solution(object):
    def countGoodSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def is_proper_subset(a, b):
            return a != b and a|b == b

        def is_subset(a, b):
            return a|b == b
        
        right = [len(nums)]*len(nums)
        stk = []
        for i in reversed(xrange(len(nums))):
            while stk and is_subset(nums[stk[-1]], nums[i]):
                stk.pop()
            right[i] = stk[-1] if stk else len(nums)
            stk.append(i)
        result, left = 0, -1
        stk = []
        for i in xrange(len(nums)):
            while stk and is_proper_subset(nums[stk[-1]], nums[i]):
                stk.pop()
            left = stk[-1] if stk else -1
            stk.append(i)
            result += (i-left)*(right[i]-i)
        return result