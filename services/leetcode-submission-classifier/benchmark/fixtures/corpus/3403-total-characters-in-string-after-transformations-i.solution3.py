# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: total-characters-in-string-after-transformations-i
# source_path: LeetCode-Solutions-master/Python/total-characters-in-string-after-transformations-i.py
# solution_class: Solution3
# submission_id: b0a2df177156fabb0b24db2236e56f27560a0281
# seed: 4105217338

# Time:  precompute: O(t + 26)
#        runtime:    O(n)
# Space: O(t + 26)

# precompute, dp
MOD = 10**9+7
MAX_T = 10**5
DP = [0]*(MAX_T+26)
for i in xrange(26):
    DP[i] = 1
for i in xrange(26, len(DP)):
    DP[i] = (DP[i-26]+DP[(i-26)+1])%MOD

class Solution3(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :type nums: List[int]
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

        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        nums = [1]*26
        nums[-1] = 2
        matrix = [[0]*26 for _ in xrange(26)]
        for i in xrange(len(nums)):
            for j in xrange(1, nums[i]+1):
                matrix[i][(i+j)%26] = 1
        matrix_pow_t = matrix_expo(matrix, t)
        return reduce(lambda accu, x: (accu+x)%MOD, matrix_mult([cnt], matrix_pow_t)[0], 0)