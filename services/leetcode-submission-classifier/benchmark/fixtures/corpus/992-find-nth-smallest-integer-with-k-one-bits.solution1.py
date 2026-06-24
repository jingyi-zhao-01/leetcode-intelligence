# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-nth-smallest-integer-with-k-one-bits
# source_path: LeetCode-Solutions-master/Python/find-nth-smallest-integer-with-k-one-bits.py
# solution_class: Solution
# submission_id: 4469c7f6beee8ea2558e5017aeac21675cd9209d
# seed: 2574705837

# Time:  ctor:    O(r^2)
#        runtime: O(r)
# Space: O(r^2)

# dp, combinatorics
MAX_K = 50
DP = [[0]*(MAX_K+1) for _ in xrange(MAX_K+1)]
for i in xrange(MAX_K+1):
    DP[i][0] = 1
    for j in xrange(1, i+1):
        DP[i][j] = DP[i-1][j-1]+DP[i-1][j]

class Solution(object):
    def nthSmallest(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        result = 0
        for i in reversed(xrange(MAX_K)):
            if n <= DP[i][k]:
                continue
            n -= DP[i][k]
            result |= 1<<i
            k -= 1
            if not k:
                break
        return result