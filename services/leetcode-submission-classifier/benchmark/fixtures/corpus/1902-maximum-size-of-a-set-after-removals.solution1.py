# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-size-of-a-set-after-removals
# source_path: LeetCode-Solutions-master/Python/maximum-size-of-a-set-after-removals.py
# solution_class: Solution
# submission_id: 2ffde96e96d960b503fd43ace42c189e1f4ede62
# seed: 1164098211

# Time:  O(n)
# Space: O(n)

# math, hash table, greedy

class Solution(object):
    def maximumSetSize(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        lookup1, lookup2 = set(nums1), set(nums2)
        n, c = len(nums1), len(lookup1&lookup2)
        d1, d2 = min(len(lookup1)-c, n//2), min(len(lookup2)-c, n//2)
        return min(n, d1+d2+c)