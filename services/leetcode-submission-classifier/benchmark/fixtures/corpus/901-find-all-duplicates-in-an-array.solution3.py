# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-all-duplicates-in-an-array
# source_path: LeetCode-Solutions-master/Python/find-all-duplicates-in-an-array.py
# solution_class: Solution3
# submission_id: f2b8f0fbbd89de99c5b90373448c72db01596170
# seed: 2249192110

# Time:  O(n)
# Space: O(1)

class Solution3(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [elem for elem, count in Counter(nums).items() if count == 2]