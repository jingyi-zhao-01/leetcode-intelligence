# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: ugly-number-ii
# source_path: LeetCode-Solutions-master/Python/ugly-number-ii.py
# solution_class: Solution2
# submission_id: 94d7555f29f9904e3cf9991ff43a74ae1a4dc880
# seed: 2113297308

# Time:  O(n)
# Space: O(1)

import heapq

class Solution2(object):
    ugly = sorted(2**a * 3**b * 5**c
                  for a in range(32) for b in range(20) for c in range(14))

    def nthUglyNumber(self, n):
        return self.ugly[n-1]