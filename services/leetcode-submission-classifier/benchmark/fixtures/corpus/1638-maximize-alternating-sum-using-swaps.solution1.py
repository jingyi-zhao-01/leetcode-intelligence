# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-alternating-sum-using-swaps
# source_path: LeetCode-Solutions-master/Python/maximize-alternating-sum-using-swaps.py
# solution_class: Solution
# submission_id: e39de0349b87a38f3de8100bce5076f2ed490e29
# seed: 2302378953

# Time:  O(n + s)
# Space: O(n + s)

import random


# bfs, flood fill, quick select

class Solution(object):
    def maxAlternatingSum(self, nums, swaps):
        """
        :type nums: List[int]
        :type swaps: List[List[int]]
        :rtype: int
        """
        def nth_element(nums, n, compare=lambda a, b: a < b):
            def tri_partition(nums, left, right, target, compare):
                mid = left
                while mid <= right:
                    if nums[mid] == target:
                        mid += 1
                    elif compare(nums[mid], target):
                        nums[left], nums[mid] = nums[mid], nums[left]
                        left += 1
                        mid += 1
                    else:
                        nums[mid], nums[right] = nums[right], nums[mid]
                        right -= 1
                return left, right

            left, right = 0, len(nums)-1
            while left <= right:
                pivot_idx = random.randint(left, right)
                pivot_left, pivot_right = tri_partition(nums, left, right, nums[pivot_idx], compare)
                if pivot_left <= n <= pivot_right:
                    return
                elif pivot_left > n:
                    right = pivot_left-1
                else:  # pivot_right < n.
                    left = pivot_right+1

        def bfs(u):
            q = []
            if lookup[u]:
                return q
            lookup[u] = True
            q.append(u)
            for u in q:
                for v in adj[u]:
                    if lookup[v]:
                        continue
                    lookup[v] = True
                    q.append(v)
            return q
    
        adj = [[] for _ in xrange(len(nums))]
        for i, j in swaps:
            adj[i].append(j)
            adj[j].append(i)
        lookup = [False]*len(adj)
        result = sum(nums)
        for u in xrange(len(nums)):
            g = bfs(u)
            if not g:
                continue
            l = sum(i%2 for i in g)
            arr = [nums[i] for i in g]
            nth_element(arr, l)
            result -= 2*sum(arr[i] for i in xrange(l))
        return result