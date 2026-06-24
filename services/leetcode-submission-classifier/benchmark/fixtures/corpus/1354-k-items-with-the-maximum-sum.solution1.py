# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: k-items-with-the-maximum-sum
# source_path: LeetCode-Solutions-master/Python/k-items-with-the-maximum-sum.py
# solution_class: Solution
# submission_id: 63741eb0658c5bd164f2a4b653ff3767cba06f63
# seed: 1860702571

# Time:  O(1)
# Space: O(1)

# greedy, math

class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        """
        :type numOnes: int
        :type numZeros: int
        :type numNegOnes: int
        :type k: int
        :rtype: int
        """
        return min(numOnes, k)-max(k-numOnes-numZeros, 0)