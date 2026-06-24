# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: regular-expression-matching
# source_path: LeetCode-Solutions-master/Python/regular-expression-matching.py
# solution_class: Solution2
# submission_id: ac2227697e5b31e427e7a07ffea0d57873b5c36d
# seed: 967397341

# Time:  O(m * n)
# Space: O(n)

class Solution2(object):
    # @return a boolean
    def isMatch(self, s, p):
        result = [[False for j in xrange(len(p) + 1)] for i in xrange(len(s) + 1)]

        result[0][0] = True
        for i in xrange(2, len(p) + 1):
            if p[i-1] == '*':
                result[0][i] = result[0][i-2]

        for i in xrange(1,len(s) + 1):
            for j in xrange(1, len(p) + 1):
                if p[j-1] != '*':
                    result[i][j] = result[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                else:
                    result[i][j] = result[i][j-2] or (result[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))

        return result[len(s)][len(p)]