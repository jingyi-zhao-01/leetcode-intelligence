# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: plates-between-candles
# source_path: LeetCode-Solutions-master/Python/plates-between-candles.py
# solution_class: Solution
# submission_id: bde5ea61063adf8014b480009c222efd9757056b
# seed: 883548154

# Time:  O(n + q)
# Space: O(n)

class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        left, prefix = [0]*len(s), {}
        curr, cnt = -1, 0
        for i in xrange(len(s)):
            if s[i] == '|':
                curr = i
                cnt += 1
                prefix[i] = cnt
            left[i] = curr
        right = [0]*len(s)
        curr = len(s)
        for i in reversed(xrange(len(s))):
            if s[i] == '|':
                curr = i
            right[i] = curr
        return [max((left[r]-right[l]+1) - (prefix[left[r]]-prefix[right[l]]+1), 0) for l, r in queries]