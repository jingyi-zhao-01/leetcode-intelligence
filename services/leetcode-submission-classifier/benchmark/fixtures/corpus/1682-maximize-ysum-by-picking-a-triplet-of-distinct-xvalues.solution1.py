# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-ysum-by-picking-a-triplet-of-distinct-xvalues
# source_path: LeetCode-Solutions-master/Python/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues.py
# solution_class: Solution
# submission_id: a3f0237c77d6a5f37b1b9cdd9a5a562dbe127e10
# seed: 1834264956

# Time:  O(n)
# Space: O(n)

import collections
import itertools
import random


# hash table, quick select

class Solution(object):
    def maxSumDistinctTriplet(self, x, y):
        """
        :type x: List[int]
        :type y: List[int]
        :rtype: int
        """
        def nth_element(nums, n, left=0, compare=lambda a, b: a < b):
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
            
            right = len(nums)-1
            while left <= right:
                pivot_idx = random.randint(left, right)
                pivot_left, pivot_right = tri_partition(nums, left, right, nums[pivot_idx], compare)
                if pivot_left <= n <= pivot_right:
                    return
                elif pivot_left > n:
                    right = pivot_left-1
                else:  # pivot_right < n.
                    left = pivot_right+1

        K = 3
        lookup = collections.defaultdict(int)
        for i, j in itertools.izip(x, y):
            lookup[i] = max(lookup[i], j)
        if len(lookup) < K:
            return -1
        vals = lookup.values()
        nth_element(vals, K-1, compare=lambda x, y: x > y)
        return sum(vals[i] for i in xrange(K))