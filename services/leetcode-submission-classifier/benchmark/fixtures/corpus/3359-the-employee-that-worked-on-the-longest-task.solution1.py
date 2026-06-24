# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-employee-that-worked-on-the-longest-task
# source_path: LeetCode-Solutions-master/Python/the-employee-that-worked-on-the-longest-task.py
# solution_class: Solution
# submission_id: cccb9488df204f2964cfebc5b391c19fe3640699
# seed: 902056088

# Time:  O(l)
# Space: O(1)

# array

class Solution(object):
    def hardestWorker(self, n, logs):
        """
        :type n: int
        :type logs: List[List[int]]
        :rtype: int
        """
        return logs[max(xrange(len(logs)), key=lambda x: (logs[x][1]-(logs[x-1][1] if x-1 >= 0 else 0), -logs[x][0]))][0]