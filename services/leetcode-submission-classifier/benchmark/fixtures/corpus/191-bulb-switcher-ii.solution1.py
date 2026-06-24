# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: bulb-switcher-ii
# source_path: LeetCode-Solutions-master/Python/bulb-switcher-ii.py
# solution_class: Solution
# submission_id: fee01aaf01c605630b6eec4cb9467cf3065d74f3
# seed: 1576089355

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m == 0:
            return 1
        if n == 1:
            return 2
        if m == 1 and n == 2:
            return 3
        if m == 1 or n == 2:
            return 4
        if m == 2:
            return 7
        return 8