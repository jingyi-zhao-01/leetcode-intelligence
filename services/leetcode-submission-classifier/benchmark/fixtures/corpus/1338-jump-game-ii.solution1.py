# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: jump-game-ii
# source_path: LeetCode-Solutions-master/Python/jump-game-ii.py
# solution_class: Solution
# submission_id: 87a648c8ff54dbddd178297925d6e8cdcf6eb5b8
# seed: 2367720402

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        jump_count = 0
        reachable = 0
        curr_reachable = 0
        for i, length in enumerate(A):
            if i > reachable:
                return -1
            if i > curr_reachable:
                curr_reachable = reachable
                jump_count += 1
            reachable = max(reachable, i + length)
        return jump_count