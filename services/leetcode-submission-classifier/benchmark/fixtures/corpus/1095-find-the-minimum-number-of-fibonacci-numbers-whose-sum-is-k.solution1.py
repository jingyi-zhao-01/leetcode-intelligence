# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k
# source_path: LeetCode-Solutions-master/Python/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k.py
# solution_class: Solution
# submission_id: 9c125febccc4dc86480cfe23c06c6b878c454480
# seed: 3010591536

# Time:  O(logk)
# Space: O(1)

class Solution(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        result, a, b = 0, 1, 1
        while b <= k:
            b, a = a+b, b
        while k:
            if a <= k:
                k -= a
                result += 1
            a, b = b-a, a
        return result