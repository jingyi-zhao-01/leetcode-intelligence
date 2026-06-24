# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: most-beautiful-item-for-each-query
# source_path: LeetCode-Solutions-master/Python/most-beautiful-item-for-each-query.py
# solution_class: Solution
# submission_id: 25a7e9d1be53b767fd50bef8943235318232e872
# seed: 701703563

# Time:  O(nlogn + qlogn)
# Space: O(1)

import bisect

class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        items.sort()
        for i in xrange(len(items)-1):
            items[i+1][1] = max(items[i+1][1], items[i][1])
        result = []
        for q in queries:
            i = bisect.bisect_left(items, [q+1])
            result.append(items[i-1][1] if i else 0)
        return result