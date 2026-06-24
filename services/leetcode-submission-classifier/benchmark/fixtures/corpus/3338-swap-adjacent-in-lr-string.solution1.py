# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: swap-adjacent-in-lr-string
# source_path: LeetCode-Solutions-master/Python/swap-adjacent-in-lr-string.py
# solution_class: Solution
# submission_id: c9fdeb78259b19f3ac6bf577550b282e13f91845
# seed: 3726421973

# Time:  O(n)
# Space: O(1)

# the followings are invariant if the number of 'X' in both strings are the same
# 1. the ordering of 'L', 'R' in both strings are the same
# 2. for each position (i, j) of paired 'L' character in both strings, i >= j
# 3. for each position (i, j) of paired 'R' character in both strings, i <= j

class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if start.count('X') != end.count('X'):
            return False
        i, j = 0, 0
        while i < len(start) and j < len(end):
            while i < len(start) and start[i] == 'X':
                i += 1
            while j < len(end) and end[j] == 'X':
                j += 1
            if (i < len(start)) != (j < len(end)):
                return False
            elif i < len(start) and j < len(end):
                if start[i] != end[j] or \
                   (start[i] == 'L' and i < j) or \
                   (start[i] == 'R' and i > j):
                    return False
            i += 1
            j += 1
        return True