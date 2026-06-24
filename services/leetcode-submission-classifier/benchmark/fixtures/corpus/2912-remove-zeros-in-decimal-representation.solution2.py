# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-zeros-in-decimal-representation
# source_path: LeetCode-Solutions-master/Python/remove-zeros-in-decimal-representation.py
# solution_class: Solution2
# submission_id: 2fe88931884a42966f3877d04d0c49584a4460cf
# seed: 2670836197

# Time:  O(logn)
# Space: O(1)

# math

class Solution2(object):
    def removeZeros(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = "".join(x for x in str(n) if x != '0')
        return int(result) if result else 0