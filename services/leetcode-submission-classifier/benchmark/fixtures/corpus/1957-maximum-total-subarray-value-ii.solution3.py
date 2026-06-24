# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-subarray-value-ii
# source_path: LeetCode-Solutions-master/Python/maximum-total-subarray-value-ii.py
# solution_class: Solution3
# submission_id: 3254c810071b905a948326c34ee1b8900731c220
# seed: 2074867266

# Time:  O((n + k) * logn)
# Space: O(n + k)

import heapq


# heap, sort, two pointers

class Solution3(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        class SegmentTree(object):
            def __init__(self, N, build_fn, query_fn):
                self.tree = [None]*(1<<((N-1).bit_length()+1))
                self.base = len(self.tree)>>1
                self.query_fn = query_fn
                for i in xrange(self.base, self.base+N):
                    self.tree[i] = build_fn(i-self.base)
                for i in reversed(xrange(1, self.base)):
                    self.tree[i] = query_fn(self.tree[i<<1], self.tree[(i<<1)+1])

            def query(self, L, R):
                if L > R:
                    return None
                L += self.base
                R += self.base
                left = right = None
                while L <= R:
                    if L & 1:
                        left = self.query_fn(left, self.tree[L])
                        L += 1
                    if R & 1 == 0:
                        right = self.query_fn(self.tree[R], right)
                        R -= 1
                    L >>= 1
                    R >>= 1
                return self.query_fn(left, right)

    
        st_min = SegmentTree(len(nums), build_fn=lambda x: nums[x], query_fn=lambda x, y: y if x is None else x if y is None else min(x, y))
        st_max = SegmentTree(len(nums), build_fn=lambda x: nums[x], query_fn=lambda x, y: y if x is None else x if y is None else max(x, y))
        max_heap = [(-(st_max.query(i, len(nums)-1)-st_min.query(i, len(nums)-1)), (i, len(nums)-1)) for i in xrange(len(nums))]
        heapq.heapify(max_heap)
        result = 0
        for _ in xrange(k):
            v, (i, j) = heappop(max_heap)
            result += -v
            if i <= j-1:
                heapq.heappush(max_heap, (-(st_max.query(i, j-1)-st_min.query(i, j-1)), (i, j-1)))
        return result