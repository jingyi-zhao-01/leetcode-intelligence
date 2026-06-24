# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-strings-which-can-be-rearranged-to-contain-substring
# source_path: LeetCode-Solutions-master/Python/number-of-strings-which-can-be-rearranged-to-contain-substring.py
# solution_class: Solution2
# submission_id: c61106c72d3f89112b94d73416220753d45ffede
# seed: 478245405

# Time:  O(logn)
# Space: O(1)

# combinatorics, principle of inclusion-exclusion

class Solution2(object):
    def stringCount(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        L, E, EE, T = [1<<i for i in xrange(4)]
        dp = [0]*(1<<4)
        dp[0] = 1
        for _ in xrange(n):
            new_dp = [0]*(1<<4)
            for mask in xrange(len(dp)):
                new_dp[mask|L] = (new_dp[mask|L]+dp[mask])%MOD
                if not (mask & E):
                    new_dp[mask|E] = (new_dp[mask|E]+dp[mask])%MOD
                else:
                    new_dp[mask|EE] = (new_dp[mask|EE]+dp[mask])%MOD
                new_dp[mask|T] = (new_dp[mask|T]+dp[mask])%MOD
                new_dp[mask] = (new_dp[mask]+23*dp[mask])%MOD
            dp = new_dp
        return dp[-1]