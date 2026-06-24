# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-removals-to-achieve-target-xor
# source_path: LeetCode-Solutions-master/Python/minimum-removals-to-achieve-target-xor.py
# solution_class: Solution2
# submission_id: d5d4e7c2b24774ae3ae554db1689f71a469a1796
# seed: 555558299

# Time:  O(n * r), r = max(nums)
# Space: O(r)

# bitmasks, bfs

class Solution2(object):
    def minRemovals(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = {}
        dp[0] = 0
        for x in nums:
            target ^= x
            new_dp = {k:v for k, v in dp.iteritems()}
            for k in dp.iterkeys():
                if k^x not in new_dp or new_dp[k^x] > dp[k]+1:
                    new_dp[k^x] = dp[k]+1
            dp = new_dp
        return dp[target] if target in dp else -1