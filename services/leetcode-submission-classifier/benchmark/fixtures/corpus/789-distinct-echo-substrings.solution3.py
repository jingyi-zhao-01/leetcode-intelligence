# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: distinct-echo-substrings
# source_path: LeetCode-Solutions-master/Python/distinct-echo-substrings.py
# solution_class: Solution3
# submission_id: 3390d284da3e205d01ca9b63a6a0aaff3ea40491
# seed: 90925975

# Time:  O(n^2 + d), d is the duplicated of result substrings size
# Space: O(r), r is the size of result substrings set

class Solution3(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """
        MOD = 10**9+7
        D = 27  # a-z and ''
        result = set()
        for i in xrange(len(text)-1):
            left, right, pow_D = 0, 0, 1
            for l in xrange(1, min(i+2, len(text)-i)):
                left = (D*left + (ord(text[i-l+1])-ord('a')+1)) % MOD
                right = (pow_D*(ord(text[i+l])-ord('a')+1) + right) % MOD
                if left == right:  # assumed no collision
                    result.add(left)
                pow_D = (pow_D*D) % MOD 
        return len(result)