# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-k-th-lucky-number
# source_path: LeetCode-Solutions-master/Python/find-the-k-th-lucky-number.py
# solution_class: Solution
# submission_id: 5a7e6ac8dd5d966616a39c14b2441ef01fd85459
# seed: 485039060

# Time:  O(logn)
# Space: O(1)

# math, bitmasks

class Solution(object):
    def kthLuckyNumber(self, k):
        """
        :type k: int
        :rtype: str
        """
        result = []
        k += 1
        while k != 1:
            result.append('7' if k&1 else '4')
            k >>= 1
        result.reverse()
        return "".join(result)