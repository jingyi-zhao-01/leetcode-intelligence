# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-frequency-after-subarray-operation
# source_path: LeetCode-Solutions-master/Python/maximum-frequency-after-subarray-operation.py
# solution_class: Solution
# submission_id: 7b11764398c09f3dc1d4addd015830011d55c300
# seed: 1705399458

# Time:  O(n)
# Space: O(n)

import collections


# freq table, dp

class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        cnt = collections.defaultdict(int)
        for x in nums:
            cnt[x] = max(cnt[x], cnt[k])+1
            result = max(result+int(x == k), cnt[x])
        return result