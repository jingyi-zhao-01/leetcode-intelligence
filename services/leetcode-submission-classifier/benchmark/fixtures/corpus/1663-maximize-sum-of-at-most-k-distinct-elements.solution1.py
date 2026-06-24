# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-sum-of-at-most-k-distinct-elements
# source_path: LeetCode-Solutions-master/Python/maximize-sum-of-at-most-k-distinct-elements.py
# solution_class: Solution
# submission_id: 0624f5ae319e039d4f912ad711477140b2df9c13
# seed: 2874099496

# Time:  O(nlogk)
# Space: O(k)

import heapq


# heap, sort

class Solution(object):
    def maxKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return heapq.nlargest(k, set(nums))