# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-middle-index-in-array
# source_path: LeetCode-Solutions-master/Python/find-the-middle-index-in-array.py
# solution_class: Solution
# submission_id: 465474c9eb49ffb26787bf4ed2da091794042841
# seed: 1300342196

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        accu = 0
        for i, x in enumerate(nums):
            if accu*2 == total-x:
                return i
            accu += x
        return -1