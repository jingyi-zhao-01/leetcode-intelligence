# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-groups-with-increasing-length
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-groups-with-increasing-length.py
# solution_class: Solution3
# submission_id: 6ea524962dd5acfde7cf8e83eb461a5d3aef07d3
# seed: 690597919

# Time:  O(n)
# Space: O(n)

# constructive algorithms, counting sort, greedy

class Solution3(object):
    def maxIncreasingGroups(self, usageLimits):
        """
        :type usageLimits: List[int]
        :rtype: int
        """
        def check(l):
            curr = 0
            for i in xrange(l):
                curr += usageLimits[~i]-(l-i)
                curr = min(curr, 0)
            for i in xrange(len(usageLimits)-l):
                curr += usageLimits[i]
            return curr >= 0

        usageLimits.sort()
        left, right = 1, len(usageLimits)
        while left <= right:
            mid = left + (right-left)//2
            if not check(mid):
                right = mid-1
            else:
                left = mid+1
        return right