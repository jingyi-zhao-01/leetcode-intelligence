# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-beautiful-indices-in-the-given-array-ii
# source_path: LeetCode-Solutions-master/Python/find-beautiful-indices-in-the-given-array-ii.py
# solution_class: Solution2
# submission_id: 677d528a8e8f2f42595f0522b75cafb12b50b28d
# seed: 2655127390

# Time:  O(n), x = len(KMP(s, a)), y = len(KMP(s, b))
# Space: O(min(a + b + x + y, n))

# kmp, two pointers

class Solution2(object):
    def beautifulIndices(self, s, a, b, k):
        """
        :type s: str
        :type a: str
        :type b: str
        :type k: int
        :rtype: List[int]
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

        def KMP(text, pattern):
            prefix = getPrefix(pattern+'#'+text)
            return ((i-(len(pattern)+1))-(len(pattern)-1) for i in xrange((len(pattern)+1)+(len(pattern)-1) , len(prefix)) if prefix[i]+1 == len(pattern))
    
        result = []
        if not (len(a) <= len(s) and len(b) <= len(s)):
            return result
        lookup = list(KMP(s, b))
        j = 0
        for i in KMP(s, a):
            j = bisect.bisect_left(lookup, i-k)
            if j < len(lookup) and lookup[j] <= i+k:
                result.append(i)
        return result