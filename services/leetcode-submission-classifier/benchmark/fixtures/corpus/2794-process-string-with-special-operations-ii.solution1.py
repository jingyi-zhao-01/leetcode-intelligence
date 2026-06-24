# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: process-string-with-special-operations-ii
# source_path: LeetCode-Solutions-master/Python/process-string-with-special-operations-ii.py
# solution_class: Solution
# submission_id: fbc5465446ef47fe13fc4a53b5f931067cd43608
# seed: 2191267782

# Time:  O(n)
# Space: O(1)

# backward simulation

class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = 0
        for x in s:
            if x == '*':
                l = max(l-1, 0)
            elif x == '#':
                l <<= 1
            elif x == '%':
                continue
            else:
                l += 1
        if k >= l:
            return '.'
        for x in reversed(s):
            if x == '*':
                l += 1
            elif x == '#':
                l >>= 1
                if k >= l:
                    k -= l
            elif x == '%':
                k = (l-1)-k
            else:
                l -= 1
                if l == k:
                    return x