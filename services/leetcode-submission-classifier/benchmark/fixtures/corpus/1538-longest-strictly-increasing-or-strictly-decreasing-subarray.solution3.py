# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-strictly-increasing-or-strictly-decreasing-subarray
# source_path: LeetCode-Solutions-master/Python/longest-strictly-increasing-or-strictly-decreasing-subarray.py
# solution_class: Solution3
# submission_id: 5d6581c5e68cc8bd7ea870637897e9b272146384
# seed: 2099500824

# Time:  O(n)
# Space: O(1)

# array

class Solution3(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def f(compare):
            result = l = 0
            for i in xrange(len(nums)):
                l += 1
                if i+1 == len(nums) or not compare(nums[i], nums[i+1]):
                    result = max(result, l)
                    l = 0
            return result

        return max(f(lambda x, y: x < y), f(lambda x, y: x > y))