# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-all-duplicates-in-an-array
# source_path: LeetCode-Solutions-master/Python/find-all-duplicates-in-an-array.py
# solution_class: Solution
# submission_id: c827d7e55f11d39d3410dc4217527feb63b18d9a
# seed: 2544498956

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                result.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
        return result