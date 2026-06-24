# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-size-subarray-in-infinite-array
# source_path: LeetCode-Solutions-master/Python/minimum-size-subarray-in-infinite-array.py
# solution_class: Solution2
# submission_id: 7387714c92cc552cb249767fea8fcdad4447624d
# seed: 2341679051

# Time:  O(n)
# Space: O(1)

# two pointers, sliding window

class Solution2(object):
    def minSizeSubarray(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        INF = float("inf")
        q, target = divmod(target, sum(nums))
        if not target:
            return q*len(nums)
        result = INF
        lookup = {0:-1}
        prefix = 0
        for right in xrange((len(nums)-1)+(len(nums)-1)):
            prefix += nums[right%len(nums)]
            if prefix-target in lookup:
                result = min(result, right-lookup[prefix-target])
            lookup[prefix] = right
        return result+q*len(nums) if result != INF else -1