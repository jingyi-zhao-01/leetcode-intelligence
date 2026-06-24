# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: node-with-highest-edge-score
# source_path: LeetCode-Solutions-master/Python/node-with-highest-edge-score.py
# solution_class: Solution
# submission_id: 7d9022f5f74d60d8bf2e2cac70f3c5df7c2144b3
# seed: 333575549

# Time:  O(n)
# Space: O(n)

# freq table

class Solution(object):
    def edgeScore(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        score = [0]*len(edges)
        for u, v in enumerate(edges):
            score[v] += u
        return max(xrange(len(edges)), key=lambda x:score[x])