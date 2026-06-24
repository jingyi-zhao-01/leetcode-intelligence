# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-k-th-lucky-number
# source_path: LeetCode-Solutions-master/Python/find-the-k-th-lucky-number.py
# solution_class: Solution2
# submission_id: a43ff50d7cfadbcfa9efb4d8971f816f69440445
# seed: 546726285

# Time:  O(logn)
# Space: O(1)

# math, bitmasks

class Solution2(object):
    def kthLuckyNumber(self, k):
        """
        :type k: int
        :rtype: str
        """
        return bin(k+1)[3:].replace('1', '7').replace('0', '4')