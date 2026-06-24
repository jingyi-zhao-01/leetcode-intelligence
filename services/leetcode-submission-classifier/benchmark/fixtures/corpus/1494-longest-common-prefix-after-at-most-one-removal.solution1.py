# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-common-prefix-after-at-most-one-removal
# source_path: LeetCode-Solutions-master/Python/longest-common-prefix-after-at-most-one-removal.py
# solution_class: Solution
# submission_id: 7f3788b13225de6ad645b51276f3146d206b8f62
# seed: 3622189082

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution(object):
    def longestCommonPrefix(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        result = i = j = 0
        removed = False
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                result += 1
                i += 1
                j += 1
            elif not removed:
                removed = True
                i += 1
            else:
                break
        return result