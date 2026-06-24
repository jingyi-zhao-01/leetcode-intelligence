# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-array-by-increasing-frequency
# source_path: LeetCode-Solutions-master/Python/sort-array-by-increasing-frequency.py
# solution_class: Solution
# submission_id: 634d58e263dac24851152526f0cd2fbe40cd0ab2
# seed: 2496045938

# Time:  O(nlogn)
# Space: O(n)

import collections

class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))