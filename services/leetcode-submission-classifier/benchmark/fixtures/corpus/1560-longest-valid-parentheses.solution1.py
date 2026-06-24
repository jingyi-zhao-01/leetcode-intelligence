# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-valid-parentheses
# source_path: LeetCode-Solutions-master/Python/longest-valid-parentheses.py
# solution_class: Solution
# submission_id: 5c944c561b3b2691e5966977b93bc25e3646328a
# seed: 4052507060

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        def length(it, start, c):
            depth, longest = 0, 0
            for i in it:
                if s[i] == c:
                    depth += 1
                else:
                    depth -= 1
                    if depth < 0:
                        start, depth = i, 0
                    elif depth == 0:
                        longest = max(longest, abs(i - start))
            return longest

        return max(length(xrange(len(s)), -1, '('), \
                   length(reversed(xrange(len(s))), len(s), ')'))