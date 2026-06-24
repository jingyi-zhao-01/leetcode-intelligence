# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: adjacent-increasing-subarrays-detection-ii
# source_path: LeetCode-Solutions-master/Python/adjacent-increasing-subarrays-detection-ii.py
# solution_class: Solution
# submission_id: abe6a4fe049e759b40308ad1938ba11ebbfd3831
# seed: 1898016188

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        curr, prev = 1, 0
        for i in xrange(len(nums)-1):
            if nums[i] < nums[i+1]:
                curr += 1
            else:
                prev = curr
                curr = 1
            result = max(result, curr//2, min(prev, curr))
        return result