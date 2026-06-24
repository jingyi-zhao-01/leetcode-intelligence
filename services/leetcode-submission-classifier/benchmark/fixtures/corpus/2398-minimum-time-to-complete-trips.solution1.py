# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-time-to-complete-trips
# source_path: LeetCode-Solutions-master/Python/minimum-time-to-complete-trips.py
# solution_class: Solution
# submission_id: d6241e34945eed475561a5cade1124afe7958212
# seed: 164953786

# Time:  O(nlogr)
# Space: O(1)

# binary search

class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        def check(time, totalTrips, x):
            return sum(x//t for t in time) >= totalTrips

        left, right = 1, max(time)*totalTrips
        while left <= right:
            mid = left + (right-left)//2
            if check(time, totalTrips, mid):
                right = mid-1
            else:
                left = mid+1
        return left