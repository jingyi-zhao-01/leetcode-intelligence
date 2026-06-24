# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: stone-removal-game
# source_path: LeetCode-Solutions-master/Python/stone-removal-game.py
# solution_class: Solution
# submission_id: 28351ce617f932489485541e7b164c722e6513fd
# seed: 4040324047

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        c = 10
        # (c+(c-l+1))*l/2 <= n
        # l^2-(2*c+1)*l-2*n >= 0
        # l <= ((2*c+1)-((2*c+1)**2-8*n)**0.5)/2
        l = int(((2*c+1)-((2*c+1)**2-8*n)**0.5)/2)
        return l%2 == 1