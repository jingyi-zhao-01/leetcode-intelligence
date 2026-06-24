# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-good-subarrays
# source_path: LeetCode-Solutions-master/Python/count-good-subarrays.py
# solution_class: Solution2
# submission_id: f03dfa891ea2d7fd4e9fb9e8f8ff7d9ae95a454d
# seed: 2986694531

# Time:  O(n)
# Space: O(n)

# combinatorics, mono stack

class Solution2(object):
    def countGoodSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def is_proper_subset(a, b):
            return a != b and a|b == b

        def is_subset(a, b):
            return a|b == b

        left = [-1]*len(nums)
        stk = []
        for i in reversed(xrange(len(nums))):
            while stk and not is_proper_subset(nums[i], nums[stk[-1]]):
                left[stk.pop()] = i
            stk.append(i)
        right = [len(nums)]*len(nums)
        stk = []
        for i in xrange(len(nums)):
            while stk and not is_subset(nums[i], nums[stk[-1]]):
                right[stk.pop()] = i
            stk.append(i)
        return sum((i-left[i])*(right[i]-i) for i in xrange(len(nums)))