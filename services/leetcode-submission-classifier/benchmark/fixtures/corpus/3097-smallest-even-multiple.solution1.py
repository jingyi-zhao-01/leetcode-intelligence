# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-even-multiple
# source_path: LeetCode-Solutions-master/Python/smallest-even-multiple.py
# solution_class: Solution
# submission_id: 6573c8a647100588ba91f5d0ae059e2c04f1743e
# seed: 1340505442

# Time:  O(1)
# Space: O(1)

# math, bit manipulation

class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n<<(n&1)