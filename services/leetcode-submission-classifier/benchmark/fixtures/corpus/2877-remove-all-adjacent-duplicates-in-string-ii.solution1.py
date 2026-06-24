# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-all-adjacent-duplicates-in-string-ii
# source_path: LeetCode-Solutions-master/Python/remove-all-adjacent-duplicates-in-string-ii.py
# solution_class: Solution
# submission_id: 8ba4054edf8d5545b787dcc24d3a4133ed99a3fa
# seed: 2169808077

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stk = [['^', 0]]
        for c in s:
            if stk[-1][0] == c:
                stk[-1][1] += 1
                if stk[-1][1] == k:
                    stk.pop()
            else:
                stk.append([c, 1])
        return "".join(c*k for c, k in stk)