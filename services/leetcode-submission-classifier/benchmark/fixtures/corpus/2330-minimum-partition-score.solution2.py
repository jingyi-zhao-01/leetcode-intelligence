# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-partition-score
# source_path: LeetCode-Solutions-master/Python/minimum-partition-score.py
# solution_class: Solution2
# submission_id: 41d6ead08272f9a2949510744003a4f6f97cb26a
# seed: 1598798469

# Time:  O(n * log(n * r)) = O(nlogn + nlogr), r = max(nums)
# Space: O(n)

import collections


# prefix sum, dp, convex hull trick, wqs binary search, alien trick

class Solution2(object):
    def minPartitionScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def check(l1, l2, l3):
            return (l2[1]-l1[1])*(l2[0]-l3[0]) < (l3[1]-l2[1])*(l1[0]-l2[0])

        INF = float("inf")
        prefix = [0]*(len(nums)+1)
        for i in xrange(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
        dp = [INF]*(len(nums)+1)
        dp[0] = 0
        for j in xrange(k):
            new_dp = [INF]*(len(nums)+1)
            hull = collections.deque()
            for i in xrange(j, len(nums)):
                if dp[i] is not INF:
                    x = prefix[i]
                    line = (-x, dp[i]+(x*x-x)//2)
                    while len(hull) >= 2 and not check(hull[-2], hull[-1], line):
                        hull.pop()
                    hull.append(line)
                x = prefix[i+1]
                while len(hull) >= 2 and hull[0][0]*x+hull[0][1] >= hull[1][0]*x+hull[1][1]:
                    hull.popleft()
                new_dp[i+1] = hull[0][0]*x+hull[0][1]+(x*x+x)//2
            dp = new_dp
        return dp[-1]