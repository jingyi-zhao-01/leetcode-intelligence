# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-zeros-in-decimal-representation
# source_path: LeetCode-Solutions-master/Python/remove-zeros-in-decimal-representation.py
# solution_class: Solution
# submission_id: c1938c617178cbaed435b494b8ffd07a2b483ed8
# seed: 644959770

# Time:  O(logn)
# Space: O(1)

# math

class Solution(object):
    def removeZeros(self, n):
        """
        :type n: int
        :rtype: int
        """
        def reverse(n):
            result = 0
            while n:
                n, r = divmod(n, 10)
                result = result*10+r
            return result
    
        result = 0
        while n:
            n, r = divmod(n, 10)
            if r:
                result = result*10+r
        return reverse(result)