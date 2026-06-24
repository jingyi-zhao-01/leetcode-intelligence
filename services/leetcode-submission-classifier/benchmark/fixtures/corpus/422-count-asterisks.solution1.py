# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-asterisks
# source_path: LeetCode-Solutions-master/Python/count-asterisks.py
# solution_class: Solution
# submission_id: 245013363d12ea1c65fe83f0629a7bb81d473cf8
# seed: 1491126631

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = cnt = 0
        for c in s:
            if c == '|':
                cnt = (cnt+1)%2
                continue
            if c == '*' and cnt == 0:
                result += 1
        return result