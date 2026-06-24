# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: circular-permutation-in-binary-representation
# source_path: LeetCode-Solutions-master/Python/circular-permutation-in-binary-representation.py
# solution_class: Solution
# submission_id: a75f73aa62fd332819e5eb6ffd3b0df4e34f04c1
# seed: 1653660923

# Time:  O(2^n)
# Space: O(1)

class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        return [start ^ (i>>1) ^ i for i in xrange(1<<n)]