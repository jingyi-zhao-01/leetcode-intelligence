# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: mean-of-array-after-removing-some-elements
# source_path: LeetCode-Solutions-master/Python/mean-of-array-after-removing-some-elements.py
# solution_class: Solution
# submission_id: fda58224339704eb8fad22cfe13d2dbac38a5260
# seed: 4002731808

# Time:  O(n) on average, using Median of Medians could achieve O(n) (Intro Select)
# Space: O(1)

import random

class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        P = 20
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
        
        k = len(arr)//P
        nth_element(arr, k-1)
        nth_element(arr, len(arr)-k, left=k)
        return float(sum(arr[i] for i in xrange(k, len(arr)-k)))/(len(arr)-2*k)