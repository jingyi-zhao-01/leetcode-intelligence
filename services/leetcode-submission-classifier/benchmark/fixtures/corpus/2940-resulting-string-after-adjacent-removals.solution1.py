# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: resulting-string-after-adjacent-removals
# source_path: LeetCode-Solutions-master/Python/resulting-string-after-adjacent-removals.py
# solution_class: Solution
# submission_id: 6cad4c77154b3eace289ef7d18b98ee03eff7036
# seed: 2410524775

# Time:  O(n)
# Space: O(1)

# simulation, stack

class Solution(object):
    def resultingString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for x in s:
            if result:
                diff = abs(ord(x)-ord(result[-1]))
                if diff in (1, 25):
                    result.pop()
                    continue
            result.append(x)
        return "".join(result)