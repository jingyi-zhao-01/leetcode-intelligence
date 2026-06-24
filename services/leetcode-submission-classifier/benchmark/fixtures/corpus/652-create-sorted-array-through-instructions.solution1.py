# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: create-sorted-array-through-instructions
# source_path: LeetCode-Solutions-master/Python/create-sorted-array-through-instructions.py
# solution_class: Solution
# submission_id: e11add6bd32f962c85fdee9c4c5a7e8cf97c2971
# seed: 1805548706

# Time:  O(nlogm)
# Space: O(m)

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

class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        bit = BIT(max(instructions))
        result = 0
        for i, inst in enumerate(instructions):
            inst -= 1
            result += min(bit.query(inst-1), i-bit.query(inst))
            bit.add(inst, 1)
        return result % MOD