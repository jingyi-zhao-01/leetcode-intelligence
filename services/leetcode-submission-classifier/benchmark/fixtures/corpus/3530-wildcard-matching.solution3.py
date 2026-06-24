# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: wildcard-matching
# source_path: LeetCode-Solutions-master/Python/wildcard-matching.py
# solution_class: Solution3
# submission_id: 49c2566022e233181b6c263cce1a0b3f9f05ed56
# seed: 2463656919

# Time:  O(m + n) ~ O(m * n)
# Space: O(1)

# iterative solution with greedy

class Solution3(object):
    # @return a boolean
    def isMatch(self, s, p):
        result = [[False for j in xrange(len(p) + 1)] for i in xrange(len(s) + 1)]

        result[0][0] = True
        for i in xrange(1, len(p) + 1):
            if p[i-1] == '*':
                result[0][i] = result[0][i-1]
        for i in xrange(1,len(s) + 1):
            result[i][0] = False
            for j in xrange(1, len(p) + 1):
                if p[j-1] != '*':
                    result[i][j] = result[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    result[i][j] = result[i][j-1] or result[i-1][j]

        return result[len(s)][len(p)]