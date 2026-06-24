# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: meeting-rooms
# source_path: LeetCode-Solutions-master/Python/meeting-rooms.py
# solution_class: Solution
# submission_id: d5e7b872f602370ecedc33d3b75f1ac741ba8d38
# seed: 3045929225

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key=lambda x: x[0])

        for i in xrange(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True