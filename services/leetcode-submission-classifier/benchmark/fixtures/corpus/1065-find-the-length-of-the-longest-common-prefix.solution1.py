# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-length-of-the-longest-common-prefix
# source_path: LeetCode-Solutions-master/Python/find-the-length-of-the-longest-common-prefix.py
# solution_class: Solution
# submission_id: 65fb71e6e636c10a2a3f13ca1b5249d3e22f4738
# seed: 2621007786

# Time:  O((n + m) * l)
# Space: O(t)

# trie

class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for x in arr1:
            reduce(dict.__getitem__, str(x), trie)
        result = 0
        for x in arr2:
            curr = trie
            for i, c in enumerate(str(x)):
                if c not in curr:
                    break
                curr = curr[c]
            else:
                i += 1
            result = max(result, i)
        return result