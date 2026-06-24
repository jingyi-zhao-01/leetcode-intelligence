# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-a-subsequence
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-a-subsequence.py
# solution_class: Solution
# submission_id: 45acd8626d6288097304e2761f95038d58887009
# seed: 2581610129

# Time:  O(nlogn)
# Space: O(n)

import bisect

class Solution(object):
    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: int
        """
        lookup = {x:i for i, x in enumerate(target)}
        lis = []
        for x in arr:
            if x not in lookup:
                continue
            i = bisect.bisect_left(lis, lookup[x])
            if i == len(lis):
                lis.append(lookup[x])
            else:
                lis[i] = lookup[x]
        return len(target)-len(lis)