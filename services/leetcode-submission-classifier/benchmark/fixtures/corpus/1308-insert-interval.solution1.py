# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: insert-interval
# source_path: LeetCode-Solutions-master/Python/insert-interval.py
# solution_class: Solution
# submission_id: 2f75a661a2bf562ba371ec73787885a57b33465e
# seed: 81150130

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i = 0
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            result += intervals[i],
            i += 1
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval = [min(newInterval[0], intervals[i][0]),
                           max(newInterval[1], intervals[i][1])]
            i += 1
        result.append(newInterval)
        result.extend(intervals[i:])
        return result