# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-limit-of-balls-in-a-bag
# source_path: LeetCode-Solutions-master/Python/minimum-limit-of-balls-in-a-bag.py
# solution_class: Solution
# submission_id: 94380c2a474a5d92fbd6451293641cc44644550f
# seed: 2026450046

# Time:  O(nlogm), m is the max of nums
# Space: O(1)

class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        def check(nums, maxOperations, x):
            return sum((num+x-1)//x-1 for num in nums) <= maxOperations
    
        left, right = 1, max(nums)
        while left <= right:
            mid = left + (right-left)//2
            if check(nums, maxOperations, mid):
                right = mid-1
            else:
                left = mid+1
        return left