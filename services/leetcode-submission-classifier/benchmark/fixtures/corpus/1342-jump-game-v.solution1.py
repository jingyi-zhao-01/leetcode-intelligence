# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: jump-game-v
# source_path: LeetCode-Solutions-master/Python/jump-game-v.py
# solution_class: Solution
# submission_id: f2d443ac107eab5fcbf6167725a2f261c64f58fc
# seed: 1251064994

# Time:  O(n)
# Space: O(n)

import collections
import itertools


# sliding window + top-down dp

class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        def dp(arr, d, i, left, right, lookup):
            if lookup[i]:
                return lookup[i]
            lookup[i] = 1
            for j in itertools.chain(left[i], right[i]):
                # each dp[j] will be visited at most twice 
                lookup[i] = max(lookup[i], dp(arr, d, j, left, right, lookup)+1)
            return lookup[i]

        left, decreasing_dq = [[] for _ in xrange(len(arr))], collections.deque()
        for i in xrange(len(arr)):
            if decreasing_dq and i - decreasing_dq[0] == d+1:
                decreasing_dq.popleft()
            while decreasing_dq and arr[decreasing_dq[-1]] < arr[i]:
                if left[i] and arr[left[i][-1]] != arr[decreasing_dq[-1]]:
                    left[i] = []
                left[i].append(decreasing_dq.pop())
            decreasing_dq.append(i)
        right, decreasing_dq = [[] for _ in xrange(len(arr))], collections.deque()
        for i in reversed(xrange(len(arr))):
            if decreasing_dq and decreasing_dq[0] - i == d+1:
                decreasing_dq.popleft()
            while decreasing_dq and arr[decreasing_dq[-1]] < arr[i]:
                if right[i] and arr[right[i][-1]] != arr[decreasing_dq[-1]]:
                    right[i] = []
                right[i].append(decreasing_dq.pop())
            decreasing_dq.append(i)

        lookup = [0]*len(arr)
        return max(itertools.imap(lambda x: dp(arr, d, x, left, right, lookup), xrange(len(arr))))