# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-x-sum-of-all-k-long-subarrays-i
# source_path: LeetCode-Solutions-master/Python/find-x-sum-of-all-k-long-subarrays-i.py
# solution_class: Solution
# submission_id: b7e2bd9c9049451859bbfe627befe10d93413228
# seed: 899583798

# Time:  O(nlogn)
# Space: O(n)

from sortedcontainers import SortedList
import collections


# freq table, sorted list, two pointers, sliding window

class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        def update(v, d, curr):
            if d == 1:
                sl.add((-cnt[v], -v))
            if sl.index((-cnt[v], -v)) < x:
                curr += d*cnt[v]*v
                if x < len(sl):
                    nc, nv = sl[x]
                    curr -= d*nc*nv
            if d != 1:
                sl.remove((-cnt[v], -v))
            return curr

        sl = SortedList()
        cnt = collections.defaultdict(int)
        result = []
        curr = 0
        for i, v in enumerate(nums):
            if v in cnt:
                curr = update(v, -1, curr)
            cnt[v] += 1
            curr = update(v, +1, curr)
            if i < k-1:
                continue
            result.append(curr)
            curr = update(nums[i-(k-1)], -1, curr)
            cnt[nums[i-(k-1)]] -= 1
            if cnt[nums[i-(k-1)]]:
                curr = update(nums[i-(k-1)], +1, curr)
            else:
                del cnt[nums[i-(k-1)]]
        return result