# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: destroying-asteroids
# source_path: LeetCode-Solutions-master/Python/destroying-asteroids.py
# solution_class: Solution
# submission_id: ee3da8eec7a5bd4f607e779981bba566fc7cdac1
# seed: 410534078

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()
        for x in asteroids:
            if x > mass:
                return False
            mass += min(x, asteroids[-1]-mass)
        return True