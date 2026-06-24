# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-a-string-contains-all-binary-codes-of-size-k
# source_path: LeetCode-Solutions-master/Python/check-if-a-string-contains-all-binary-codes-of-size-k.py
# solution_class: Solution2
# submission_id: db878e3b7221bfdb36e934f1d53b9e2b983718b0
# seed: 3024384183

# Time:  O(n * k)
# Space: O(k * 2^k)

class Solution2(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        lookup = set()
        base = 2**k
        if base > len(s):
            return False
        num = 0
        for i in xrange(len(s)):
            num = (num << 1) + (s[i] == '1')
            if i >= k-1:
                lookup.add(num)
                num -= (s[i-k+1] == '1') * (base//2)
        return len(lookup) == base