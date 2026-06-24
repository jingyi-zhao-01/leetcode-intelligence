# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-occurrence-of-first-almost-equal-substring
# source_path: LeetCode-Solutions-master/Python/find-the-occurrence-of-first-almost-equal-substring.py
# solution_class: Solution
# submission_id: 9b39ad9a5eb2178d354af21d3986a8d943b64a09
# seed: 1315755496

# Time:  O(n + m)
# Space: O(n + m)

# z-function

class Solution(object):
    def minStartingIndex(self, s, pattern):
        """
        :type s: str
        :type pattern: str
        :rtype: int
        """
        K = 1
        # Template: https://cp-algorithms.com/string/z-function.html
        def z_function(s):  # Time: O(n), Space: O(n)
            z = [0]*len(s)
            l, r = 0, 0
            for i in xrange(1, len(z)):
                if i <= r:
                    z[i] = min(r-i+1, z[i-l])
                while i+z[i] < len(z) and s[z[i]] == s[i+z[i]]:
                    z[i] += 1
                if i+z[i]-1 > r:
                    l, r = i, i+z[i]-1
            return z
        
        z1 = z_function(pattern+s)
        z2 = z_function(pattern[::-1]+s[::-1])
        return next((i for i in xrange(len(s)-len(pattern)+1) if z1[len(pattern)+i]+K+z2[len(s)-i] >= len(pattern)), -1)