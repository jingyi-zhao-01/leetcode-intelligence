# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: average-height-of-buildings-in-each-segment
# source_path: LeetCode-Solutions-master/Python/average-height-of-buildings-in-each-segment.py
# solution_class: Solution
# submission_id: ea219bfe21c319000a1845e64f86561e3773648c
# seed: 3331501393

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def averageHeightOfBuildings(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        points = []
        for x, y, h in buildings:
            points.append((x, 1, h))
            points.append((y, -1, h))
        points.sort()
        result = []
        total = cnt = 0
        prev = -1
        for curr, c, h in points:
            if cnt and curr != prev:
                if result and result[-1][1] == prev and result[-1][2] == total//cnt:
                    result[-1][1] = curr
                else:
                    result.append([prev, curr, total//cnt])
            total += h*c
            cnt += c
            prev = curr
        return result