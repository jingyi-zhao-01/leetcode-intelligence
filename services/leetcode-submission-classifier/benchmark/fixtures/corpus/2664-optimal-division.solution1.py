# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: optimal-division
# source_path: LeetCode-Solutions-master/Python/optimal-division.py
# solution_class: Solution
# submission_id: ae1c5ad8010d365029be1475585b32d530a26798
# seed: 3128385715

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        result = [str(nums[0]) + "/(" + str(nums[1])]
        for i in xrange(2, len(nums)):
            result += "/" + str(nums[i])
        result += ")"
        return "".join(result)