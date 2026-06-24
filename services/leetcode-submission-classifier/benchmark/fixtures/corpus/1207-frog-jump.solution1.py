# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: frog-jump
# source_path: LeetCode-Solutions-master/Python/frog-jump.py
# solution_class: Solution
# submission_id: 62801c782414e08c538a2bc03123ae6d3f871637
# seed: 1216540434

# Time:  O(n^2)
# Space: O(n^2)

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[1] != 1:
            return False

        last_jump_units = {s: set() for s in stones}
        last_jump_units[1].add(1)
        for s in stones[:-1]:
            for j in last_jump_units[s]:
                for k in (j-1, j, j+1):
                    if k > 0 and s+k in last_jump_units:
                        last_jump_units[s+k].add(k)
        return bool(last_jump_units[stones[-1]])