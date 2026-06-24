# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: elimination-game
# source_path: LeetCode-Solutions-master/Python/elimination-game.py
# solution_class: Solution
# submission_id: df134cd0caa5a8c8003681641fa035f1967c827d
# seed: 1533934200

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, step, direction = 1, 2, 1
        while n > 1:
            start += direction * (step * (n//2) - step//2)
            n //= 2
            step *= 2
            direction *= -1
        return start