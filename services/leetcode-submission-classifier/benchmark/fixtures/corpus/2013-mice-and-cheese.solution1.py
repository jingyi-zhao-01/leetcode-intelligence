# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: mice-and-cheese
# source_path: LeetCode-Solutions-master/Python/mice-and-cheese.py
# solution_class: Solution
# submission_id: 3a08a8ab57a3aa9daf2086255fc1b375633c784d
# seed: 3610640610

# Time:  O(n)
# Space: O(1)

import random


# greedy, quick select

class Solution(object):
    def miceAndCheese(self, reward1, reward2, k):
        """
        :type reward1: List[int]
        :type reward2: List[int]
        :type k: int
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
    
        for i in xrange(len(reward1)):
            reward1[i] -= reward2[i]
        nth_element(reward1, k-1, compare=lambda a, b: a > b)
        return sum(reward2)+sum(reward1[i] for i in xrange(k))