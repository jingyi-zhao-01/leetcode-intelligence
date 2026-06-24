# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: most-profit-assigning-work
# source_path: LeetCode-Solutions-master/Python/most-profit-assigning-work.py
# solution_class: Solution
# submission_id: 0fe299f9e26c72c34aaccb58d265cda71220ae4d
# seed: 1016150717

# Time:  O(mlogm + nlogn), m is the number of workers,
#                        , n is the number of jobs
# Space: O(n)

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = zip(difficulty, profit)
        jobs.sort()
        worker.sort()
        result, i, max_profit = 0, 0, 0
        for ability in worker:
            while i < len(jobs) and jobs[i][0] <= ability:
                max_profit = max(max_profit, jobs[i][1])
                i += 1
            result += max_profit
        return result