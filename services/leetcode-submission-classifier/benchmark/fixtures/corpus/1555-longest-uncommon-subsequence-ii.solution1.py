# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-uncommon-subsequence-ii
# source_path: LeetCode-Solutions-master/Python/longest-uncommon-subsequence-ii.py
# solution_class: Solution
# submission_id: dcc22c784258eabefe19a4c4ea807b185f7ec540
# seed: 1588791470

# Time:  O(l * n^2)
# Space: O(1)

class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def isSubsequence(a, b):
            i = 0
            for j in xrange(len(b)):
                if i >= len(a):
                    break
                if a[i] == b[j]:
                    i += 1
            return i == len(a)

        strs.sort(key=len, reverse=True)
        for i in xrange(len(strs)):
            all_of = True
            for j in xrange(len(strs)):
                if len(strs[j]) < len(strs[i]):
                    break
                if i != j and isSubsequence(strs[i], strs[j]):
                    all_of = False
                    break
            if all_of:
                return len(strs[i])
        return -1