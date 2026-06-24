# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: string-transformation
# source_path: LeetCode-Solutions-master/Python/string-transformation.py
# solution_class: Solution2
# submission_id: 459664e6775e6dce000b2e6bbbda028e38d81ba1
# seed: 3042284085

# Time:  O(n + logk)
# Space: O(n)

# dp, math, kmp

class Solution2(object):
    def numberOfWays(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        def matrix_mult(A, B):
            ZB = zip(*B)
            return [[sum(a*b % MOD for a, b in itertools.izip(row, col)) % MOD for col in ZB] for row in A]
 
        def matrix_expo(A, K):
            result = [[int(i == j) for j in xrange(len(A))] for i in xrange(len(A))]
            while K:
                if K % 2:
                    result = matrix_mult(result, A)
                A = matrix_mult(A, A)
                K /= 2
            return result

        def getPrefix(pattern):
            prefix = [-1]*len(pattern)
            j = -1
            for i in xrange(1, len(pattern)):
                while j+1 > 0 and pattern[j+1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix

        def KMP(text, pattern):
            prefix = getPrefix(pattern)
            j = -1
            for i in xrange(len(text)):
                while j+1 > 0 and pattern[j+1] != text[i]:
                    j = prefix[j]
                if pattern[j+1] == text[i]:
                    j += 1
                if j+1 == len(pattern):
                    yield i-j
                    j = prefix[j]

        n = len(s)
        T = [[0, 1],
             [n-1, (n-1)-1]]
        dp = [1, 0]
        dp = matrix_mult([dp], matrix_expo(T, k))[0]  # [dp[0], dp[1]] * T^k
        return reduce(lambda a, b: (a+b)%MOD, (dp[int(i != 0)] for i in KMP(s+s[:-1], t)), 0)