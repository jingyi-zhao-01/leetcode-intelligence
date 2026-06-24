# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-bitwise-or-from-grid
# source_path: LeetCode-Solutions-master/Python/minimum-bitwise-or-from-grid.py
# solution_class: Solution
# submission_id: 423b1166ef4e82755913eb34484594577ed241be
# seed: 3956794082

# Time:  O(nlogr), r = max(nums)
# Space: O(1)

# bitmasks, greedy

class Solution(object):
    def minimumOR(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        mx = max(x for row in grid for x in row)
        result = 0
        for i in reversed(xrange(mx.bit_length())):
            if any(all(x&(result|((1<<i)-1)) != x for x in row) for row in grid):
                result |= 1<<i
        return result