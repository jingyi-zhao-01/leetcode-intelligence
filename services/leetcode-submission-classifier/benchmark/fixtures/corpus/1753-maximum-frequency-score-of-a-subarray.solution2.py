# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-frequency-score-of-a-subarray
# source_path: LeetCode-Solutions-master/Python/maximum-frequency-score-of-a-subarray.py
# solution_class: Solution2
# submission_id: 356a43b3e0b4aba586cc2560e0f831354839d412
# seed: 2319391290

# Time:  O(n)
# Space: O(n)

import collections


# two pointers, sliding window freq table, hash table

class Solution2(object):
    def maxFrequencyScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        result = curr = 0
        cnt = collections.Counter()
        for i in xrange(len(nums)):
            if i >= k:
                curr = (curr-pow(nums[i-k], cnt[nums[i-k]], MOD))%MOD
                cnt[nums[i-k]] -= 1
                if cnt[nums[i-k]]:
                    curr = (curr+pow(nums[i-k], cnt[nums[i-k]], MOD))%MOD
            if cnt[nums[i]]:
               curr = (curr-pow(nums[i], cnt[nums[i]], MOD))%MOD
            cnt[nums[i]] += 1
            curr = (curr+pow(nums[i], cnt[nums[i]], MOD))%MOD
            if i >= k-1:
                result = max(result, curr)
        return result