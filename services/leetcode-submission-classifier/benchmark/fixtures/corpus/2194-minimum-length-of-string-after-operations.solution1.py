# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-length-of-string-after-operations
# source_path: LeetCode-Solutions-master/Python/minimum-length-of-string-after-operations.py
# solution_class: Solution
# submission_id: d887257ff92f5fb6aff0133592f567ae11453448
# seed: 269193083

# Time:  O(n + 26)
# Space: O(26)

# freq table

class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        return sum(2-x%2 for x in cnt if x)