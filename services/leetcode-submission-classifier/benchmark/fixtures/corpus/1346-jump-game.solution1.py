# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: jump-game
# source_path: LeetCode-Solutions-master/Python/jump-game.py
# solution_class: Solution
# submission_id: 85a9098ee337b8baf7e301bc71e66aaff4979adc
# seed: 3207426293

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        reachable = 0
        for i, length in enumerate(A):
            if i > reachable:
                break
            reachable = max(reachable, i + length)
        return reachable >= len(A) - 1