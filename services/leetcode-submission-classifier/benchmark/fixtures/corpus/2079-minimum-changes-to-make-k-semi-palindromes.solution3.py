# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-changes-to-make-k-semi-palindromes
# source_path: LeetCode-Solutions-master/Python/minimum-changes-to-make-k-semi-palindromes.py
# solution_class: Solution3
# submission_id: b7afe079ffbc0c4fd0b76b681cda8c251755c200
# seed: 2761049439

# Time:  O(n * nlogn + n^3 + n^2 * k) = O(n^3)
# Space: O(n * nlogn) = O(n^2 * logn)

# number theory, dp

class Solution3(object):
    def minimumChanges(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def min_dist(left, right):  # Time: O(nlogn)
            return min(sum(s[left+i] != s[right-((i//d+1)*d-1)+(i%d)] for i in xrange((right-left+1)//2))
 for d in divisors[right-left+1])

        divisors = [[] for _ in xrange(len(s)+1)]
        for i in xrange(1, len(divisors)):  # Time: O(nlogn), Space: O(nlogn)
            for j in xrange(i+i, len(divisors), i):
                divisors[j].append(i)
        dp = [[len(s)]*(k+1) for _ in xrange(len(s)+1)]
        dp[0][0] = 0
        for i in xrange(len(s)):  # Time: O(n^2 * nlogn + n^2 * k), Space: O(n * k)
            for j in xrange(i):
                c = min_dist(j, i)
                for l in xrange(k):
                    dp[i+1][l+1] = min(dp[i+1][l+1], dp[j][l]+c)
        return dp[len(s)][k]