# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-profit-from-task-assignment
# source_path: LeetCode-Solutions-master/Python/maximize-profit-from-task-assignment.py
# solution_class: Solution
# submission_id: 3d846072ab075180bbe23bdf3b7a4d7ca49c1a5e
# seed: 2630180218

# Time:  O(n + tlogt)
# Space: O(n)

import collections


# freq table, sort, greedy

class Solution(object):
    def maxProfit(self, workers, tasks):
        """
        :type workers: List[int]
        :type tasks: List[List[int]]
        :rtype: int
        """
        cnt = collections.defaultdict(int)
        for x in workers:
            cnt[x] += 1
        tasks.sort(key=lambda x: x[1], reverse=True)
        result = 0
        k = 1
        for s, p in tasks:
            if cnt[s]:
                cnt[s] -= 1
                result += p
            elif k:
                k -= 1
                result += p
        return result