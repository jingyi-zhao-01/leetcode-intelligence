# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-time-to-revert-word-to-initial-state-i
# source_path: LeetCode-Solutions-master/Python/minimum-time-to-revert-word-to-initial-state-i.py
# solution_class: Solution
# submission_id: 915edb5fbd2fdddf7542b3b21cf334a808aeafa5
# seed: 2942742977

# Time:  O(n)
# Space: O(n)

# z-function

class Solution(object):
    def minimumTimeToInitialState(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b
    
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

        z = z_function(word)
        for i in xrange(k, len(word), k):
            if z[i] == len(word)-i:
                return i//k
        return ceil_divide(len(word), k)