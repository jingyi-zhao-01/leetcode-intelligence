# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-1-bits
# source_path: LeetCode-Solutions-master/Python/number-of-1-bits.py
# solution_class: Solution4
# submission_id: 02264ca90896913afd29096748f5d97eed57e47b
# seed: 1065057636

# Time:  O(32), bit shift in python is not O(1), it's O(k), k is the number of bits shifted
#             , see https://github.com/python/cpython/blob/2.7/Objects/longobject.c#L3652
# Space: O(1)

class Solution4(object):
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n: int) -> int:
        b="{0:b}".format(n)
        result=b.count("1")
        return result