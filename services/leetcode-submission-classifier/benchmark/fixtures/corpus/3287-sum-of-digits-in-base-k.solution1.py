# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-digits-in-base-k
# source_path: LeetCode-Solutions-master/Python/sum-of-digits-in-base-k.py
# solution_class: Solution
# submission_id: 6a7e130120a69dbfde4b25481bb6865ef83451e7
# seed: 1648838509

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        result = 0
        while n:
            n, r = divmod(n, k)
            result += r
        return result