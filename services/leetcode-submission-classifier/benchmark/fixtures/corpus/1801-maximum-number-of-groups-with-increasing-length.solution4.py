# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-groups-with-increasing-length
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-groups-with-increasing-length.py
# solution_class: Solution4
# submission_id: e9d1d9d005fc0b45065b5e8b445419d6b81cea40
# seed: 3157108633

# Time:  O(n)
# Space: O(n)

# constructive algorithms, counting sort, greedy

class Solution4(object):
    def maxIncreasingGroups(self, usageLimits):
        """
        :type usageLimits: List[int]
        :rtype: int
        """
        def check(l):
            return all((i+1)*i//2 <= prefix[len(usageLimits)-(l-i)] for i in xrange(1, l+1))

        usageLimits.sort()
        prefix = [0]*(len(usageLimits)+1)
        for i in xrange(len(usageLimits)):
            prefix[i+1] = prefix[i]+usageLimits[i]
        left, right = 1, len(usageLimits)
        while left <= right:
            mid = left + (right-left)//2
            if not check(mid):
                right = mid-1
            else:
                left = mid+1
        return right