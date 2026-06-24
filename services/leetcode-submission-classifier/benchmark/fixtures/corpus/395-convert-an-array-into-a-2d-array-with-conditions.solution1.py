# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: convert-an-array-into-a-2d-array-with-conditions
# source_path: LeetCode-Solutions-master/Python/convert-an-array-into-a-2d-array-with-conditions.py
# solution_class: Solution
# submission_id: 8bdcf9ee74cf675ddacd3974c8ed960dca592536
# seed: 1572347407

# Time:  O(n)
# Space: O(n)

import collections


# freq table, constructive algorithms

class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        cnt = collections.Counter()
        for x in nums:
            if cnt[x] == len(result):
                result.append([])
            result[cnt[x]].append(x)
            cnt[x] += 1
        return result