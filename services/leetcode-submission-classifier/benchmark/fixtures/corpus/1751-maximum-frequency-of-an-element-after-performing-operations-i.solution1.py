# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-frequency-of-an-element-after-performing-operations-i
# source_path: LeetCode-Solutions-master/Python/maximum-frequency-of-an-element-after-performing-operations-i.py
# solution_class: Solution
# submission_id: 55260e47315c2704d13e5c55d1e41a95d814de88
# seed: 2902143438

# Time:  O(nlogn)
# Space: O(n)

import collections


# sort, freq table, two pointers, sliding window

class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        nums.sort()
        result = 0
        left, right = 0, -1
        cnt = collections.defaultdict(int)
        for i in xrange(len(nums)):
            while right+1 < len(nums) and nums[right+1]-nums[i] <= k:
                cnt[nums[right+1]] += 1 
                right += 1
            while nums[i]-nums[left] > k:
                cnt[nums[left]] -= 1
                left += 1
            result = max(result, cnt[nums[i]]+min((right-left+1)-cnt[nums[i]], numOperations))
        left = 0
        for right in xrange(len(nums)):
            while nums[left]+k < nums[right]-k:
                left += 1
            result = max(result, min(right-left+1, numOperations))
        return result