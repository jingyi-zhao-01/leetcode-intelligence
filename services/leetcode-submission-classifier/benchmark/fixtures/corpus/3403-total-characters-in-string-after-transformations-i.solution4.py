# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: total-characters-in-string-after-transformations-i
# source_path: LeetCode-Solutions-master/Python/total-characters-in-string-after-transformations-i.py
# solution_class: Solution4
# submission_id: 91dd90eeecac58f6163559e2532933d474dca8ba
# seed: 296119784

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

class Solution4(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        MOD = 10**9+7
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        for _ in xrange(t):
            new_cnt = [0]*26
            for i in xrange(26):
                new_cnt[(i+1)%26] = (new_cnt[(i+1)%26]+cnt[i])%MOD
                if i == 25:
                    new_cnt[(i+2)%26] = (new_cnt[(i+2)%26]+cnt[i])%MOD
            cnt = new_cnt
        return reduce(lambda accu, x: (accu+x)%MOD, cnt, 0)