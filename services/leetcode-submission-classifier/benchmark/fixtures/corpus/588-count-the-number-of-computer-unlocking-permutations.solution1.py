# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-computer-unlocking-permutations
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-computer-unlocking-permutations.py
# solution_class: Solution
# submission_id: 4a0e8ec7cf0a32506bc94a0e11a578406d5aa2d7
# seed: 3266842779

# Time:  O(n)
# Space: O(1)

# combinatorics

class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        def factorial(n):
            return reduce(lambda accu, x: (accu*x)%MOD, xrange(1, n+1), 1)

        return factorial(len(complexity)-1) if all(complexity[0] < complexity[i] for i in xrange(1, len(complexity))) else 0