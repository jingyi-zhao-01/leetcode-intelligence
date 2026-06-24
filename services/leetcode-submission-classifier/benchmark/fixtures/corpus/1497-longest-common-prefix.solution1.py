# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-common-prefix
# source_path: LeetCode-Solutions-master/Python/longest-common-prefix.py
# solution_class: Solution
# submission_id: 73fd627a7d687b4f2034e53e7906a8bb205ab383
# seed: 1188470525

# Time:  O(n * k), k is the length of the common prefix
# Space: O(1)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in xrange(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]