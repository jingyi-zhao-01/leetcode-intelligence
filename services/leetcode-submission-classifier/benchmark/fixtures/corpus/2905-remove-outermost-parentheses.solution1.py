# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-outermost-parentheses
# source_path: LeetCode-Solutions-master/Python/remove-outermost-parentheses.py
# solution_class: Solution
# submission_id: 1eb471d4d1af934d9e74b603850c0c063fdf44fc
# seed: 1423659379

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        deep = 1
        result, cnt = [], 0
        for c in S:
            if c == '(' and cnt >= deep:
                result.append(c)
            if c == ')' and cnt > deep:
                result.append(c)
            cnt += 1 if c == '(' else -1
        return "".join(result)