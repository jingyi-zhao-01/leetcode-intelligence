# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-length-of-the-longest-common-prefix
# source_path: LeetCode-Solutions-master/Python/find-the-length-of-the-longest-common-prefix.py
# solution_class: Solution2
# submission_id: 95a3fb625f1a9b38f25be787840c095975b624ce
# seed: 2992741936

# Time:  O((n + m) * l)
# Space: O(t)

# trie

class Solution2(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        lookup = {0}
        for x in arr1:
            while x not in lookup:
                lookup.add(x)
                x //= 10
        result = 0
        for x in arr2:
            l = len(str(x))
            while x not in lookup:
                x //= 10
                l -= 1
            result = max(result, l)
        return result