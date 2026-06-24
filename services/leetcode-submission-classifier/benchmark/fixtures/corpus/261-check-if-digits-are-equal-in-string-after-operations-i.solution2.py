# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-digits-are-equal-in-string-after-operations-i
# source_path: LeetCode-Solutions-master/Python/check-if-digits-are-equal-in-string-after-operations-i.py
# solution_class: Solution2
# submission_id: 9b9dd4c5d498d6ae4e9184279a62157a6171922e
# seed: 4250749940

# Time:  O(nlogn)
# Space: O(1)

# fast exponentiation

class Solution2(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def nCr(n, r):
            if n-r < r:
                r = n-r
            if LOOKUP[n][r] == -1:
                c = 1
                for k in xrange(1, r+1):
                    c *= n-k+1
                    c //= k
                LOOKUP[n][r] = c
            return LOOKUP[n][r]

        # https://en.wikipedia.org/wiki/Lucas%27s_theorem
        def nCr_mod(n, r, mod):
            result = 1
            while n > 0 or r > 0:
                n, ni = divmod(n, mod)
                r, ri = divmod(r, mod)
                if ni < ri:
                    return 0
                result = (result*nCr(ni, ri))%mod
            return result

        def nC10(n, k):
            return lookup[nCr_mod(n, k, 2)][nCr_mod(n, k, 5)]

        lookup = [[0]*5 for _ in xrange(2)]
        for i in xrange(10):
            lookup[i%2][i%5] = i
        total = 0
        for i in xrange(len(s)-1):
            total = (total+nC10(len(s)-2, i)*(ord(s[i])-ord(s[i+1])))%10
        return total == 0