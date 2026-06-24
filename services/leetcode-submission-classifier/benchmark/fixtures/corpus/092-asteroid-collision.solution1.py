# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: asteroid-collision
# source_path: LeetCode-Solutions-master/Python/asteroid-collision.py
# solution_class: Solution
# submission_id: 6f9fe92cefe7056f2004c82aa57a9e9fb5a82e91
# seed: 711262845

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        result = []
        for x in asteroids:
            if x > 0:
                result.append(x)
                continue
            while result and 0 < result[-1] < -x:
                result.pop()
            if result and 0 < result[-1]:
                if result[-1] == -x:
                    result.pop()
                continue
            result.append(x)
        return result