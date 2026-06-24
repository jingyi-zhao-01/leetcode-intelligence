# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-most-common-response
# source_path: LeetCode-Solutions-master/Python/find-the-most-common-response.py
# solution_class: Solution
# submission_id: 5c8fb4ddb20776453b582338c6da15d03f04bcec
# seed: 192821429

# Time:  O(n * l)
# Space: O(n * l)

import collections


# hash table, freq table

class Solution(object):
    def findCommonResponse(self, responses):
        """
        :type responses: List[List[str]]
        :rtype: str
        """
        cnt = collections.defaultdict(int)
        for r in responses:
            for x in set(r):
                cnt[x] += 1
        return min((-c, x) for x, c in cnt.iteritems())[1]