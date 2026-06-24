# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: calculate-score-after-performing-instructions
# source_path: LeetCode-Solutions-master/Python/calculate-score-after-performing-instructions.py
# solution_class: Solution
# submission_id: fb3b6c142d18de4089e66c41025dea3e6e944344
# seed: 2972551380

# Time:  O(n)
# Space: O(n)

# simulation

class Solution(object):
    def calculateScore(self, instructions, values):
        """
        :type instructions: List[str]
        :type values: List[int]
        :rtype: int
        """
        result = 0
        lookup = [False]*len(instructions)
        i = 0
        while 0 <= i < len(instructions):
            if lookup[i]:
                break
            lookup[i] = True
            if instructions[i] == "add":
                result += values[i]
                i += 1
            else:
                i += values[i]
        return result