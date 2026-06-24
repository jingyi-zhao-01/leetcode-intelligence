# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-building-height
# source_path: LeetCode-Solutions-master/Python/maximum-building-height.py
# solution_class: Solution
# submission_id: 7f2a2f8aaf7f73d3ccc63984e76e13e0cda8d657
# seed: 1696702305

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        restrictions.extend([[1, 0], [n, n-1]])
        restrictions.sort()
        for i in reversed(xrange(len(restrictions)-1)):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1]+(restrictions[i+1][0]-restrictions[i][0]))
        result = 0
        for i in xrange(1, len(restrictions)):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1]+(restrictions[i][0]-restrictions[i-1][0]))
            left, h1 = restrictions[i-1]
            right, h2 = restrictions[i]
            result = max(result, max(h1, h2)+((right-left)-abs(h1-h2))//2)
        return result