# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: closest-divisors
# source_path: LeetCode-Solutions-master/Python/closest-divisors.py
# solution_class: Solution2
# submission_id: 0dccd2609115b55240deced24e6dcb93af841acc
# seed: 3017470955

# Time:  O(sqrt(n))
# Space: O(1)

class Solution2(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result, d = [1, num+1], 1
        while d*d <= num+2:
            if (num+2) % d == 0:
                result = [d, (num+2)//d]
            if (num+1) % d == 0:
                result = [d, (num+1)//d]
            d += 1
        return result