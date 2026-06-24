# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: goal-parser-interpretation
# source_path: LeetCode-Solutions-master/Python/goal-parser-interpretation.py
# solution_class: Solution
# submission_id: e53957ad814092e9c5478e311cd7fc1a05a3c548
# seed: 558155600

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        result, i = [], 0
        while i < len(command):
            if command[i] == 'G':
                result += ["G"]
                i += 1
            elif command[i] == '(' and command[i+1] == ')':
                result += ["o"]
                i += 2
            else:
                result += ["al"]
                i += 4
        return "".join(result)