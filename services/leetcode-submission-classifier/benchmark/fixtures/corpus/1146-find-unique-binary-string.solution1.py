# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-unique-binary-string
# source_path: LeetCode-Solutions-master/Python/find-unique-binary-string.py
# solution_class: Solution
# submission_id: 46e91a6a30b2044779c03a75a7ee3de39a451e9c
# seed: 616886082

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        return "".join("01"[nums[i][i] == '0'] for i in xrange(len(nums)))