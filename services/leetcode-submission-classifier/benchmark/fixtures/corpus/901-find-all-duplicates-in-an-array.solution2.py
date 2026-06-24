# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-all-duplicates-in-an-array
# source_path: LeetCode-Solutions-master/Python/find-all-duplicates-in-an-array.py
# solution_class: Solution2
# submission_id: 90d0745693b10e4144eb2e091de9df89f919fe17
# seed: 605455578

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i += 1

        for i in xrange(len(nums)):
            if i != nums[i]-1:
                result.append(nums[i])
        return result