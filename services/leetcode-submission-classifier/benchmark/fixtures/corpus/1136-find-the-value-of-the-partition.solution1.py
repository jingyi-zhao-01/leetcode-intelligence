# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-value-of-the-partition
# source_path: LeetCode-Solutions-master/Python/find-the-value-of-the-partition.py
# solution_class: Solution
# submission_id: 023e8edcf976ee94398890292cfa7ffe7fa07c0c
# seed: 1862397317

# Time:  O(nlogn)
# Space: O(1)

# sort

class Solution(object):
    def findValueOfPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return min(nums[i+1]-nums[i] for i in xrange(len(nums)-1))