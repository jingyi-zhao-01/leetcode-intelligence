# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-xor-sum-of-all-pairs-bitwise-and
# source_path: LeetCode-Solutions-master/Python/find-xor-sum-of-all-pairs-bitwise-and.py
# solution_class: Solution
# submission_id: a2f6342bd1402afc3a90b99eb4d59854ef13f397
# seed: 3961352770

# Time:  O(n)
# Space: O(1)

import operator

class Solution(object):
    def getXORSum(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        return reduce(operator.xor, arr1) & reduce(operator.xor, arr2)