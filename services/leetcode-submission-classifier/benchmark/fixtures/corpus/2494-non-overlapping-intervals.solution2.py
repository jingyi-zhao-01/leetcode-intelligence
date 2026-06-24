# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: non-overlapping-intervals
# source_path: LeetCode-Solutions-master/Python/non-overlapping-intervals.py
# solution_class: Solution2
# submission_id: d0b86eb326670e678f57724c8e3b772ac6ebbe4c
# seed: 555382129

# Time:  O(nlogn)
# Space: O(1)

class Solution2(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda interval: interval[0])
        result, prev = 0, 0
        for i in xrange(1, len(intervals)):
            if intervals[i][0] < intervals[prev][1]:
                if intervals[i][1] < intervals[prev][1]:
                    prev = i
                result += 1
            else:
                prev = i
        return result