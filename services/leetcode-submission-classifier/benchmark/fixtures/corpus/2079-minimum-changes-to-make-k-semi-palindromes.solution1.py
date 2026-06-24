# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-changes-to-make-k-semi-palindromes
# source_path: LeetCode-Solutions-master/Python/minimum-changes-to-make-k-semi-palindromes.py
# solution_class: Solution
# submission_id: 0001946b1add8517812c95adac84918edb253530
# seed: 89534866

# Time:  O(n * nlogn + n^3 + n^2 * k) = O(n^3)
# Space: O(n * nlogn) = O(n^2 * logn)

# number theory, dp

class Solution(object):
    def minimumChanges(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        divisors = [[] for _ in xrange(len(s)+1)]
        for i in xrange(1, len(divisors)):  # Time: O(nlogn), Space: O(nlogn)
            for j in xrange(i, len(divisors), i):
                divisors[j].append(i)
        dp = [[{} for _ in xrange(len(s))] for _ in xrange(len(s))]
        for l in xrange(1, len(s)+1):  # Time: O(n * nlogn + n^3), Space: O(n * nlogn)
            for left in xrange(len(s)-l+1):
                right = left+l-1
                for d in divisors[l]:
                    dp[left][right][d] = (dp[left+d][right-d][d] if left+d < right-d else 0)+sum(s[left+i] != s[(right-(d-1))+i] for i in xrange(d))
        dp2 = [[min(dp[i][j][d] for d in divisors[j-i+1] if d != j-i+1) if i < j else 0 for j in xrange(len(s))] for i in xrange(len(s))]  # Time: O(n^2), Space: O(n^2)
        dp3 = [len(s)]*(len(s)+1)
        dp3[0] = 0
        for l in xrange(k):  # Time: O(k * n^2), Space: O(n)
            new_dp3 = [len(s)]*(len(s)+1)
            for i in xrange(len(s)):
                for j in xrange(l*2, i):  # optimized for the fact that the length of semi-palindrome is at least 2
                    new_dp3[i+1]= min(new_dp3[i+1], dp3[j]+dp2[j][i])
            dp3 = new_dp3
        return dp3[len(s)]