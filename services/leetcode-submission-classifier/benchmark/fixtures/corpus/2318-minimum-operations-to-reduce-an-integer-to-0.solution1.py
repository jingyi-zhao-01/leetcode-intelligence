# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-reduce-an-integer-to-0
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-reduce-an-integer-to-0.py
# solution_class: Solution
# submission_id: d26e4812948dc7a69de371199628df9683be6529
# seed: 2245647394

# Time:  O(logn)
# Space: O(1)

# greedy, trick
# reference: https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/solutions/3203994/java-c-python-1-line-solution/

class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        def popcount(x):
            return bin(x)[2:].count('1')

        return popcount(n^(n*0b11))