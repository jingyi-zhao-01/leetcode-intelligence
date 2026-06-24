# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-sum-of-values-by-dividing-array
# source_path: LeetCode-Solutions-master/Python/minimum-sum-of-values-by-dividing-array.py
# solution_class: Solution
# submission_id: 5d8a488c8a9a90071193a96de0df0c57b7c5ab48
# seed: 3419852443

# Time:  O(n * m * logr), r = max(nums)
# Space: O(n + logr)

import collections


# dp, mono deque, two pointers

class Solution(object):
    def minimumValueSum(self, nums, andValues):
        """
        :type nums: List[int]
        :type andValues: List[int]
        :rtype: int
        """
        INF = float("inf")
        L = max(nums).bit_length()
        def update(cnt, x, d):
            for i in xrange(L):
                if x&(1<<i):
                    cnt[i] += d
        
        def mask(cnt, l):
            return reduce(lambda accu, i: accu|(1<<i), (i for i  in xrange(L) if cnt[i] == l), 0)

        dp = [INF]*(len(nums)+1)
        dp[0] = 0
        for j in xrange(len(andValues)):
            new_dp = [INF]*(len(nums)+1)
            cnt = [0]*L
            l = [0]*len(dp)
            dq = collections.deque()
            left = idx = j
            for right in xrange(j, len(nums)):
                update(cnt, nums[right], +1)
                if mask(cnt, right-left+1) <= andValues[j]:
                    while left <= right:
                        if mask(cnt, right-left+1) > andValues[j]:
                            break
                        update(cnt, nums[left], -1)
                        left += 1
                    left -= 1
                    update(cnt, nums[left], +1)  # try to move to the last left s.t. mask(cnt, right-left+1) == andValues[j]
                if (andValues[j]&nums[right]) == andValues[j]:
                    l[right + 1] = l[right]+1
                if mask(cnt, right-left+1) != andValues[j]:
                    continue
                # new_dp[right+1] = min(dp[left-l[left]], dp[left-l[left]+1], ..., dp[left])+nums[right]
                while idx <= left:
                    while dq and dp[dq[-1]] >= dp[idx]:
                        dq.pop()
                    dq.append(idx)
                    idx += 1
                while dq and dq[0] < left-l[left]:
                    dq.popleft()
                if dq:
                    new_dp[right+1] = dp[dq[0]]+nums[right]
            dp = new_dp
        return dp[-1] if dp[-1] != INF else -1