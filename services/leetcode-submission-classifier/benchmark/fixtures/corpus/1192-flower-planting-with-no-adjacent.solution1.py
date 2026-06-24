# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: flower-planting-with-no-adjacent
# source_path: LeetCode-Solutions-master/Python/flower-planting-with-no-adjacent.py
# solution_class: Solution
# submission_id: 4ee90e29109d72a7ca9f0cc44c3b955cbe8a41e1
# seed: 2949843973

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        result = [0]*N
        G = [[] for i in xrange(N)]
        for x, y in paths:
            G[x-1].append(y-1)
            G[y-1].append(x-1)
        for i in xrange(N):
            result[i] = ({1, 2, 3, 4} - {result[j] for j in G[i]}).pop()
        return result