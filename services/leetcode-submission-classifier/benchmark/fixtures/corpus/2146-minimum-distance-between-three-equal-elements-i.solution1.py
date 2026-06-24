# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-distance-between-three-equal-elements-i
# source_path: LeetCode-Solutions-master/Python/minimum-distance-between-three-equal-elements-i.py
# solution_class: Solution
# submission_id: be97d803e0aade4f4b1287159e0d89137da1f45e
# seed: 2958931983

# Time:  O(n)
# Space: O(n)

import collections


# hash table, sliding window

class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        INF = float("inf")
        result = INF
        lookup = collections.defaultdict(list)
        for i, x in enumerate(nums):
            lookup[x].append(i)
            if len(lookup[x]) < 3:
                continue
            result = min(result, 2*(i-lookup[x][-3]))  # k, j, i = lookup[x][:-3], (i-j)+(j-k)+(i-k) = 2*(i-k)
        return result if result != INF else -1