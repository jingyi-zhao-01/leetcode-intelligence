# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: jump-game-v
# source_path: LeetCode-Solutions-master/Python/jump-game-v.py
# solution_class: Solution2
# submission_id: 2970af7f0da6b13d2285b52d43fd66ca200ac7bc
# seed: 3056815555

# Time:  O(n)
# Space: O(n)

import collections
import itertools


# sliding window + top-down dp

class Solution2(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        left, decreasing_stk = [[] for _ in xrange(len(arr))], []
        for i in xrange(len(arr)):
            while decreasing_stk and arr[decreasing_stk[-1]] < arr[i]:
                if i - decreasing_stk[-1] <= d:
                    if left[i] and arr[left[i][-1]] != arr[decreasing_stk[-1]]:
                        left[i] = []
                    left[i].append(decreasing_stk[-1])
                decreasing_stk.pop()
            decreasing_stk.append(i)
        right, decreasing_stk = [[] for _ in xrange(len(arr))], []
        for i in reversed(xrange(len(arr))):
            while decreasing_stk and arr[decreasing_stk[-1]] < arr[i]:
                if decreasing_stk[-1] - i <= d:
                    if right[i] and arr[right[i][-1]] != arr[decreasing_stk[-1]]:
                        right[i] = []
                    right[i].append(decreasing_stk[-1])
                decreasing_stk.pop()
            decreasing_stk.append(i)

        dp = [0]*len(arr)
        for a, i in sorted([a, i] for i, a in enumerate(arr)):
            dp[i] = 1
            for j in itertools.chain(left[i], right[i]):
                # each dp[j] will be visited at most twice 
                dp[i] = max(dp[i], dp[j]+1)
        return max(dp)