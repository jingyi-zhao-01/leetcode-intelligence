# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: adjacent-increasing-subarrays-detection-i
# source_path: LeetCode-Solutions-master/Python/adjacent-increasing-subarrays-detection-i.py
# solution_class: Solution
# submission_id: 4ba8fcb0adadd087de71f677bdfbc124d45aa2b7
# seed: 1738254682

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
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
        return result >= k