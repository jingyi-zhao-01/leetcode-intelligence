# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-hills-and-valleys-in-an-array
# source_path: LeetCode-Solutions-master/Python/count-hills-and-valleys-in-an-array.py
# solution_class: Solution
# submission_id: 8a740e7b7a2cfb56a1e61fad1da1434679814981
# seed: 442845086

# Time:  O(n)
# Space: O(1)

# simulation, array

class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, inc = 0, -1
        for i in xrange(len(nums)-1):
            if nums[i] < nums[i+1]:
                result += int(inc == 0)
                inc = 1
            elif nums[i] > nums[i+1]:
                result += int(inc == 1)
                inc = 0
        return result