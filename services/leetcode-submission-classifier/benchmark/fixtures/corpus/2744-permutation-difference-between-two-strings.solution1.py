# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: permutation-difference-between-two-strings
# source_path: LeetCode-Solutions-master/Python/permutation-difference-between-two-strings.py
# solution_class: Solution
# submission_id: dc4a0a12273dbc4ad0795da5ff88e5f35c6a8eba
# seed: 171681971

# Time:  O(n + 26)
# Space: O(26)

# hash table

class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        lookup = [-1]*26
        for i, x in enumerate(s):
            lookup[ord(x)-ord('a')] = i
        return sum(abs(lookup[ord(x)-ord('a')]-i)for i, x in enumerate(t))