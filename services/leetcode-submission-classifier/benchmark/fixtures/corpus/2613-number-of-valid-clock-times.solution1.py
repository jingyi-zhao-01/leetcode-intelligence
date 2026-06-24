# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-valid-clock-times
# source_path: LeetCode-Solutions-master/Python/number-of-valid-clock-times.py
# solution_class: Solution
# submission_id: 985a748500b6506f85bb2907a3d3bac28aad1667
# seed: 3428896946

# Time:  O(1)
# Space: O(1)

# combinatorics

class Solution(object):
    def countTime(self, time):
        """
        :type time: str
        :rtype: int
        """
        result = 1
        if time[4] == '?':
            result *= 10
        if time[3] == '?':
            result *= 6
        if time[1] == time[0] == '?':
            result *= 24
        elif time[1] == '?':
            result *= 10 if time[0] != '2' else 4
        elif time[0] == '?':
            result *= 3 if time[1] < '4' else 2
        return result