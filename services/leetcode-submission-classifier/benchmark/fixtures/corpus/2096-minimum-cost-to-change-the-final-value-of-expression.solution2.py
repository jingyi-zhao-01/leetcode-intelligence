# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-change-the-final-value-of-expression
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-change-the-final-value-of-expression.py
# solution_class: Solution2
# submission_id: 8abce44bcae705e2ec162e094af82cba712915e7
# seed: 3101172185

# Time:  O(n)
# Space: O(n)

class Solution2(object):
    def minOperationsToFlip(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        stk = [[None]*3]
        for c in expression:                                
            if c == '(':                                            
                stk.append([None]*3)
            elif c in {')', '0', '1'}:
                if c == ')':
                    dp0, dp1, _ = stk.pop()
                else:
                    dp0, dp1 = int(c != '0'), int(c != '1')
                if stk[-1][2] == '&':
                    stk[-1] = [min(stk[-1][0], dp0),
                               min(stk[-1][1]+dp1, min(stk[-1][1], dp1)+1),
                               None]
                elif stk[-1][2] == '|':
                    stk[-1] = [min(stk[-1][0]+dp0, min(stk[-1][0], dp0)+1),
                               min(stk[-1][1], dp1),
                               None]
                else:  # operand
                    stk[-1] = [dp0, dp1, None]
            else:
                stk[-1][2] = c
        return max(stk[0][0], stk[0][1])