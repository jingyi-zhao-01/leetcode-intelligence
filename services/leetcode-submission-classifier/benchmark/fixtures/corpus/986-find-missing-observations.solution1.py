# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-missing-observations
# source_path: LeetCode-Solutions-master/Python/find-missing-observations.py
# solution_class: Solution
# submission_id: ca7d189d32b4f22ef0669734cc37fbe0a3ad8969
# seed: 78497182

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        MAX_V = 6
        MIN_V = 1
        total = sum(rolls)
        missing = mean*(n+len(rolls))-total
        if missing < MIN_V*n or missing > MAX_V*n:
            return []
        q, r = divmod(missing, n)
        return [q+int(i < r) for i in xrange(n)]