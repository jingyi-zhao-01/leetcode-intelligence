# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: meeting-rooms-ii
# source_path: LeetCode-Solutions-master/Python/meeting-rooms-ii.py
# solution_class: Solution3
# submission_id: c219d94e73f1557027c4f662d7377757c5833c0a
# seed: 3202337004

# Time:  O(nlogn)
# Space: O(n)

class Solution3(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        free_rooms = []
        
        heappush(free_rooms, intervals[0][1])
        for interval in intervals[1:]:
            if free_rooms[0] <= interval[0]:
                heappop(free_rooms)
            
            heappush(free_rooms, interval[1])
        
        return len(free_rooms)