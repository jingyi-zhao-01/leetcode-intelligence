# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: bulb-switcher-iii
# source_path: LeetCode-Solutions-master/Python/bulb-switcher-iii.py
# solution_class: Solution
# submission_id: 75ac6f0d77b62cadf87f7619599fd38b4c392a79
# seed: 164935297

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        result, right = 0, 0
        for i, num in enumerate(light, 1):
            right = max(right, num)
            result += (right == i)
        return result