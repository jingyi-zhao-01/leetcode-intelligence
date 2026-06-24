# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-sum-of-weights-after-edge-removals
# source_path: LeetCode-Solutions-master/Python/maximize-sum-of-weights-after-edge-removals.py
# solution_class: Solution2
# submission_id: 2c6c72f278e64c9df101ab538968517833c0e360
# seed: 843901033

# Time:  O(n)
# Space: O(n)

import random


# iterative dfs, quick select

class Solution2(object):
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

        def dfs(u, p):
            result = 0
            diff = []
            for v, w in adj[u]:
                if v == p:
                    continue
                cnt = dfs(v, u)
                result += cnt[0]
                diff.append(max((cnt[1]+w)-cnt[0], 0))
            if k-1 < len(diff):
                nth_element(diff, k-1, lambda a, b: a > b)
            return (result+sum(diff[i] for i in xrange(min(k, len(diff)))), result+sum(diff[i] for i in xrange(min(k-1, len(diff)))))

        adj = [[] for _ in xrange(len(edges)+1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        return dfs(0, -1)[0]