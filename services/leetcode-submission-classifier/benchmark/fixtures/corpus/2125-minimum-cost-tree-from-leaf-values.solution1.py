# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-tree-from-leaf-values
# source_path: LeetCode-Solutions-master/Python/minimum-cost-tree-from-leaf-values.py
# solution_class: Solution
# submission_id: f861824eb64b0449be7ac928a2e30d6c73badbbe
# seed: 544555041

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = 0
        stk = [float("inf")]
        for x in arr:
            while stk[-1] <= x:
                result += stk.pop() * min(stk[-1], x)
            stk.append(x)
        while len(stk) > 2:
            result += stk.pop() * stk[-1]
        return result