# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-value-after-insertion
# source_path: LeetCode-Solutions-master/Python/maximum-value-after-insertion.py
# solution_class: Solution
# submission_id: 0c33ec0b268af9b1909d912618ecc7dc7a9a4913
# seed: 274526531

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """
        check = (lambda i: str(x) > n[i]) if n[0] != '-' else (lambda i: str(x) < n[i])
        for i in xrange(len(n)):
            if check(i):
                break
        else:
            i = len(n)
        return n[:i] + str(x) + n[i:]