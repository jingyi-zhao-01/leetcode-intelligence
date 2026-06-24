# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-covered-intervals
# source_path: LeetCode-Solutions-master/Python/remove-covered-intervals.py
# solution_class: Solution
# submission_id: 06872fff178dc8950a3b69327b8593a4571f7116
# seed: 1351553954

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: [x[0], -x[1]])
        result, max_right = 0, 0
        for left, right in intervals:
            result += int(right > max_right)
            max_right = max(max_right, right)
        return result