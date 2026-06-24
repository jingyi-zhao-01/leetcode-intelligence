# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: asteroid-collision
# source_path: LeetCode-Solutions-master/Python/asteroid-collision.py
# solution_class: Solution2
# submission_id: 614b678ec0deae0dd67cde54533fb0535a08a54e
# seed: 2883492922

# Time:  O(n)
# Space: O(n)

class Solution2(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        result = []
        for x in asteroids:
            while result and x < 0 < result[-1]:
                if result[-1] < -x:
                    result.pop()
                    continue
                elif result[-1] == -x:
                    result.pop()
                break
            else:
                result.append(x)
        return result