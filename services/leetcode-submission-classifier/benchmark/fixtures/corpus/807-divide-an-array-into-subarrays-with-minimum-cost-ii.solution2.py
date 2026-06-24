# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divide-an-array-into-subarrays-with-minimum-cost-ii
# source_path: LeetCode-Solutions-master/Python/divide-an-array-into-subarrays-with-minimum-cost-ii.py
# solution_class: Solution2
# submission_id: c9b81d0a11f69cecd0bd24f74140b3c0e2f55e32
# seed: 2089767039

# Time:  O(nlogd)
# Space: O(d)

import heapq


# sliding window, heap

class Solution2(object):
    def minimumCost(self, nums, k, dist):
        """
        :type nums: List[int]
        :type k: int
        :type dist: int
        :rtype: int
        """
        def get_top(heap, cnt, total):
            while heap[0] in cnt:
                x = heapq.heappop(heap)
                cnt[x] -= 1
                if cnt[x] == 0:
                    del cnt[x]
                total[0] -= 1
            return heap[0]

        def lazy_delete(heap, cnt, total, x):
            cnt[x] += 1
            total[0] += 1
            if total[0] <= len(heap)-total[0]:
                return
            new_heap = []
            for x in heap:
                if x not in cnt:
                    new_heap.append(x)
                    continue
                cnt[x] -= 1
                if cnt[x] == 0:
                    del cnt[x]
            total[0] = 0
            heapq.heapify(new_heap)
            heap[:] = new_heap

        max_heap, min_heap = [], []
        cnt1, cnt2 = collections.Counter(), collections.Counter()
        total1, total2 = [0], [0]
        mn, curr = float("inf"), 0
        for i in xrange(1, len(nums)):
            heapq.heappush(max_heap, -nums[i])
            curr += nums[i]
            if (len(max_heap)-total1[0]) > k-1:
                x = get_top(max_heap, cnt1, total1)
                curr -= -x
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            if (len(max_heap)-total1[0])+(len(min_heap)-total2[0]) > 1+dist:
                x = get_top(min_heap, cnt2, total2)
                if x <= nums[i-(1+dist)]:
                    lazy_delete(min_heap, cnt2, total2, nums[i-(1+dist)])
                else:
                    lazy_delete(max_heap, cnt1, total1, -nums[i-(1+dist)])
                    heapq.heappop(min_heap)
                    curr -= nums[i-(1+dist)]-x
                    heapq.heappush(max_heap, -x)
            if len(max_heap)-total1[0] == k-1:
                mn = min(mn, curr)
        return nums[0]+mn