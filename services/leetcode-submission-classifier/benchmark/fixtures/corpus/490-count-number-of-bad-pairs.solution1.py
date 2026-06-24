# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-number-of-bad-pairs
# source_path: LeetCode-Solutions-master/Python/count-number-of-bad-pairs.py
# solution_class: Solution
# submission_id: 426cfa647da13fdd5a7d6ed30cd98b16b8cbe4f3
# seed: 3959308154

# Time:  O(n)
# Space: O(n)

import collections


# freq table

class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums)*(len(nums)-1)//2
        cnt = collections.Counter()
        for i, x in enumerate(nums):
            result -= cnt[x-i]
            cnt[x-i] += 1
        return result