# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: split-the-array
# source_path: LeetCode-Solutions-master/Python/split-the-array.py
# solution_class: Solution
# submission_id: 3eee4eb86b306044bcb6c4d945784c71953a9393
# seed: 3175652853

# Time:  O(n)
# Space: O(n)

import collections


# freq table

class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return all(v <= 2 for v in collections.Counter(nums).itervalues())