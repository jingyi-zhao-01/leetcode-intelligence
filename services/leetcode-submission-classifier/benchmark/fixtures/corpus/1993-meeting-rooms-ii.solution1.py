# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: meeting-rooms-ii
# source_path: LeetCode-Solutions-master/Python/meeting-rooms-ii.py
# solution_class: Solution
# submission_id: ce7913c570e594d464a9c07410703e17fc8803fb
# seed: 1255196691

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    # @param {Interval[]} intervals
    # @return {integer}
    def minMeetingRooms(self, intervals):
        result, curr = 0, 0
        line = [x for i, j in intervals for x in [[i, 1], [j, -1]]]
        line.sort()
        for _, num in line:
            curr += num
            result = max(result, curr)
        return result