# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: mark-elements-on-array-by-performing-queries
# source_path: LeetCode-Solutions-master/Python/mark-elements-on-array-by-performing-queries.py
# solution_class: Solution
# submission_id: 12ec3ad9699d12842b886e992e8c19956d2aab49
# seed: 2669378150

# Time:  O(q + nlogn)
# Space: O(n)

# hash table, heap

class Solution(object):
    def unmarkedSumArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        total = sum(nums)
        lookup = [False]*len(nums)
        min_heap = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(min_heap)
        result = []
        for i, k in queries:
            if not lookup[i]:
                lookup[i] = True
                total -= nums[i]
            for _ in xrange(k):
                while min_heap:
                    x, i = heapq.heappop(min_heap)
                    if lookup[i]:
                        continue
                    lookup[i] = True
                    total -= x
                    break
                if not min_heap:
                    break
            result.append(total)
        return result