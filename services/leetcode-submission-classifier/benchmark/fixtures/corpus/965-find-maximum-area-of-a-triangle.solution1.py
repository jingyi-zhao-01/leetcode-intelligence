# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-maximum-area-of-a-triangle
# source_path: LeetCode-Solutions-master/Python/find-maximum-area-of-a-triangle.py
# solution_class: Solution
# submission_id: 224cab02bda7eadb25f364ce63a44be7959eae53
# seed: 3419266658

# Time:  O(n)
# Space: O(n)

import collections


# math, hash table

class Solution(object):
    def maxArea(self, coords):
        """
        :type coords: List[List[int]]
        :rtype: int
        """
        mx_x = max(x for x, _ in coords)
        mn_x = min(x for x, _ in coords)
        mx_y = max(y for _, y in coords)
        mn_y = min(y for _, y in coords)
        lookup_mx_y = collections.defaultdict(lambda: float("-inf"))
        lookup_mn_y = collections.defaultdict(lambda: float("inf"))
        lookup_mx_x = collections.defaultdict(lambda: float("-inf"))
        lookup_mn_x = collections.defaultdict(lambda: float("inf"))
        for x, y in coords:
            lookup_mx_y[x] = max(lookup_mx_y[x], y)
            lookup_mn_y[x] = min(lookup_mn_y[x], y)
            lookup_mx_x[y] = max(lookup_mx_x[y], x)
            lookup_mn_x[y] = min(lookup_mn_x[y], x)
        result = max(max((lookup_mx_y[x]-lookup_mn_y[x])*max(x-mn_x, mx_x-x) for x in lookup_mx_y.iterkeys()),
                     max((lookup_mx_x[y]-lookup_mn_x[y])*max(y-mn_y, mx_y-y) for y in lookup_mx_x.iterkeys()))
        return result if result else -1