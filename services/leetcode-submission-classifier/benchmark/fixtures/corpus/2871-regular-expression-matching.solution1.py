# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: regular-expression-matching
# source_path: LeetCode-Solutions-master/Python/regular-expression-matching.py
# solution_class: Solution
# submission_id: bc8ed593ab1788b9f13d99f85a54d573fdaaaf84
# seed: 2393415039

# Time:  O(m * n)
# Space: O(n)

class Solution(object):
    # @return a boolean
    def isMatch(self, s, p):
        k = 3
        result = [[False for j in xrange(len(p) + 1)] for i in xrange(k)]

        result[0][0] = True
        for i in xrange(2, len(p) + 1):
            if p[i-1] == '*':
                result[0][i] = result[0][i-2]

        for i in xrange(1,len(s) + 1):
            if i > 1:
                result[0][0] = False
            for j in xrange(1, len(p) + 1):
                if p[j-1] != '*':
                    result[i % k][j] = result[(i-1) % k][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                else:
                    result[i % k][j] = result[i % k][j-2] or (result[(i-1) % k][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))

        return result[len(s) % k][len(p)]