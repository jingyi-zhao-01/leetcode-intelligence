# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divide-array-into-equal-pairs
# source_path: LeetCode-Solutions-master/Python/divide-array-into-equal-pairs.py
# solution_class: Solution
# submission_id: 9fe36a4e34b42c5e433ad5e6b71b9bdd77509ade
# seed: 933122798

# Time:  O(n)
# Space: O(n)

import collections


# freq table

class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return all(cnt%2 == 0 for cnt in collections.Counter(nums).itervalues())