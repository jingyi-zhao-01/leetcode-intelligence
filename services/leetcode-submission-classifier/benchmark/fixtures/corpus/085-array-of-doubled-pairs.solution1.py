# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: array-of-doubled-pairs
# source_path: LeetCode-Solutions-master/Python/array-of-doubled-pairs.py
# solution_class: Solution
# submission_id: eee4b5693211f5a3e03e57095e5ad1a826c850d6
# seed: 2635557476

# Time:  O(n + klogk)
# Space: O(k)

import collections

class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        count = collections.Counter(A)
        for x in sorted(count, key=abs):
            if count[x] > count[2*x]:
                return False
            count[2*x] -= count[x]
        return True