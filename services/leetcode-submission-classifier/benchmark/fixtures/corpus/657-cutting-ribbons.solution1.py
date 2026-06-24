# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: cutting-ribbons
# source_path: LeetCode-Solutions-master/Python/cutting-ribbons.py
# solution_class: Solution
# submission_id: 727cb2017db2a70c4e5523c32c14a6d4b137f031
# seed: 408996204

# Time:  O(nlogr), r is sum(ribbons)/k
# Space: O(1)

class Solution(object):
    def maxLength(self, ribbons, k):
        """
        :type ribbons: List[int]
        :type k: int
        :rtype: int
        """
        def check(ribbons, k, s):
            return reduce(lambda total,x: total+x//s, ribbons, 0) >= k

        left, right = 1, sum(ribbons)//k
        while left <= right:
            mid = left + (right-left)//2
            if not check(ribbons, k, mid):
                right = mid-1
            else:
                left = mid+1
        return right