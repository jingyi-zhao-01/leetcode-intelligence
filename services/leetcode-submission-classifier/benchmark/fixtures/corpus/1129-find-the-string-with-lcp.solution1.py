# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-string-with-lcp
# source_path: LeetCode-Solutions-master/Python/find-the-string-with-lcp.py
# solution_class: Solution
# submission_id: b25822f743a3c4f119ee8d5f2a92bc9e71598ee9
# seed: 2911745536

# Time:  O(n^2)
# Space: O(1)

# constructive algorithms, greedy, dp

class Solution(object):
    def findTheString(self, lcp):
        """
        :type lcp: List[List[int]]
        :rtype: str
        """
        result = [-1]*len(lcp)
        curr = 0
        for i in xrange(len(lcp)):
            if result[i] != -1:
                continue
            if curr == 26:
                return ""
            for j in xrange(i, len(lcp[0])):
                if lcp[i][j]:
                    result[j] = curr
            curr += 1
        for i in reversed(xrange(len(lcp))):
            for j in reversed(xrange(len(lcp[0]))):
                if lcp[i][j] != ((lcp[i+1][j+1]+1 if i+1 < len(lcp) and j+1 < len(lcp[0]) else 1) if result[i] == result[j] else 0):
                    return ''
        return "".join(map(lambda x: chr(ord('a')+x), result))