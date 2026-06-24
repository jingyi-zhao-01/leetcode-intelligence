# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: partition-array-such-that-maximum-difference-is-k
# source_path: LeetCode-Solutions-master/Python/partition-array-such-that-maximum-difference-is-k.py
# solution_class: Solution
# submission_id: 8c13053df8f68d046c23cfd80dde616dcfb5ba89
# seed: 396904887

# Time:  O(nlogn)
# Space: O(1)

# sort, greedy

class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        result, prev = 1, 0
        for i in xrange(len(nums)):
            if nums[i]-nums[prev] <= k:
                continue
            prev = i
            result += 1
        return result