# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-binary-string-after-change
# source_path: LeetCode-Solutions-master/Python/maximum-binary-string-after-change.py
# solution_class: Solution
# submission_id: d1c5632bee71d7a98c2cd701fc101ab93b09cf2c
# seed: 3806254833

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def maximumBinaryString(self, binary):
        """
        :type binary: str
        :rtype: str
        """
        result = list(binary)
        zeros = ones = 0
        for i, c in enumerate(result):
            if c == '0':
                zeros += 1
            elif zeros == 0:
                ones += 1
            result[i] = '1'
        if ones != len(result):
            result[zeros+ones-1] = '0'
        return "".join(result)