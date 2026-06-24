# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-k-reducible-numbers-less-than-n
# source_path: LeetCode-Solutions-master/Python/count-k-reducible-numbers-less-than-n.py
# solution_class: Solution2
# submission_id: 82030218e7163235a77d22f41a02d7a243caa4c4
# seed: 1061837712

# Time:  O(n^2)
# Space: O(n)

# dp
cnt = [0]*2

class Solution2(object):
    def countKReducibleNumbers(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        fact, inv, inv_fact = [[1]*2 for _ in xrange(3)]  
        def nCr(n, k):
            while len(inv) <= n:  # lazy initialization
                fact.append(fact[-1]*len(inv) % MOD)
                inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
                inv_fact.append(inv_fact[-1]*inv[-1] % MOD)
            return (fact[n]*inv_fact[n-k] % MOD) * inv_fact[k] % MOD

        def popcount(x):
            return bin(x).count('1')
      
        while len(s)-1 >= len(cnt):  # cached
            cnt.append(cnt[popcount(len(cnt))]+1)
        result = curr = 0
        for i in xrange(len(s)):
            if s[i] != '1':
                continue
            for c in xrange((len(s)-(i+1))+1):
                if cnt[curr+c] < k:
                    result = (result+nCr(len(s)-(i+1), c))%MOD
            curr += 1
        return (result-1)%MOD