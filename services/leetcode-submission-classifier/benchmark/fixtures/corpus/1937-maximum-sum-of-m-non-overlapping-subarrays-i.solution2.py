# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-sum-of-m-non-overlapping-subarrays-i
# source_path: LeetCode-Solutions-master/Python/maximum-sum-of-m-non-overlapping-subarrays-i.py
# solution_class: Solution2
# submission_id: edc4d396df858085ddf5303c4afc842d1f99ed2a
# seed: 539688183

# Time:  O(nlogr)
# Space: O(n)

import collections


# prefix sum, dp, mono deque, wqs binary search, alien trick

class Solution2(object):
    def maximumSum(self, nums, m, l, r):
        """
        :type nums: List[int]
        :type m: int
        :type l: int
        :type r: int
        :rtype: int
        """        
        NEG_INF = float("-inf")
        prefix = [0]*(len(nums)+1)
        for i in xrange(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
        result = NEG_INF
        dp = [0]*(len(nums)+1)
        for _ in xrange(m):
            new_dp = [NEG_INF]*(len(nums)+1)
            dq = collections.deque()
            for i in xrange(1, len(nums)+1):
                new_dp[i] = new_dp[i-1]
                j = i-l
                if j >= 0 and dp[j] is not NEG_INF:
                    while dq and dp[dq[-1]]-prefix[dq[-1]] <= dp[j]-prefix[j]:
                        dq.pop()
                    dq.append(j)
                while dq and dq[0] < i-r:
                    dq.popleft()
                if dq:
                    new_dp[i] = max(new_dp[i], (dp[dq[0]]-prefix[dq[0]])+prefix[i])
            dp = new_dp
            result = max(result, dp[-1])
        return result