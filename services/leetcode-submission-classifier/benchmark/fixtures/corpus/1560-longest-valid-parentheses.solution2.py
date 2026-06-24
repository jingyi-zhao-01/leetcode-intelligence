# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-valid-parentheses
# source_path: LeetCode-Solutions-master/Python/longest-valid-parentheses.py
# solution_class: Solution2
# submission_id: dce07eea423ce8e78878c559d6e0d23bc6fa3156
# seed: 2039442275

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        longest, last, indices = 0, -1, []
        for i in xrange(len(s)):
            if s[i] == '(':
                indices.append(i)
            elif not indices:
                last = i
            else:
                indices.pop()
                if not indices:
                    longest = max(longest, i - last)
                else:
                    longest = max(longest, i - indices[-1])
        return longest