# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-maximum-number-of-non-intersecting-substrings
# source_path: LeetCode-Solutions-master/Python/find-maximum-number-of-non-intersecting-substrings.py
# solution_class: Solution
# submission_id: a4aa5e14a02f8b43e95e2499e9637e7bed96c850
# seed: 2089992967

# Time:  O(n)
# Space: O(26)

# greedy, hash table

class Solution(object):
    def maxSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        L = 4
        result = 0
        lookup = {}
        for i, c in enumerate(word):
            if c not in lookup:
                lookup[c] = i
            elif i-lookup[c]+1 >= L:
                result += 1
                lookup.clear()
        return result