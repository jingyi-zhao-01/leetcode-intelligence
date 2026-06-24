# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delete-characters-to-make-fancy-string
# source_path: LeetCode-Solutions-master/Python/delete-characters-to-make-fancy-string.py
# solution_class: Solution
# submission_id: c16674142306470a83a0f320f6f3adefcc60acbe
# seed: 3487838428

# Time:  O(n)
# Space: O(1)

# inplace solution

class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        cnt = j = 0
        for i, c in enumerate(s):
            cnt = cnt+1 if i >= 1 and c == s[i-1] else 1
            if cnt < 3:
                s[j] = c
                j += 1
        s[:] = s[:j]
        return "".join(s)