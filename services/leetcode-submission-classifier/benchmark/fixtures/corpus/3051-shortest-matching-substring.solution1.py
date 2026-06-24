# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-matching-substring
# source_path: LeetCode-Solutions-master/Python/shortest-matching-substring.py
# solution_class: Solution
# submission_id: 68fe6db2e8d5a3067a90229c360f1ff705dbed79
# seed: 760994039

# Time:  O(n + m)
# Space: O(n + m)

# kmp, two pointers (three pointers)

class Solution(object):
    def shortestMatchingSubstring(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: int
        """
        INF = float("inf")
        def getPrefix(pattern):
            prefix = [-1]*len(pattern)
            j = -1
            for i in xrange(1, len(pattern)):
                while j+1 > 0 and pattern[j+1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix

        def KMP(text, pattern):
            if not pattern:
                for i in xrange(len(text)+1):
                    yield i
                return
            prefix = getPrefix(pattern)
            j = -1
            for i in xrange(len(text)):
                while j+1 > 0 and pattern[j+1] != text[i]:
                    j = prefix[j]
                if pattern[j+1] == text[i]:
                    j += 1
                if j+1 == len(pattern):
                    yield i-j
                    j = prefix[j]
        
        a, b, c = p.split('*')
        n = len(s)
        la, lb, lc = len(a), len(b), len(c)
        result = INF
        j = k = 0
        jt = KMP(s, b)
        kt = KMP(s, c)
        for i in KMP(s, a):
            while j != -1 and j < i+la:
                j = next(jt, -1)
            if j == -1:
                break
            while k != -1 and k < j+lb:
                k = next(kt, -1)
            if k == -1:
                break
            result = min(result, (k+lc)-i)
        return result if result != INF else -1 