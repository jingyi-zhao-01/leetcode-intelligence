# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lexicographically-smallest-generated-string
# source_path: LeetCode-Solutions-master/Python/lexicographically-smallest-generated-string.py
# solution_class: Solution2
# submission_id: 14c55944173835c1b9c605900c176f4a57148589
# seed: 491331987

# Time:  O(n + m)
# Space: O(n + m)

import collections


# kmp, two pointers, sliding window, deque, greedy

class Solution2(object):
    def generateString(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
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

        n, m = len(str1), len(str2)
        candidate = ['*']*(n+m-1)
        z = z_function(str2)
        prev = -m
        for i, x in enumerate(str1):
            if x != 'T':
                continue
            diff = i-prev
            if diff < m:
                if z[diff] == m-diff:
                    candidate[prev+m:i+m] = str2[m-diff:]
                else:
                    return ""
            else:
                candidate[i:i+m] = str2
            prev = i
        result = list(str2)+['#']+candidate
        idxs = []
        for i in xrange(m+1, len(result)):
            if result[i] == '*':
                result[i] = 'a'
                idxs.append(i)
        z = z_function(result)
        dq = collections.deque()
        i, j = m+1, 0
        while i-(m+1) < n:
            while dq and dq[0] < i:
                dq.popleft()
            while j < len(idxs) and idxs[j] <= i+(m-1):
                dq.append(idxs[j])
                j += 1
            if str1[i-(m+1)] == 'F' and z[i] == m:
                if not dq:
                    return ""
                result[dq[-1]] = 'b'
                i += m
            else:
                i += 1
        return "".join(result[m+1:])