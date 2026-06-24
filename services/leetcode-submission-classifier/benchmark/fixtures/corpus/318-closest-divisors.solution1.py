# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: closest-divisors
# source_path: LeetCode-Solutions-master/Python/closest-divisors.py
# solution_class: Solution
# submission_id: ffc5ec4f80f4538c1265488d35d1518c80d8df51
# seed: 2206360957

# Time:  O(sqrt(n))
# Space: O(1)

class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def divisors(n):
            for d in reversed(xrange(1, int(n**0.5)+1)):
                if n % d == 0:
                    return d, n//d
            return 1, n

        return min([divisors(num+1), divisors(num+2)], key=lambda x: x[1]-x[0])