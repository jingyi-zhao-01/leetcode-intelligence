# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: furthest-point-from-origin
# source_path: LeetCode-Solutions-master/Python/furthest-point-from-origin.py
# solution_class: Solution
# submission_id: 4ee131328e216fffda9cb075ccf12c4e9b48220d
# seed: 931570929

# Time:  O(n)
# Space: O(1)

# math

class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        curr = cnt = 0
        for x in moves:
            if x == 'L':
                curr -= 1
            elif x == 'R':
                curr += 1
            else:
                cnt += 1
        return abs(curr)+cnt