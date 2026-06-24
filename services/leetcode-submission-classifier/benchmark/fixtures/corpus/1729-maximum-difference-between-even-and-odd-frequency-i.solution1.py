# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-difference-between-even-and-odd-frequency-i
# source_path: LeetCode-Solutions-master/Python/maximum-difference-between-even-and-odd-frequency-i.py
# solution_class: Solution
# submission_id: 855df2d80ae101106839cab9e40b370f6d6d160d
# seed: 719434777

# Time:  O(n + 26)
# Space: O(26)

# freq table

class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        mn, mx = float("inf"), 0
        for x in cnt:
            if not x:
                continue
            if x%2 == 0:
                mn = min(mn, x)
            else:
                mx = max(mx, x)
        return mx-mn