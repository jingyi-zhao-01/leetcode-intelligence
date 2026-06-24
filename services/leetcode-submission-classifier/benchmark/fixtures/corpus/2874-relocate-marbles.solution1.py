# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: relocate-marbles
# source_path: LeetCode-Solutions-master/Python/relocate-marbles.py
# solution_class: Solution
# submission_id: dfa8087ca16fabcf54fdfa1cc47e28dd12850808
# seed: 1995399621

# Time:  O(nlogn)
# Space: O(n)

import itertools


# hash table, sort

class Solution(object):
    def relocateMarbles(self, nums, moveFrom, moveTo):
        """
        :type nums: List[int]
        :type moveFrom: List[int]
        :type moveTo: List[int]
        :rtype: List[int]
        """
        lookup = set(nums)
        for a, b in itertools.izip(moveFrom, moveTo):
            lookup.remove(a)
            lookup.add(b)
        return sorted(lookup)