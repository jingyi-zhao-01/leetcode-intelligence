# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-missing-observations
# source_path: LeetCode-Solutions-master/Python/find-missing-observations.py
# solution_class: Solution2
# submission_id: 7368f64f96214420a74c7e46c8534a2cff2de7d2
# seed: 3230147705

# Time:  O(n)
# Space: O(1)

class Solution2(object):
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
        q, r = divmod(missing-MIN_V*n, (MAX_V-MIN_V))
        return [MAX_V if i < q else MIN_V+r if i == q else MIN_V  for i in xrange(n)]