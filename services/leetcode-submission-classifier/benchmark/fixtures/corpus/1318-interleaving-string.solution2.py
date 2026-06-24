# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: interleaving-string
# source_path: LeetCode-Solutions-master/Python/interleaving-string.py
# solution_class: Solution2
# submission_id: f9a5a1500474b0f6f6a7efe504aa03c96fdac3ad
# seed: 2040080167

# Time:  O(m * n)
# Space: O(m + n)

class Solution2(object):
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        match = [[False for i in xrange(len(s2) + 1)] for j in xrange(len(s1) + 1)]
        match[0][0] = True
        for i in xrange(1, len(s1) + 1):
            match[i][0] = match[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in xrange(1, len(s2) + 1):
            match[0][j] = match[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in xrange(1, len(s1) + 1):
            for j in xrange(1, len(s2) + 1):
                match[i][j] = (match[i - 1][j] and s1[i - 1] == s3[i + j - 1]) \
                                       or (match[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return match[-1][-1]