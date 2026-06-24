# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-elements-with-maximum-frequency
# source_path: LeetCode-Solutions-master/Python/count-elements-with-maximum-frequency.py
# solution_class: Solution
# submission_id: 4cff821dc9a55fdd22ccda8b45ec3b33b03f26fb
# seed: 1978487324

# Time:  O(n)
# Space: O(n)

import collections


# freq table

class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.Counter(nums)
        mx = max(cnt.itervalues())
        return sum(v for v in cnt.itervalues() if v == mx)