# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lexicographically-smallest-generated-string
# source_path: LeetCode-Solutions-master/Python/lexicographically-smallest-generated-string.py
# solution_class: Solution
# submission_id: 2bdbd7719487076a493af0b1d9abd52dee3a9ae4
# seed: 1225086997

# Time:  O(n + m)
# Space: O(n + m)

import collections


# kmp, two pointers, sliding window, deque, greedy

class Solution(object):
    def generateString(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
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

        n, m = len(str1), len(str2)
        candidate = ['*']*(n+m-1)
        prefix = getPrefix(str2)
        prev = -m
        for i, x in enumerate(str1):
            if x != 'T':
                continue
            diff = i-prev
            if diff < m:
                if prefix[m-1]+1 == m-diff:
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
        prefix = getPrefix(result)
        dq = collections.deque()
        i, j = m+1, 0
        while i-(m+1) < n:
            while dq and dq[0] < i:
                dq.popleft()
            while j < len(idxs) and idxs[j] <= i+(m-1):
                dq.append(idxs[j])
                j += 1
            if str1[i-(m+1)] == 'F' and prefix[i+(m-1)]+1 == m:
                if not dq:
                    return ""
                result[dq[-1]] = 'b'
                i += m
            else:
                i += 1
        return "".join(result[m+1:])