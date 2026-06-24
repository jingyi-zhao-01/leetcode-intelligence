# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: bulb-switcher-iv
# source_path: LeetCode-Solutions-master/Python/bulb-switcher-iv.py
# solution_class: Solution
# submission_id: efaa23f3e46cf520983bd2b6bc10c17536de7e02
# seed: 825679651

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        result, curr = 0, '0'
        for c in target:
            if c == curr:
                continue
            curr = c
            result += 1
        return result