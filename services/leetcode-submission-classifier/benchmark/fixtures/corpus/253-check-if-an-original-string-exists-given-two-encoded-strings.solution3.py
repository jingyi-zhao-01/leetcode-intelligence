# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-an-original-string-exists-given-two-encoded-strings
# source_path: LeetCode-Solutions-master/Python/check-if-an-original-string-exists-given-two-encoded-strings.py
# solution_class: Solution3
# submission_id: f9b78ed59d01f3e7ec37e1fca47b888732cb249c
# seed: 3512844054

# Time:  O(m * n * k), k is the max number of consecutive digits in s1 and s2
# Space: O(m * n * k)

# top-down dp (faster since accessing less states)

class Solution3(object):
    def possiblyEquals(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        MAX_DIGIT_LEN = 3
        w = 1+MAX_DIGIT_LEN
        dp = [[set() for _ in xrange(len(s2)+1)] for _ in xrange(w)]
        dp[0][0].add(0)
        for i in xrange(len(s1)+1):
            if i:
                dp[(i-1)%w] = [set() for _ in xrange(len(s2)+1)]
            if i != len(s1) and s1[i] == '0':
                continue
            for j in xrange(len(s2)+1):
                for k in dp[i%w][j]:
                    if i != len(s1) and j != len(s2) and s1[i] == s2[j] and k == 0:
                        dp[(i+1)%w][j+1].add(k)
                    if k <= 0 and i != len(s1):
                        if not s1[i].isdigit():
                            if k:
                                dp[(i+1)%w][j].add(k+1)
                        elif s1[i] != '0':
                            curr = 0
                            for ni in xrange(i, len(s1)):
                                if not s1[ni].isdigit():
                                    break
                                curr = curr*10 + int(s1[ni])
                                dp[(ni+1)%w][j].add(k+curr)
                    if k >= 0 and j != len(s2):
                        if not s2[j].isdigit():
                            if k:
                                dp[i%w][j+1].add(k-1)
                        elif s2[j] != '0':
                            curr = 0
                            for nj in xrange(j, len(s2)):
                                if not s2[nj].isdigit():
                                    break
                                curr = curr*10 + int(s2[nj])
                                dp[i%w][nj+1].add(k-curr)
        return 0 in dp[len(s1)%w][len(s2)]