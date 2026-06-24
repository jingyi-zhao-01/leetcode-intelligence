# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-sum-of-distinct-subarrays-with-length-k
# source_path: LeetCode-Solutions-master/Python/maximum-sum-of-distinct-subarrays-with-length-k.py
# solution_class: Solution
# submission_id: 47014f956fd2fd1d41d454498c37e2e6c924123f
# seed: 620484752

# Time:  O(n)
# Space: O(k)

# two pointers

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = left = total = 0
        lookup = set()
        for right in xrange(len(nums)):
            while nums[right] in lookup or len(lookup) == k:
                lookup.remove(nums[left])
                total -= nums[left]
                left += 1
            lookup.add(nums[right])
            total += nums[right]
            if len(lookup) == k:
                result = max(result, total)
        return result