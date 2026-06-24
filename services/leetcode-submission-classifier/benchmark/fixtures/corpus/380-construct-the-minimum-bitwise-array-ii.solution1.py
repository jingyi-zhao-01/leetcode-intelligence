# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: construct-the-minimum-bitwise-array-ii
# source_path: LeetCode-Solutions-master/Python/construct-the-minimum-bitwise-array-ii.py
# solution_class: Solution
# submission_id: 92bbcb1ec6d092a06bd2174fdd94a61889abba36
# seed: 3084588417

# Time:  O(n)
# Space: O(1)

# bit manipulation

class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [x-(((x+1)&~x)>>1) if x&1 else -1 for x in nums]