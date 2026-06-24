# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-good-numbers
# source_path: LeetCode-Solutions-master/Python/count-good-numbers.py
# solution_class: Solution2
# submission_id: 1919bd55a522bc8f7616be375c281671d5c2a463
# seed: 3901167264

# Time:  O(logn)
# Space: O(1)

class Solution2(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        return pow(5, (n+1)//2%(MOD-1), MOD)*pow(4, n//2%(MOD-1), MOD) % MOD