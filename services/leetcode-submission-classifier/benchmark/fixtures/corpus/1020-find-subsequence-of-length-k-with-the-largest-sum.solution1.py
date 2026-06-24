# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-subsequence-of-length-k-with-the-largest-sum
# source_path: LeetCode-Solutions-master/Python/find-subsequence-of-length-k-with-the-largest-sum.py
# solution_class: Solution
# submission_id: a25b845cb603569b82d05c064de811835474e37a
# seed: 1116637832

# Time:  O(n)
# Space: O(n)

import random


# quick select solution

class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
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

        partition = nums[:]
        nth_element(partition, k-1, compare=lambda a, b: a > b)
        cnt = sum(partition[i] == partition[k-1] for i in xrange(k))
        result = []
        for x in nums:
            if x > partition[k-1]:
                result.append(x)
            elif x == partition[k-1] and cnt > 0:
                cnt -= 1
                result.append(x)
        return result