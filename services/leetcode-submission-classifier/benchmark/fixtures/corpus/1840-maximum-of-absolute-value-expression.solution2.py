# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-of-absolute-value-expression
# source_path: LeetCode-Solutions-master/Python/maximum-of-absolute-value-expression.py
# solution_class: Solution2
# submission_id: ad593170b0560511962f77b384bdaae4f79a9d16
# seed: 4176877667

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        return max(max(c1*arr1[i] + c2*arr2[i] + i for i in xrange(len(arr1))) -
                   min(c1*arr1[i] + c2*arr2[i] + i for i in xrange(len(arr1)))
                   for c1 in [1, -1] for c2 in [1, -1])