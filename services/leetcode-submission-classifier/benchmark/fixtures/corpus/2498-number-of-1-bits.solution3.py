# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-1-bits
# source_path: LeetCode-Solutions-master/Python/number-of-1-bits.py
# solution_class: Solution3
# submission_id: 6671383bb0ed3747d07c00bff27c95033eda169c
# seed: 2162386115

# Time:  O(32), bit shift in python is not O(1), it's O(k), k is the number of bits shifted
#             , see https://github.com/python/cpython/blob/2.7/Objects/longobject.c#L3652
# Space: O(1)

class Solution3(object):
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        result = 0
        while n:
            n &= n - 1
            result += 1
        return result