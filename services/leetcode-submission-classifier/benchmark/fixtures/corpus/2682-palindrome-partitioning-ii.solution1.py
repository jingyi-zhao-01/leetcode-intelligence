# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: palindrome-partitioning-ii
# source_path: LeetCode-Solutions-master/Python/palindrome-partitioning-ii.py
# solution_class: Solution
# submission_id: 1885ff214210497affad644860acba41a3813050
# seed: 447030183

# Time:  O(n^2)
# Space: O(n^2)

class Solution(object):
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        lookup = [[False for j in xrange(len(s))] for i in xrange(len(s))]
        mincut = [len(s) - 1 - i for i in xrange(len(s) + 1)]

        for i in reversed(xrange(len(s))):
            for j in xrange(i, len(s)):
                if s[i] == s[j]  and (j - i < 2 or lookup[i + 1][j - 1]):
                    lookup[i][j] = True
                    mincut[i] = min(mincut[i], mincut[j + 1] + 1)

        return mincut[0]