# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-beautiful-subarrays
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-beautiful-subarrays.py
# solution_class: Solution
# submission_id: f8b844fe5e9d255c82f3624bf7320be47eb37b13
# seed: 2572176414

# Time:  O(n)
# Space: O(n)

import collections


# freq table, combinatorics

class Solution(object):
    def beautifulSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.Counter()
        cnt[0] = 1
        result = curr = 0
        for x in nums:
            curr ^= x
            result += cnt[curr]
            cnt[curr] += 1
        return result