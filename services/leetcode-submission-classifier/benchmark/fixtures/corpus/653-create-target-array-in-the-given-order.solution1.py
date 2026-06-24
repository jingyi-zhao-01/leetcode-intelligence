# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: create-target-array-in-the-given-order
# source_path: LeetCode-Solutions-master/Python/create-target-array-in-the-given-order.py
# solution_class: Solution
# submission_id: 5afce02ebe5c444bdda7d0bf8ffc7ebf3bc28f82
# seed: 728966799

# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            for j in xrange(i):
                if index[j] >= index[i]:
                    index[j] += 1
        result = [0]*(len(nums))
        for i in xrange(len(nums)):
            result[index[i]] = nums[i]
        return result