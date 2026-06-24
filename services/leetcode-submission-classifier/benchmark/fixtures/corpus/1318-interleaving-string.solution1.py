# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: interleaving-string
# source_path: LeetCode-Solutions-master/Python/interleaving-string.py
# solution_class: Solution
# submission_id: 98d1c062c476ee0d8b27f9d9a07c38e8aacc3905
# seed: 209889360

# Time:  O(m * n)
# Space: O(m + n)

class Solution(object):
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) > len(s2):
            return self.isInterleave(s2, s1, s3)
        match = [False for i in xrange(len(s1) + 1)]
        match[0] = True
        for i in xrange(1, len(s1) + 1):
            match[i] = match[i -1] and s1[i - 1] == s3[i - 1]
        for j in xrange(1, len(s2) + 1):
            match[0] = match[0] and s2[j - 1] == s3[j - 1]
            for i in xrange(1, len(s1) + 1):
                match[i] = (match[i - 1] and s1[i - 1] == s3[i + j - 1]) \
                                       or (match[i] and s2[j - 1] == s3[i + j - 1])
        return match[-1]