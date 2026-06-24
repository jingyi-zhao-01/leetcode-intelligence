# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-one-bit-operations-to-make-integers-zero
# source_path: LeetCode-Solutions-master/Python/minimum-one-bit-operations-to-make-integers-zero.py
# solution_class: Solution
# submission_id: f4d9890a0e765bb0ff779cbe7e117b26bb0bae09
# seed: 2237433519

# Time:  O(logn)
# Space: O(1)

# reference: https://en.wikipedia.org/wiki/Gray_code

class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        def gray_to_binary(n):
            result = 0
            while n:
                result ^= n
                n >>= 1
            return result
        
        # [observation]
        # n    f(n)
        # 000    0
        # 001    1
        # 011    2
        # 010    3
        # 110    4
        # 111    5
        # 101    6
        # 100    7
	# f(0XX...X) + f(1XX...X) = f(100...0) implies n is a gray code
        # => f(n) is actually the inverse of gray code
        return gray_to_binary(n)