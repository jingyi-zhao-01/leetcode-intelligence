# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-operations-to-make-arrays-similar
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-operations-to-make-arrays-similar.py
# solution_class: Solution
# submission_id: 6665c7f2c062406e0cc9534211dd147c830c94a9
# seed: 2021379383

# Time:  O(nlogn)
# Space: O(1)

import itertools


# greedy, sort

class Solution(object):
    def makeSimilar(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        nums.sort(key=lambda x: (x%2, x))
        target.sort(key=lambda x: (x%2, x))
        return sum(abs(x-y)//2 for x, y in itertools.izip(nums, target))//2