# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: construct-the-minimum-bitwise-array-i
# source_path: LeetCode-Solutions-master/Python/construct-the-minimum-bitwise-array-i.py
# solution_class: Solution2
# submission_id: d784f6e58bef532e096f2bfe2d8efb72021e1677
# seed: 808521645

# Time:  O(n)
# Space: O(1)

# bit manipulation

class Solution2(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [next((i for i in xrange(x) if i|(i+1) == x), -1) for x in nums]