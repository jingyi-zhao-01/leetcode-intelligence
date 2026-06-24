# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-k-subarray-sums-equal
# source_path: LeetCode-Solutions-master/Python/make-k-subarray-sums-equal.py
# solution_class: Solution
# submission_id: 06e7f193e39e726891b50e5809a2c19acf04c397
# seed: 2103979885

# Time:  O(n)
# Space: O(n)

import random


# math, greedy, quick select

class Solution(object):
    def makeSubKSumEqual(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

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

        l = gcd(k, len(arr))
        result = 0
        for i in xrange(l):
            vals = [arr[j] for j in xrange(i, len(arr), l)]
            nth_element(vals, len(vals)//2)
            result += sum(abs(v-vals[len(vals)//2]) for v in vals)
        return result