# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: meeting-rooms-ii
# source_path: LeetCode-Solutions-master/Python/meeting-rooms-ii.py
# solution_class: Solution2
# submission_id: 2dbf538a9db2f905c2fa5616dd57f4fbf9e9206f
# seed: 538861857

# Time:  O(nlogn)
# Space: O(n)

class Solution2(object):
    # @param {Interval[]} intervals
    # @return {integer}
    def minMeetingRooms(self, intervals):
        starts, ends = [], []
        for start, end in intervals:
            starts.append(start)
            ends.append(end)

        starts.sort()
        ends.sort()

        s, e = 0, 0
        min_rooms, cnt_rooms = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                cnt_rooms += 1  # Acquire a room.
                # Update the min number of rooms.
                min_rooms = max(min_rooms, cnt_rooms)
                s += 1
            else:
                cnt_rooms -= 1  # Release a room.
                e += 1

        return min_rooms