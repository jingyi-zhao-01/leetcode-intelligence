# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-distinct-subarrays-divisible-by-k-in-sorted-array
# source_path: LeetCode-Solutions-master/Python/count-distinct-subarrays-divisible-by-k-in-sorted-array.py
# solution_class: Solution
# submission_id: b2f01e9b7deb01013f388d50556c924fb37626a0
# seed: 3206187722

# Time:  O(n)
# Space: O(min(n, k))

import collections


# prefix sum, freq table

class Solution(object):
    def numGoodSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = prefix = 0
        cnt = collections.defaultdict(int)
        cnt[0] = 1
        i = 0
        while i < len(nums):
            j, prefix2 = i, prefix
            while j < len(nums) and nums[j] == nums[i]:
                prefix2 = (prefix2+nums[j])%k
                result += cnt[prefix2]
                j += 1
            while i < j:
                prefix = (prefix+nums[i])%k
                cnt[prefix] += 1
                i += 1
        return result