# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-scores-of-built-strings
# source_path: LeetCode-Solutions-master/Python/sum-of-scores-of-built-strings.py
# solution_class: Solution
# submission_id: ba35cb54ab09a0f00ced4dff601822c9d8c31fd9
# seed: 1128019519

# Time:  O(n)
# Space: O(n)

# z-function

class Solution(object):
    def sumScores(self, s):
        """
        :type s: str
        :rtype: int
        """
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

        z = z_function(s)
        z[0] = len(s)
        return sum(z)