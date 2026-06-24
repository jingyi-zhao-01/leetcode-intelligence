# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: scramble-string
# source_path: LeetCode-Solutions-master/Python/scramble-string.py
# solution_class: Solution
# submission_id: b52b9a9884c092992e4133cc73fdc6fc7f6a889e
# seed: 3841306063

# Time:  O(n^4)
# Space: O(n^3)

class Solution(object):
    # @return a boolean
    def isScramble(self, s1, s2):
        if not s1 or not s2 or len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        result = [[[False for j in xrange(len(s2))] for i in xrange(len(s1))] for n in xrange(len(s1) + 1)]
        for i in xrange(len(s1)):
            for j in xrange(len(s2)):
                if s1[i] == s2[j]:
                    result[1][i][j] = True

        for n in xrange(2, len(s1) + 1):
            for i in xrange(len(s1) - n + 1):
                for j in xrange(len(s2) - n + 1):
                    for k in xrange(1, n):
                        if result[k][i][j] and result[n - k][i + k][j + k] or\
                           result[k][i][j + n - k] and result[n - k][i + k][j]:
                            result[n][i][j] = True
                            break

        return result[n][0][0]