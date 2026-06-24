# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-grid-happiness
# source_path: LeetCode-Solutions-master/Python/maximize-grid-happiness.py
# solution_class: Solution
# submission_id: e4ac427310c4e2e2530ee92a14a17422d7128ba9
# seed: 3678934463

# Time:  O(C(m * n, i) * C(m * n - i, e))
# Space: O(min(m * n, i + e))

class Solution(object):
    def getMaxGridHappiness(self, m, n, introvertsCount, extrovertsCount):
        """
        :type m: int
        :type n: int
        :type introvertsCount: int
        :type extrovertsCount: int
        :rtype: int
        """
        def left(curr):
            return curr[-1] if len(curr)%n else 0

        def up(curr):
            return curr[-n] if len(curr) >= n else 0 

        def count_total(curr, t, total):
            return (total
                    - 30*((left(curr) == 1)+(up(curr) == 1))
                    + 20*((left(curr) == 2)+(up(curr) == 2))
                    + (120 - 30*((left(curr) != 0)+(up(curr) != 0)))*(t == 1)
                    + ( 40 + 20*((left(curr) != 0)+(up(curr) != 0)))*(t == 2))
        
        def iter_backtracking(i, e):
            result = 0
            curr = []
            stk = [(2, (i, e, 0))]
            while stk:
                step, params = stk.pop()
                if step == 2:
                    i, e, total = params             
                    if len(curr) == m*n or (i == 0 and e == 0):
                        result = max(result, total)                
                        continue
                    if total + (i+e)*120 < result:  # pruning
                        continue
                    if e > 0:
                        stk.append((3, tuple()))
                        stk.append((2, (i, e-1, count_total(curr, 2, total))))
                        stk.append((1, (2,)))
                    if i > 0:
                        stk.append((3, tuple()))
                        stk.append((2, (i-1, e, count_total(curr, 1, total))))
                        stk.append((1, (1,)))
                    if left(curr) or up(curr):  # leave unoccupied iff left or up is occupied
                        stk.append((3, tuple()))
                        stk.append((2, (i, e, total)))
                        stk.append((1, (0,)))
                elif step == 1:
                    x = params[0]
                    curr.append(x)
                elif step == 3:
                    curr.pop()
            return result
          
        return iter_backtracking(introvertsCount, extrovertsCount)