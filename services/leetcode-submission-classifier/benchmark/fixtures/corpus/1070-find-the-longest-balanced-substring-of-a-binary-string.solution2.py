# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-longest-balanced-substring-of-a-binary-string
# source_path: LeetCode-Solutions-master/Python/find-the-longest-balanced-substring-of-a-binary-string.py
# solution_class: Solution2
# submission_id: 34d98d531b7bea20fb13af88da43813ad749d7cb
# seed: 3764947108

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution2(object):
    def findTheLongestBalancedSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        prev, cnt = [0]*2, [0]*2
        for c in s:
            cnt[int(c)] += 1
            if cnt[int(c)^1]:
                prev[int(c)^1], cnt[int(c)^1] = cnt[int(c)^1], 0
            result = max(result, 2*min(prev[0], cnt[1]))
        return result