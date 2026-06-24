# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: xor-operation-in-an-array
# source_path: LeetCode-Solutions-master/Python/xor-operation-in-an-array.py
# solution_class: Solution2
# submission_id: 0be91b32e0c2981e6008960f58881013fbd5b1b2
# seed: 820543651

# Time:  O(1)
# Space: O(1)

class Solution2(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        return reduce(operator.xor, (i for i in xrange(start, start+2*n, 2)))