# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-minimum-time-to-finish-all-jobs-ii
# source_path: LeetCode-Solutions-master/Python/find-minimum-time-to-finish-all-jobs-ii.py
# solution_class: Solution
# submission_id: d4bbfee68863e9020a77ff762849790ec5ae25de
# seed: 1576604601

# Time:  O(nlogn)
# Space: O(1)

import itertools


# greedy

class Solution(object):
    def minimumTime(self, jobs, workers):
        """
        :type jobs: List[int]
        :type workers: List[int]
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+(b-1))//b

        jobs.sort()
        workers.sort()
        return max(ceil_divide(j, w) for j, w in itertools.izip(jobs, workers))