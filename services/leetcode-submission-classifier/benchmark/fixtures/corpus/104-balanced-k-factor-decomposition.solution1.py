# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: balanced-k-factor-decomposition
# source_path: LeetCode-Solutions-master/Python/balanced-k-factor-decomposition.py
# solution_class: Solution
# submission_id: ac83002b83eba14b521961a624168566836cce38
# seed: 204963303

# Time:  precompute: O(rlogr)
#        runtime:    O(k * (logn)^(k - 1))
# Space: O(rlogr)

import bisect


# backtracking, number theory
def factors(n):
    result = [[] for _ in xrange(n+1)]
    for i in xrange(1, n+1):
        for j in range(i, n+1, i):
            result[j].append(i)
    return result


MAX_N = 10**5
FACTORS = factors(MAX_N)

class Solution(object):
    def minDifference(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        def backtracking(remain):
            start = curr[-1] if curr else 1
            if len(curr) == k-1 and remain >= start:
                curr.append(remain)
                if not result or result[-1]-result[0] > curr[-1]-curr[0]:
                    result[:] = curr
                curr.pop()
                return
            factors = FACTORS[remain]
            for i in xrange(bisect.bisect_left(factors, start), len(factors)):
                curr.append(factors[i])
                backtracking(remain//factors[i])
                curr.pop()
                    
        result, curr = [], []
        backtracking(n)
        return result    