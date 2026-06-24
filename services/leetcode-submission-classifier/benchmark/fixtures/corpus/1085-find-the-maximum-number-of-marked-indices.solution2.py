# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-maximum-number-of-marked-indices
# source_path: LeetCode-Solutions-master/Python/find-the-maximum-number-of-marked-indices.py
# solution_class: Solution2
# submission_id: f62071402bdcdecfa1771283a9097cca7dcd1703
# seed: 1987387921

# Time:  O(nlogn)
# Space: O(1)

# sort, greedy, two pointers

class Solution2(object):
    def maxNumOfMarkedIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left = 0
        for right in xrange(len(nums)):
            if nums[right] >= 2*nums[left]:
                left += 1
        return min(left, len(nums)//2)*2