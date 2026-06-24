# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-palindromic-subsequences
# source_path: LeetCode-Solutions-master/Python/count-palindromic-subsequences.py
# solution_class: Solution
# submission_id: bb79f495581a7e7c67db2afe4ad7dbd46f1ac306
# seed: 1805789907

# Time:  O(10^(l/2) * n), l = 5
# Space: O(10^(l/2) * n)

# freq table, prefix sum

class Solution(object):
    def countPalindromes(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9+7
        cnt = [0]*10
        left = [[[0]*10 for _ in xrange(10)] for _ in xrange(len(s)+1)]
        for k in xrange(len(s)):
            left[k+1] = [[left[k][i][j] for j in xrange(10)] for i in xrange(10)]
            for i in xrange(10):
                left[k+1][int(s[k])][i] += cnt[i]
            cnt[int(s[k])] += 1
        cnt = [0]*10
        right = [[0]*10 for _ in xrange(10)]
        result = 0
        for k in reversed(xrange(len(s))):
            for i in xrange(10):
                for j in xrange(10):
                    result = (result+left[k][i][j]*right[i][j])%MOD
            for i in xrange(10):
                right[int(s[k])][i] += cnt[i]
            cnt[int(s[k])] += 1
        return result