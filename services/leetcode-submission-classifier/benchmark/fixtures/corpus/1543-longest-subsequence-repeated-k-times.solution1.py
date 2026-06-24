# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-subsequence-repeated-k-times
# source_path: LeetCode-Solutions-master/Python/longest-subsequence-repeated-k-times.py
# solution_class: Solution
# submission_id: 5ff852e6564ab210b5b99500df7b7a1a1e9e8030
# seed: 1757194576

# Time:  O(n * (n/k)!)
# Space: O(n)

import collections

class Solution(object):
    def longestSubsequenceRepeatedK(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def check(s, k, curr):
            if not curr:
                return True
            i = 0
            for c in s:
                if c != curr[i]:
                    continue
                i += 1
                if i != len(curr):
                    continue
                i = 0
                k -= 1
                if not k:
                    return True
            return False

        def backtracking(s, k, curr, cnts, result):
            if not check(s, k, curr):
                return
            if len(curr) > len(result):
                result[:] = curr
            for c in reversed(string.ascii_lowercase):
                if cnts[c] < k:
                    continue
                cnts[c] -= k
                curr.append(c)
                backtracking(s, k, curr, cnts, result)
                curr.pop()
                cnts[c] += k
                    
        cnts = collections.Counter(s)
        new_s = []
        for c in s:
            if cnts[c] < k:
                continue
            new_s.append(c)
        result =[]
        backtracking(new_s, k, [], cnts, result)
        return "".join(result)