# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-subarray-value-ii
# source_path: LeetCode-Solutions-master/Python/maximum-total-subarray-value-ii.py
# solution_class: Solution
# submission_id: 13fd163dff1ebc3a81da8ada74747ab04b95ca91
# seed: 1098765008

# Time:  O((n + k) * logn)
# Space: O(n + k)

import heapq


# heap, sort, two pointers

class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def nxt(left, right, i, j):
            while not (left <= idxs[i] <= right):
                i += 1
            while not (left <= idxs[j] <= right):
                j -= 1
            return (i, j)
            
        idxs = range(len(nums))
        idxs.sort(key=lambda x: (nums[x], x))
        lookup = {(0, len(nums)-1):(0, len(idxs)-1)}
        max_heap = [(-(nums[idxs[len(idxs)-1]]-nums[idxs[0]]), (0, len(idxs)-1))]
        result = 0
        while k:
            v, (l, r) = heapq.heappop(max_heap)
            i, j = lookup[(l, r)]
            nl, nr = min(idxs[i], idxs[j]), max(idxs[i], idxs[j])
            c = min((nl-l+1)*(r-nr+1), k)
            k -= c
            result += c*(-v)
            if nl+1 <= r and (nl+1, r) not in lookup:
                lookup[(nl+1, r)] = (ni, nj) = nxt(nl+1, r, i, j)
                heapq.heappush(max_heap, (-(nums[idxs[nj]]-nums[idxs[ni]]), (nl+1, r)))
            if l <= nr-1 and (l, nr-1) not in lookup:
                lookup[(l, nr-1)] = (ni, nj) = nxt(l, nr-1, i, j)
                heapq.heappush(max_heap, (-(nums[idxs[nj]]-nums[idxs[ni]]), (l, nr-1)))
        return result