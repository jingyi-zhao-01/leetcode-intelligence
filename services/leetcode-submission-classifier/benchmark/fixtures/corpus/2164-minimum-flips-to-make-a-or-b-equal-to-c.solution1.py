# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-flips-to-make-a-or-b-equal-to-c
# source_path: LeetCode-Solutions-master/Python/minimum-flips-to-make-a-or-b-equal-to-c.py
# solution_class: Solution
# submission_id: 7060094b2bd1358c3e9ef40aa7634e4cfee905b5
# seed: 2939108743

# Time:  O(31)
# Space: O(1)

class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        def number_of_1_bits(n):
            result = 0
            while n:
                n &= n-1
                result += 1
            return result

        return number_of_1_bits((a|b)^c) + number_of_1_bits(a&b&~c)