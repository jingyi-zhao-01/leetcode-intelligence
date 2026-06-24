# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: wildcard-matching
# source_path: LeetCode-Solutions-master/Python/wildcard-matching.py
# solution_class: Solution2
# submission_id: e8c1ea277dc6a19f6d95f086897cad4ace757524
# seed: 929282061

# Time:  O(m + n) ~ O(m * n)
# Space: O(1)

# iterative solution with greedy

class Solution2(object):
    # @return a boolean
    def isMatch(self, s, p):
        k = 2
        result = [[False for j in xrange(len(p) + 1)] for i in xrange(k)]

        result[0][0] = True
        for i in xrange(1, len(p) + 1):
            if p[i-1] == '*':
                result[0][i] = result[0][i-1]
        for i in xrange(1,len(s) + 1):
            result[i % k][0] = False
            for j in xrange(1, len(p) + 1):
                if p[j-1] != '*':
                    result[i % k][j] = result[(i-1) % k][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    result[i % k][j] = result[i % k][j-1] or result[(i-1) % k][j]

        return result[len(s) % k][len(p)]