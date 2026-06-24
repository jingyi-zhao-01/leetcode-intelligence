# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: score-of-parentheses
# source_path: LeetCode-Solutions-master/Python/score-of-parentheses.py
# solution_class: Solution
# submission_id: 5dc3071105c21a2eb2a1a46e4548f272e6327071
# seed: 3738986434

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        result, depth = 0, 0
        for i in xrange(len(S)):
            if S[i] == '(':
                depth += 1
            else:
                depth -= 1
                if S[i-1] == '(':
                    result += 2**depth
        return result