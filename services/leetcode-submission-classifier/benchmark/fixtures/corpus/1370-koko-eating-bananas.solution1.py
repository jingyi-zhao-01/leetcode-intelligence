# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: koko-eating-bananas
# source_path: LeetCode-Solutions-master/Python/koko-eating-bananas.py
# solution_class: Solution
# submission_id: 0d9931fb5db512a093839c7a1e085bfa20a6f2ff
# seed: 3041251641

# Time:  O(nlogr)
# Space: O(1)

class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def possible(piles, H, K):
            return sum((pile-1)//K+1 for pile in piles) <= H

        left, right = 1, max(piles)
        while left <= right:
            mid = left + (right-left)//2
            if possible(piles, H, mid):
                right = mid-1
            else:
                left = mid+1
        return left