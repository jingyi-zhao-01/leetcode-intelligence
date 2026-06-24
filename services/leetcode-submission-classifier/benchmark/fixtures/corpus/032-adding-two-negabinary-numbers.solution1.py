# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: adding-two-negabinary-numbers
# source_path: LeetCode-Solutions-master/Python/adding-two-negabinary-numbers.py
# solution_class: Solution
# submission_id: 9731c18414b60f5c9feb4cfda7ec8d41b3d3750e
# seed: 3488334067

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        result = []
        carry = 0
        while arr1 or arr2 or carry:
            if arr1:
                carry += arr1.pop()
            if arr2:
                carry += arr2.pop()
            result.append(carry & 1)
            carry = -(carry >> 1)
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        result.reverse()
        return result