# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: most-frequent-even-element
# source_path: LeetCode-Solutions-master/Python/most-frequent-even-element.py
# solution_class: Solution
# submission_id: 2b41d39dfb51fe168b799a0dc0b40500cba6ee38
# seed: 3677815796

# Time:  O(n)
# Space: O(n)

import collections


# freq table

class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.Counter(x for x in nums if x%2 == 0)
        return max(cnt.iterkeys(), key=lambda x: (cnt[x], -x)) if cnt else -1