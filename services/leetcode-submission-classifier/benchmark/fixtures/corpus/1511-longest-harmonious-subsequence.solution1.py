# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-harmonious-subsequence
# source_path: LeetCode-Solutions-master/Python/longest-harmonious-subsequence.py
# solution_class: Solution
# submission_id: 8540531528c487f84a7ae4702d217b5136b908f4
# seed: 3742452903

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = collections.defaultdict(int)
        result = 0
        for num in nums:
            lookup[num] += 1
            for diff in [-1, 1]:
                if (num + diff) in lookup:
                    result = max(result, lookup[num] + lookup[num + diff])
        return result