# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-weighted-modes-in-subarrays
# source_path: LeetCode-Solutions-master/Python/sum-of-weighted-modes-in-subarrays.py
# solution_class: Solution2
# submission_id: 2504726bbc781dbf3709260d57ed442bcdf0c2d3
# seed: 172958017

# Time:  O(nlogk)
# Space: O(k)

import collections
from sortedcontainers import SortedList


# sorted list, two pointers, sliding window

class Solution2(object):
    def modeWeight(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = collections.defaultdict(int)
        max_heap = []
        result = 0
        for i in xrange(len(nums)):
            cnt[nums[i]] += 1
            heapq.heappush(max_heap, (-cnt[nums[i]], nums[i]))
            if i >= k-1:
                while -max_heap[0][0] != cnt[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                result += -max_heap[0][0]*max_heap[0][1]
                cnt[nums[i-k+1]] -= 1
        return result