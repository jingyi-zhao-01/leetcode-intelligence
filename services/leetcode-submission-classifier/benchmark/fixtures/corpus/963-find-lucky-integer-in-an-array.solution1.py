# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-lucky-integer-in-an-array
# source_path: LeetCode-Solutions-master/Python/find-lucky-integer-in-an-array.py
# solution_class: Solution
# submission_id: 25a8315507a2ec18f5e3a5ee81810c7106ce8f3e
# seed: 3719953965

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = collections.Counter(arr)
        result = -1
        for k, v in count.iteritems():
            if k == v:
                result = max(result, k)
        return result