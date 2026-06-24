# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: double-modular-exponentiation
# source_path: LeetCode-Solutions-master/Python/double-modular-exponentiation.py
# solution_class: Solution
# submission_id: 8cb70602c284a514e58ecc6fec110c25dc0abbea
# seed: 2835478645

# Time:  O(n * (logb + logc))
# Space: O(1)

# fast exponentiation

class Solution(object):
    def getGoodIndices(self, variables, target):
        """
        :type variables: List[List[int]]
        :type target: int
        :rtype: List[int]
        """
        return [i for i, (a, b, c, m) in enumerate(variables) if pow(pow(a, b, 10), c, m) == target]