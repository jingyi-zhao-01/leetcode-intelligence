# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-array-elements-zero
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-array-elements-zero.py
# solution_class: Solution
# submission_id: 7c5429e1cf9d4325b5927293ce85fa5ab8ab59f0
# seed: 1000383696

# Time:  O(qlogr)
# Space: O(1)

# greedy

class Solution(object):
    def minOperations(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: int
        """
        result = 0
        for l, r in queries:
            total = 0
            base = i = 1
            while base <= r:
                nl, nr = max(l, base), min(r, 4*base-1)
                if nl <= nr:
                    total += i*(nr-nl+1)
                i += 1
                base *= 4
            result += (total+1)//2
        return result