# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-consecutive-subarrays
# source_path: LeetCode-Solutions-master/Python/sum-of-consecutive-subarrays.py
# solution_class: Solution
# submission_id: 175cebeea83de3d6df71f8b3d9c7dc69022b83e7
# seed: 3159850198

# Time:  O(n)
# Space: O(1)

# combinatorics

class Solution(object):
    def getSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        def count(d):
            result = total = l = 0
            for i in xrange(len(nums)):
                l += 1
                total = (total+nums[i]*l)%MOD
                result = (result+total)%MOD
                if i+1 < len(nums) and nums[i+1]-nums[i] == d:
                    continue
                total = l = 0
            return result
    
        return (count(1)+count(-1)-reduce(lambda accu, x: (accu+x)%MOD, nums, 0))%MOD