# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: balanced-k-factor-decomposition
# source_path: LeetCode-Solutions-master/Python/balanced-k-factor-decomposition.py
# solution_class: Solution3
# submission_id: f3f1c0bb5c0d8f961f26932bb86abb25204543d0
# seed: 3292653875

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

class Solution3(object):
    def minDifference(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        def factors(n):
            for i in xrange(1, n+1):
                if i*i > n:
                    break
                if n%i:
                    continue
                yield i
                if n//i != i:
                    yield n//i

        def backtracking(remain):
            if len(curr) == k-1:
                curr.append(remain)
                if not result or max(result)-min(result) > max(curr)-min(curr):
                    result[:] = curr
                curr.pop()
                return
            for i in factors(remain):
                curr.append(i)
                backtracking(remain//i)
                curr.pop()
                    
        result, curr = [], []
        backtracking(n)
        return result