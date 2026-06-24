# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: convert-an-array-into-a-2d-array-with-conditions
# source_path: LeetCode-Solutions-master/Python/convert-an-array-into-a-2d-array-with-conditions.py
# solution_class: Solution2
# submission_id: 3ad678ff46eb2738cd592677df78ed17ef6e1af1
# seed: 1801217192

# Time:  O(n)
# Space: O(n)

import collections


# freq table, constructive algorithms

class Solution2(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        cnt = collections.Counter(nums)
        while cnt:
            result.append(cnt.keys())
            cnt = {k:v-1 for k, v in cnt.iteritems() if v-1}
        return result