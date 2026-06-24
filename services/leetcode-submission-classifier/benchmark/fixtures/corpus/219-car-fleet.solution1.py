# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: car-fleet
# source_path: LeetCode-Solutions-master/Python/car-fleet.py
# solution_class: Solution
# submission_id: f15afb3098ca5f34203e4cf10bc2e9d36f2817ce
# seed: 2339895116

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        times = [float(target-p)/s for p, s in sorted(zip(position, speed))]
        result, curr = 0, 0
        for t in reversed(times):
            if t > curr:
                result += 1
                curr = t
        return result