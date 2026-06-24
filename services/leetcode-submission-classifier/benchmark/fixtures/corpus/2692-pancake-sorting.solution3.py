# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: pancake-sorting
# source_path: LeetCode-Solutions-master/Python/pancake-sorting.py
# solution_class: Solution3
# submission_id: bf489d9e550bf16a47304bf0b0156b10b8a4645d
# seed: 2262654266

# Time:  O(nlogn)
# Space: O(n)

class BIT(object):  # 0-indexed.
    def __init__(self, n):
        self.__bit = [0]*(n+1)  # Extra one for dummy node.

    def add(self, i, val):
        i += 1  # Extra one for dummy node.
        while i < len(self.__bit):
            self.__bit[i] += val
            i += (i & -i)

    def query(self, i):
        i += 1  # Extra one for dummy node.
        ret = 0
        while i > 0:
            ret += self.__bit[i]
            i -= (i & -i)
        return ret

# bit solution

class Solution3(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def reverse(l, begin, end):
            for i in xrange((end-begin) // 2):
                l[begin+i], l[end-1-i] = l[end-1-i], l[begin+i]

        result = []
        for n in reversed(xrange(1, len(A)+1)):
            i = A.index(n)
            reverse(A, 0, i+1)
            result.append(i+1)
            reverse(A, 0, n)
            result.append(n)
        return result