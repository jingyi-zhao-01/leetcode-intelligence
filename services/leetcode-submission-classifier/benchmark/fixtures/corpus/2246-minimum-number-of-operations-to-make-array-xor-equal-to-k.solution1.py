# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-operations-to-make-array-xor-equal-to-k
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-operations-to-make-array-xor-equal-to-k.py
# solution_class: Solution
# submission_id: 2bf09c7c5394c58e5a58eb7372dee76c7fa40204
# seed: 1708980699

# Time:  O(n)
# Space: O(1)

# bit manipulation

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def popcount(x):
            return bin(x).count('1')
    
        return popcount(reduce(lambda x, y: x^y, nums, k))