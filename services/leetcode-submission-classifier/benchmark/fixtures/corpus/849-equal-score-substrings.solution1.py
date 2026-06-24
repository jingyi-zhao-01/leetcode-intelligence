# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: equal-score-substrings
# source_path: LeetCode-Solutions-master/Python/equal-score-substrings.py
# solution_class: Solution
# submission_id: 9d731527fea379a07a922437c97c09a0e75caa8b
# seed: 3660475196

# Time:  O(n)
# Space: O(1)

# prefix sum

class Solution(object):
    def scoreBalance(self, s):
        """
        :type s: str
        :rtype: bool
        """
        total = sum(ord(x)-ord('a')+1 for x in s)
        prefix = 0
        for x in s:
            prefix += ord(x)-ord('a')+1
            if prefix == total-prefix:
                return True
        return False