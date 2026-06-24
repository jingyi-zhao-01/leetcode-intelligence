# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-sum-queries
# source_path: LeetCode-Solutions-master/Python/maximum-sum-queries.py
# solution_class: Solution
# submission_id: 60fcbef7b94578be80d275694afddc1571db447b
# seed: 176408045

# Time:  O(nlogn + mlogm + mlogn)
# Space: O(n + m)

import itertools
import bisect


# sort, mono stack, binary search

class Solution(object):
    def maximumSumQueries(self, nums1, nums2, queries):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        pairs = sorted(((i, j) for i, j in itertools.izip(nums1, nums2)))
        result = [0]*len(queries)
        stk = []
        for x, y, i in sorted(((x, y, i) for i, (x, y) in enumerate(queries)), reverse=True):
            while pairs and pairs[-1][0] >= x:
                a, b = pairs.pop()
                while stk and stk[-1][1] <= a+b:
                    stk.pop()
                if not stk or stk[-1][0] < b:
                    stk.append((b, a+b))
            j = bisect.bisect_left(stk, (y,))
            result[i] = stk[j][1] if j != len(stk) else -1
        return result