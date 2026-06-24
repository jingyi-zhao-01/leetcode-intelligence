# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: convert-integer-to-the-sum-of-two-no-zero-integers
# source_path: LeetCode-Solutions-master/Python/convert-integer-to-the-sum-of-two-no-zero-integers.py
# solution_class: Solution
# submission_id: 72dace7cac2890ca1fd5f6b867ff72ef3b253785
# seed: 3299378595

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        a, curr, base = 0, n, 1
        while curr: 
            if curr % 10 == 0 or (curr % 10 == 1 and curr != 1):
                a += base
                curr -= 10  # carry
            a += base
            base *= 10
            curr //= 10
        return [a, n-a]