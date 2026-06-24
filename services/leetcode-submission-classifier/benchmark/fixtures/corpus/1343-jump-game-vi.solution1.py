# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: jump-game-vi
# source_path: LeetCode-Solutions-master/Python/jump-game-vi.py
# solution_class: Solution
# submission_id: 0d18b8a3a83d8f2c51e2fd4638fb2cad147206ad
# seed: 948512879

# Time:  O(n)
# Space: O(k)

import collections

class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        score = 0
        dq = collections.deque()
        for i, num in enumerate(nums):
            if dq and dq[0][0] == i-k-1:
                dq.popleft()
            score = num if not dq else dq[0][1]+num
            while dq and dq[-1][1] <= score:
                dq.pop()
            dq.append((i, score))
        return score