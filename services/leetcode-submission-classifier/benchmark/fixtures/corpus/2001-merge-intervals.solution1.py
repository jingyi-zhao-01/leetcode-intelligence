# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: merge-intervals
# source_path: LeetCode-Solutions-master/Python/merge-intervals.py
# solution_class: Solution
# submission_id: 52f62e7a3eec551b339ebc0e2bc5a5a49fd2276e
# seed: 1969234073

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        result = []
        for interval in intervals:
            if not result or interval[0] > result[-1][1]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result