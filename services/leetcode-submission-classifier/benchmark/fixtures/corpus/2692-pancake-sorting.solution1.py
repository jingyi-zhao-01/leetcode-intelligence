# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: pancake-sorting
# source_path: LeetCode-Solutions-master/Python/pancake-sorting.py
# solution_class: Solution
# submission_id: 32c416032af86397312aa918e640233dc74a5fff
# seed: 739456413

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

class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        bit = BIT(len(arr))
        result = []
        for i in xrange(len(arr)):
            n = bit.query((arr[i]-1)-1)
            bit.add(arr[i]-1, 1)
            if n == i:  # already sorted
                continue
            if n == 0:                # (0..i-1)i
                if i > 1:
                    result.append(i)  # (i-1..0)i
                result.append(i+1)    # i(0..i-1)
            else:                     # (0..n-1)n(n+1..i-1)i
                if n > 1:
                    result.append(n)  # (n-1..0)n(n+1..i-1)i
                result.append(i)      # (i-1..n+1)n(0..n-1)i
                result.append(i+1)    # i(n-1..0)n(n+1..i-1)
                result.append(n+1)    # (0..n-1)in(n+1..i-1)
        return result