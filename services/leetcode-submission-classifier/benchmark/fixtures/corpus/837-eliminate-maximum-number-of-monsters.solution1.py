# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: eliminate-maximum-number-of-monsters
# source_path: LeetCode-Solutions-master/Python/eliminate-maximum-number-of-monsters.py
# solution_class: Solution
# submission_id: 938203d744655072f94e3c66e1d3ca7ac876a964
# seed: 3947781990

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        for i in xrange(len(dist)):
            dist[i] = (dist[i]-1)//speed[i]
        dist.sort()
        result = 0
        for i in xrange(len(dist)):
            if result > dist[i]:
                break
            result += 1
        return result