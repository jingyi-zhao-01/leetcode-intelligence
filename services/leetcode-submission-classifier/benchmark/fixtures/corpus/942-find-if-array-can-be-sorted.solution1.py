# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-if-array-can-be-sorted
# source_path: LeetCode-Solutions-master/Python/find-if-array-can-be-sorted.py
# solution_class: Solution
# submission_id: 5fd92d8f34babb096c8fa4e4c4bbfda08ee4eb7d
# seed: 1041587185

# Time:  O(n)
# Space: O(1)

# sort

class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def popcount(x):
            return bin(x).count("1")
    
        left = mx = 0
        for right in xrange(len(nums)):
            if right+1 != len(nums) and popcount(nums[right+1]) == popcount(nums[right]):
                continue
            if mx > min(nums[i] for i in xrange(left, right+1)):
                return False
            mx = max(nums[i] for i in xrange(left, right+1))
            left = right+1
        return True