# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: non-overlapping-intervals
# source_path: LeetCode-Solutions-master/Python/non-overlapping-intervals.py
# solution_class: Solution
# submission_id: 0776ed3b92adcc199ba447940805725007354190
# seed: 887559256

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda interval: interval[1])
        result, right = 0, float("-inf")
        for l, r in intervals:
            if l < right:
                result += 1
            else:
                right = r
        return result