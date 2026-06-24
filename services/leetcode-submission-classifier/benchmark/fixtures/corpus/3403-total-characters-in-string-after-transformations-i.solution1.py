# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: total-characters-in-string-after-transformations-i
# source_path: LeetCode-Solutions-master/Python/total-characters-in-string-after-transformations-i.py
# solution_class: Solution
# submission_id: 41c73169196513600115b556138d2277ce6363f6
# seed: 3351583680

# Time:  precompute: O(t + 26)
#        runtime:    O(n)
# Space: O(t + 26)

# precompute, dp
MOD = 10**9+7
MAX_T = 10**5
DP = [0]*(MAX_T+26)
for i in xrange(26):
    DP[i] = 1
for i in xrange(26, len(DP)):
    DP[i] = (DP[i-26]+DP[(i-26)+1])%MOD

class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        return reduce(lambda accu, x: (accu+x)%MOD, (DP[((ord(x)-ord('a'))+t)] for x in s), 0)