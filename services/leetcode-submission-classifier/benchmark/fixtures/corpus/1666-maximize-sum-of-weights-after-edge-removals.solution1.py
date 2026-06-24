# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-sum-of-weights-after-edge-removals
# source_path: LeetCode-Solutions-master/Python/maximize-sum-of-weights-after-edge-removals.py
# solution_class: Solution
# submission_id: 9f39568482039f96396e00ca563499e9c920ee6d
# seed: 3079097026

# Time:  O(n)
# Space: O(n)

import random


# iterative dfs, quick select

class Solution(object):
    def maximizeSumOfWeights(self, edges, k):
        """
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        def nth_element(nums, n, compare=lambda a, b: a < b):
            def tri_partition(nums, left, right, target):
                i = left
                while i <= right:
                    if compare(nums[i], target):
                        nums[i], nums[left] = nums[left], nums[i]
                        left += 1
                        i += 1
                    elif compare(target, nums[i]):
                        nums[i], nums[right] = nums[right], nums[i]
                        right -= 1
                    else:
                        i += 1
                return left, right

            left, right = 0, len(nums)-1
            while left <= right:
                pivot_idx = random.randint(left, right)
                pivot_left, pivot_right = tri_partition(nums, left, right, nums[pivot_idx])
                if pivot_left <= n <= pivot_right:
                    return
                elif pivot_left > n:
                    right = pivot_left-1
                else:  # pivot_right < n.
                    left = pivot_right+1

        def iter_dfs():
            cnt = [[0]*2 for _ in xrange(len(adj))]
            stk = [(1, 0, -1)]
            while stk:
                step, u, p = stk.pop()
                if step == 1:
                    stk.append((2, u, p))
                    for v, w in reversed(adj[u]):
                        if v == p:
                            continue
                        stk.append((1, v, u))
                elif step == 2:
                    curr = 0
                    diff = []
                    for v, w in adj[u]:
                        if v == p:
                            continue
                        curr += cnt[v][0]
                        diff.append(max((cnt[v][1]+w)-cnt[v][0], 0))
                    if k-1 < len(diff):
                        nth_element(diff, k-1, lambda a, b: a > b)
                    cnt[u][0] = curr+sum(diff[i] for i in xrange(min(k, len(diff))))
                    cnt[u][1] = curr+sum(diff[i] for i in xrange(min(k-1, len(diff))))
            return cnt[0][0]
    
        adj = [[] for _ in xrange(len(edges)+1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        return iter_dfs()