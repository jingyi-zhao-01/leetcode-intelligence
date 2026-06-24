# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-integers-with-even-digit-sum
# source_path: LeetCode-Solutions-master/Python/count-integers-with-even-digit-sum.py
# solution_class: Solution
# submission_id: 3291257ae622ad21913149e8914312b40a6904a4
# seed: 3640068449

# Time:  O(logn)
# Space: O(1)

# math

class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        def parity(x):
            result = 0
            while x:
                result += x%10
                x //= 10
            return result%2

        return (num-parity(num))//2