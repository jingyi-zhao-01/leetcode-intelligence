# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-distinct-binary-strings-after-applying-operations
# source_path: LeetCode-Solutions-master/Python/number-of-distinct-binary-strings-after-applying-operations.py
# solution_class: Solution
# submission_id: 087e5c005d74e76600628bc897994edf3e3fe068
# seed: 3085465207

# Time:  O(logn)
# Space: O(1)

# combinatorics

class Solution(object):
    def countDistinctStrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        return pow(2, len(s)-k+1, MOD)