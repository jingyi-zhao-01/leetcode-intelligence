# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-number-is-a-sum-of-powers-of-three
# source_path: LeetCode-Solutions-master/Python/check-if-number-is-a-sum-of-powers-of-three.py
# solution_class: Solution
# submission_id: 6da7931440a3aa892510f7d138d14e303e59cdad
# seed: 1978191704

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 0:
            if n%3 == 2:
                return False
            n //= 3
        return True