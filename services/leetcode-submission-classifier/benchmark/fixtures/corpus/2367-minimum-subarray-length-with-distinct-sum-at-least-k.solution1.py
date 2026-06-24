# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-subarray-length-with-distinct-sum-at-least-k
# source_path: LeetCode-Solutions-master/Python/minimum-subarray-length-with-distinct-sum-at-least-k.py
# solution_class: Solution
# submission_id: cd94f6ba3eaf608f64d90868c36160a33059542c
# seed: 3378909430

# Time:  O(n)
# Space: O(n)

import collections


# freq table, two pointers

class Solution(object):
    def minLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        INF = float("inf")
        cnt = collections.defaultdict(int)
        result = INF
        left = curr = 0
        for right in xrange(len(nums)):
            cnt[nums[right]] += 1
            if cnt[nums[right]] == 1:
                curr += nums[right]
            while curr >= k:
                result = min(result, right-left+1)
                if cnt[nums[left]] == 1:
                    curr -= nums[left]
                cnt[nums[left]] -= 1
                left += 1
        return result if result is not INF else -1