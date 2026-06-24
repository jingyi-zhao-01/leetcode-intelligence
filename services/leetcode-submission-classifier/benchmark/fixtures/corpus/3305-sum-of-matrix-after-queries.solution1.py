# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-matrix-after-queries
# source_path: LeetCode-Solutions-master/Python/sum-of-matrix-after-queries.py
# solution_class: Solution
# submission_id: 000302bb847a62fddff3051bce59023f23b638d8
# seed: 2836005286

# Time:  O(n + q)
# Space: O(n)

# hash table

class Solution(object):
    def matrixSumQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: int
        """
        lookup = [[False]*n for _ in xrange(2)]
        cnt = [0]*2
        result = 0
        for t, i, v in reversed(queries):
            if lookup[t][i]:
                continue
            lookup[t][i] = True
            cnt[t] += 1
            result += v*(n-cnt[t^1])
        return result