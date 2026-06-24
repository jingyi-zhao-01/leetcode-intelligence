# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-time-difference
# source_path: LeetCode-Solutions-master/Python/minimum-time-difference.py
# solution_class: Solution
# submission_id: ab23e0f76bf2ae56b792a1aef2b14e66ee604ab2
# seed: 1157500804

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minutes = map(lambda x: int(x[:2]) * 60 + int(x[3:]), timePoints)
        minutes.sort()
        return min((y - x) % (24 * 60)  \
                   for x, y in zip(minutes, minutes[1:] + minutes[:1]))