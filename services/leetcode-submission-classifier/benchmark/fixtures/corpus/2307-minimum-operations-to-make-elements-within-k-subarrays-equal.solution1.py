# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-elements-within-k-subarrays-equal
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-elements-within-k-subarrays-equal.py
# solution_class: Solution
# submission_id: 10ac58c86907e6f3c8327ce21a680c18a24bc34e
# seed: 1648726193

# Time:  O(nlogx + k * n)
# Space: O(n)

from sortedcontainers import SortedList


# two sorted lists, dp

class Solution(object):
    def minOperations(self, nums, x, k):
        """
        :type nums: List[int]
        :type x: int
        :type k: int
        :rtype: int
        """
        class SlidingWindow(object):
            def __init__(self):
                self.left = SortedList()
                self.right = SortedList()
                self.total1 = self.total2 = 0

            def add(self, val):
                if not self.left or val <= self.left[-1]:
                    self.left.add(val)
                    self.total1 += val
                else:
                    self.right.add(val)
                    self.total2 += val
                self.rebalance()

            def remove(self, val):
                if val <= self.left[-1]:
                    self.left.remove(val)
                    self.total1 -= val
                else:
                    self.right.remove(val)
                    self.total2 -= val
                self.rebalance()

            def rebalance(self):
                if len(self.left) < len(self.right):
                    self.total2 -= self.right[0]
                    self.total1 += self.right[0]
                    self.left.add(self.right[0])
                    self.right.pop(0)
                elif len(self.left) > len(self.right)+1:
                    self.total1 -= self.left[-1]
                    self.total2 += self.left[-1]
                    self.right.add(self.left[-1])
                    self.left.pop()

            def median(self):
                return self.left[-1]


        INF = float("inf")
        sw = SlidingWindow()
        cost = [INF]*(len(nums)+1)
        for i in xrange(len(nums)):
            if i-x >= 0:
                sw.remove(nums[i-x])
            sw.add(nums[i])
            if i >= x-1:
                cost[i+1] = (sw.median()*len(sw.left)-sw.total1) + (sw.total2-sw.median()*len(sw.right))
        dp = [0]*(len(nums)+1)
        for i in xrange(k):
            new_dp = [INF]*(len(nums)+1)
            for j in xrange((i+1)*x, len(nums)+1):
                new_dp[j] = min(new_dp[j-1], dp[j-x]+cost[j])
            dp = new_dp
        return dp[-1]