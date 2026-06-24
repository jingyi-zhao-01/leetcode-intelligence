# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-number-of-subsequences-with-equal-gcd
# source_path: LeetCode-Solutions-master/Python/find-the-number-of-subsequences-with-equal-gcd.py
# solution_class: Solution2
# submission_id: ad61813aab6eb901542103990e1d82eaa6b030c9
# seed: 3796209295

# Time:  precompute: O(max_r^2 * log(max_r))
#        runtime:    O(n + r^2)
# Space: O(max_r^2)

# number theory, mobius function, principle of inclusion-exclusion
MOD = 10**9+7
MAX_NUM = 200
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a//gcd(a, b)*b

POW2 = [1]*(MAX_NUM+1)  # Time: O(max_r)
for i in xrange(len(POW2)-1):
    POW2[i+1] = (POW2[i]*2)%MOD
POW3 = [1]*(MAX_NUM+1)
for i in xrange(len(POW3)-1):  # Time: O(max_r)
    POW3[i+1] = (POW3[i]*3)%MOD
LCM = [[0]*(MAX_NUM+1) for _ in xrange(MAX_NUM+1)]
for i in xrange(1, MAX_NUM+1):  # Time: O(max_r^2 * log(max_r))
    for j in xrange(i, MAX_NUM+1):
        LCM[i][j] = LCM[j][i] = lcm(i, j)
MU = [0]*(MAX_NUM+1)
MU[1] = 1
for i in xrange(1, MAX_NUM+1):  # Time: O(max_r * log(max_r))
    for j in xrange(i+i, MAX_NUM+1, i):
        MU[j] -= MU[i] 

class Solution2(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        dp = collections.defaultdict(int)
        dp[(0, 0)] = 1
        for x in nums:
            new_dp = collections.defaultdict(int)
            for (g1, g2), cnt in dp.items():
                ng1, ng2 = gcd(g1, x), gcd(g2, x)
                new_dp[(g1, g2)] = (new_dp[(g1, g2)]+cnt)%MOD
                new_dp[(ng1, g2)] = (new_dp[(ng1, g2)]+cnt)%MOD
                new_dp[(g1, ng2)] = (new_dp[(g1, ng2)]+cnt)%MOD
            dp = new_dp
        return reduce(lambda accu, x: (accu+x)%MOD, (cnt for (g1, g2), cnt in dp.iteritems() if g1 == g2 > 0), 0)