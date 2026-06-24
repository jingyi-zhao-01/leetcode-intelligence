# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: first-element-with-unique-frequency
# source_path: LeetCode-Solutions-master/Python/first-element-with-unique-frequency.py
# solution_class: Solution
# submission_id: 708f288a9105b9c56a7da37c622e74494847ff40
# seed: 812279513

# Time:  O(n)
# Space: O(n)

import collections


# freq table

class Solution(object):
    def firstUniqueFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.defaultdict(int)
        for x in nums:
            cnt[x] += 1
        cnt2 = collections.defaultdict(int)
        for v in cnt.itervalues():
            cnt2[v] += 1
        return next((x for x in nums if cnt2[cnt[x]] == 1), -1)