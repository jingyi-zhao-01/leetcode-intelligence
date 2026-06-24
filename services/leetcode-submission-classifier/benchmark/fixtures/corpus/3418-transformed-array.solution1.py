# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: transformed-array
# source_path: LeetCode-Solutions-master/Python/transformed-array.py
# solution_class: Solution
# submission_id: 114aa2709408139ce1574ac1414d7ada81ad1ce3
# seed: 2093096920

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [nums[(i+nums[i])%len(nums)] for i in xrange(len(nums))]