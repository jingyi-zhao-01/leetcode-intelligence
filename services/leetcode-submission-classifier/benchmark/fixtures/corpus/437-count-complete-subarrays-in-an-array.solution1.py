# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-complete-subarrays-in-an-array
# source_path: LeetCode-Solutions-master/Python/count-complete-subarrays-in-an-array.py
# solution_class: Solution
# submission_id: b8d108ab36e4f15a53283cc49c87be53fbd5682b
# seed: 436379982

# Time:  O(n)
# Space: O(n)

import collections


# freq table, two pointers, sliding window

class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        result = left = 0
        cnt = collections.Counter()
        for right in xrange(len(nums)):
            cnt[nums[right]] += 1
            while len(cnt) == len(nums_set):
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            result += left
        return result