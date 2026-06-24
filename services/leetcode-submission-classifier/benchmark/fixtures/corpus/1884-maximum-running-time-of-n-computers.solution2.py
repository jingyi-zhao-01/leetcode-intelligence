# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-running-time-of-n-computers
# source_path: LeetCode-Solutions-master/Python/maximum-running-time-of-n-computers.py
# solution_class: Solution2
# submission_id: 98450afcdc00cc0247e3029d662d44ead94e6447
# seed: 3608434104

# Time:  O(nlogm)
# Space: O(1)

import heapq


# greedy

class Solution2(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        def check(n, batteries, x):
            return sum(min(b, x) for b in batteries) >= n*x

        left, right = min(batteries), sum(batteries)//n
        while left <= right:
            mid = left + (right-left)//2
            if not check(n, batteries, mid):
                right = mid-1
            else:
                left = mid+1
        return right