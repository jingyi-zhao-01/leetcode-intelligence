# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-number-of-distinct-colors-among-the-balls
# source_path: LeetCode-Solutions-master/Python/find-the-number-of-distinct-colors-among-the-balls.py
# solution_class: Solution
# submission_id: a5037768605772695a9e9fc45da640b88e553c75
# seed: 2172400932

# Time:  O(q)
# Space: O(q)

import collections


# freq table

class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = [0]*len(queries)
        lookup = {}
        cnt = collections.Counter()
        for i, (x, y) in enumerate(queries):
            if x in lookup:
                cnt[lookup[x]] -= 1
                if not cnt[lookup[x]]:
                    del cnt[lookup[x]]
            lookup[x] = y
            cnt[lookup[x]] += 1
            result[i] = len(cnt)
        return result