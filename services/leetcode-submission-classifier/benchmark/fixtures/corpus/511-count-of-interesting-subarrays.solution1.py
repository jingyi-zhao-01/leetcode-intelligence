# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-of-interesting-subarrays
# source_path: LeetCode-Solutions-master/Python/count-of-interesting-subarrays.py
# solution_class: Solution
# submission_id: d6c9a67a88eea956c7ed69b02cca0f781188ea1f
# seed: 2773551137

# Time:  O(n)
# Space: O(m)

import collections


# freq table, prefix sum

class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        cnt = collections.Counter([0])
        result = prefix = 0
        for x in nums:
            if x%modulo == k:
                prefix = (prefix+1)%modulo
            result += cnt[(prefix-k)%modulo]
            cnt[prefix] += 1
        return result