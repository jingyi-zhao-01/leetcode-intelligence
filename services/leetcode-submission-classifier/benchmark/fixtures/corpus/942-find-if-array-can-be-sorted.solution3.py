# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-if-array-can-be-sorted
# source_path: LeetCode-Solutions-master/Python/find-if-array-can-be-sorted.py
# solution_class: Solution3
# submission_id: 63029c5c059ceaafc6600e5ddd29024a36426f15
# seed: 897145915

# Time:  O(n)
# Space: O(1)

# sort

class Solution3(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def popcount(x):
            return bin(x).count("1")
    
        left = 0
        for right in xrange(len(nums)):
            if right+1 != len(nums) and popcount(nums[right+1]) == popcount(nums[right]):
                continue
            nums[left:right+1] = sorted(nums[left:right+1])
            left = right+1
        return all(nums[i] <= nums[i+1] for i in xrange(len(nums)-1))