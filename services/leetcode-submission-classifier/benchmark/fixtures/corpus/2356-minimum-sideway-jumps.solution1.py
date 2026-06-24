# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-sideway-jumps
# source_path: LeetCode-Solutions-master/Python/minimum-sideway-jumps.py
# solution_class: Solution
# submission_id: 03a528089001a6dfad0d1d2545f5848a86693fc2
# seed: 1254056211

# Time:  O(n)
# Space: O(1)

# greedy solution

class Solution(object):
    def minSideJumps(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: int
        """
        result, lanes = 0, set([2])
        for i in xrange(len(obstacles)-1):
            lanes.discard(obstacles[i+1])
            if lanes:
                continue
            result += 1
            lanes = set(j for j in xrange(1, 4) if j not in [obstacles[i], obstacles[i+1]])
        return result