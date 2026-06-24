# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-k-th-character-in-string-game-ii
# source_path: LeetCode-Solutions-master/Python/find-the-k-th-character-in-string-game-ii.py
# solution_class: Solution
# submission_id: 48b1e3b1c54bf9a86f7d2736b67b5b63fa2a3cbb
# seed: 2154874290

# Time:  O(logr) = O(1)
# Space: O(1)

# bitmasks

class Solution(object):
    def kthCharacter(self, k, operations):
        """
        :type k: int
        :type operations: List[int]
        :rtype: str
        """
        result = 0
        k -= 1
        for i in xrange(min(len(operations), k.bit_length())):
            if k&(1<<i):
                result = (result+operations[i])%26
        return chr(ord('a')+result)