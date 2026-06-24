# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-days-without-meetings
# source_path: LeetCode-Solutions-master/Python/count-days-without-meetings.py
# solution_class: Solution
# submission_id: e61878e677b7ee51e0cff4c319967928cbdad97f
# seed: 1595855613

# Time:  O(nlogn)
# Space: O(1)

# sort

class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort()
        result = curr = 0
        for s, e in meetings:
            result += max((s-1)-curr, 0)
            curr = max(curr, e)
        result += days-curr
        return result