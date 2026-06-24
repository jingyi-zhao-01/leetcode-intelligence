# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-maximum-number-of-fruits-collected
# source_path: LeetCode-Solutions-master/Python/find-the-maximum-number-of-fruits-collected.py
# solution_class: Solution
# submission_id: 370f5a7c07d7df98c7ef4dc4dfa15dfb7d7151f0
# seed: 3785601754

# Time:  O(n^2)
# Space: O(1)

# dp

class Solution(object):
    def maxCollectedFruits(self, fruits):
        """
        :type fruits: List[List[int]]
        :rtype: int
        """
        n = len(fruits)
        for i in xrange(n):
            for j in xrange(i+1, n-(i+1)):
                fruits[i][j] = 0
        for i in xrange(1, n-1):
            for j in xrange(i+1, n):
                fruits[i][j] += max(fruits[i-1][j-1], fruits[i-1][j], fruits[i-1][j+1] if j+1 < n else 0)
        for j in xrange(n):
            for i in xrange(j+1, n-(j+1)):
                fruits[i][j] = 0
        for j in xrange(1, n-1):
            for i in xrange(j+1, n):
                fruits[i][j] += max(fruits[i-1][j-1], fruits[i][j-1], fruits[i+1][j-1] if i+1 < n else 0)
        return sum(fruits[i][i] for i in xrange(n))+fruits[-2][-1]+fruits[-1][-2]