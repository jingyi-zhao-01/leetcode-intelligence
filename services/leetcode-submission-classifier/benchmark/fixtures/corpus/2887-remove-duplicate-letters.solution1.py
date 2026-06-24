# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-duplicate-letters
# source_path: LeetCode-Solutions-master/Python/remove-duplicate-letters.py
# solution_class: Solution
# submission_id: af6b4d31db18892b97b5b8ce3f360c628c0044cf
# seed: 2118402282

# Time:  O(n)
# Space: O(k), k is size of the alphabet

from collections import Counter

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        remaining = Counter(s)

        in_stack, stk = set(), []
        for c in s:
            if c not in in_stack:
                while stk and stk[-1] > c and remaining[stk[-1]]:
                    in_stack.remove(stk.pop())
                stk += c
                in_stack.add(c)
            remaining[c] -= 1
        return "".join(stk)