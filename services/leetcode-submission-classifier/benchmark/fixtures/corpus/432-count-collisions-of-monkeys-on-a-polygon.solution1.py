# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-collisions-of-monkeys-on-a-polygon
# source_path: LeetCode-Solutions-master/Python/count-collisions-of-monkeys-on-a-polygon.py
# solution_class: Solution
# submission_id: b8a54ddbaa160e19253584a0a7136806603e3fb5
# seed: 3782819242

# Time:  O(logn)
# Space: O(1)

# combinatorics, fast exponentiation

class Solution(object):
    def monkeyMove(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        return (pow(2, n, MOD)-2)%MOD