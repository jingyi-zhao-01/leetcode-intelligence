# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: select-cells-in-grid-with-maximum-score
# source_path: LeetCode-Solutions-master/Python/select-cells-in-grid-with-maximum-score.py
# solution_class: Solution2
# submission_id: 99a6f212c85b2922543dc022a69ba6a2c214670d
# seed: 2385005984

# Time:  O(n^2 * max(n, r)), r = max(x for row in grid for x in row)
# Space: O(n * max(n, r))

# hungarian algorithm, weighted bipartite matching

class Solution2(object):
    def maxScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        mx = max(x for row in grid for x in row)
        lookup = [set() for _ in xrange(mx)]
        for i, row in enumerate(grid):
            for x in row:
                lookup[x-1].add(i)
        dp = [float("-inf")]*(1<<len(grid))
        dp[0] = 0
        for x in xrange(len(lookup)):
            if not lookup[x]:
                continue
            for mask in reversed(xrange(len(dp))):
                for i in lookup[x]:
                    if mask&(1<<i):
                        continue
                    dp[mask|(1<<i)] = max(dp[mask|(1<<i)], dp[mask]+(x+1))
        return max(dp)