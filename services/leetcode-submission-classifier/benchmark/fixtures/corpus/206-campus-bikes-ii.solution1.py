# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: campus-bikes-ii
# source_path: LeetCode-Solutions-master/Python/campus-bikes-ii.py
# solution_class: Solution
# submission_id: 1ec3516c01739f16132de80480a4ffd6b78bf6ec
# seed: 3657750124

# Time:  O(w * b * 2^b)
# Space: O(b * 2^b)

# if w = b, we can even apply Hungarian algorithm (see https://en.wikipedia.org/wiki/Hungarian_algorithm),
# it can be improved to O(w^3), see https://github.com/t3nsor/codebook/blob/master/bipartite-mincost.cpp

class Solution(object):  # this is slower than Solution2 in python
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        dp = [[float("inf")]*((1<<len(bikes))) for _ in xrange(2)]
        dp[0][0] = 0
        for i in xrange(len(workers)):
            dp[(i+1)%2] = [float("inf")] * ((1<<len(bikes)))
            for j in xrange(len(bikes)):
                for taken in xrange((1<<len(bikes))):
                    if taken & (1<<j):
                        continue
                    dp[(i+1)%2][taken|(1<<j)] = \
                        min(dp[(i+1)%2][taken|(1<<j)],
                            dp[i%2][taken] +
                            manhattan(workers[i], bikes[j]))
        return min(dp[len(workers)%2])