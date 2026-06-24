# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: optimal-account-balancing
# source_path: LeetCode-Solutions-master/Python/optimal-account-balancing.py
# solution_class: Solution
# submission_id: f6bde6bb03b9eabc7bcb358479d905ec4d6f21f3
# seed: 3005124616

# Time:  O(n * 2^n), n is the size of the debt.
# Space: O(2^n)

import collections

class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        accounts = collections.defaultdict(int)
        for src, dst, amount in transactions:
            accounts[src] += amount
            accounts[dst] -= amount

        debts = [account for account in accounts.itervalues() if account]

        dp = [0]*(2**len(debts))
        sums = [0]*(2**len(debts))
        for i in xrange(len(dp)):
            bit = 1
            for j in xrange(len(debts)):
                if (i & bit) == 0:
                    nxt = i | bit
                    sums[nxt] = sums[i]+debts[j]
                    if sums[nxt] == 0:
                        dp[nxt] = max(dp[nxt], dp[i]+1)
                    else:
                        dp[nxt] = max(dp[nxt], dp[i])
                bit <<= 1
        return len(debts)-dp[-1]