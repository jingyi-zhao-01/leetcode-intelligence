# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-power-of-k-size-subarrays-i
# source_path: LeetCode-Solutions-master/Python/find-the-power-of-k-size-subarrays-i.py
# solution_class: Solution2
# submission_id: 97c67b44a79a546dffa7423da5d5b186fdf37b3e
# seed: 149567675

# Time:  O(n)
# Space: O(1)

# two pointers, sliding window

class Solution2(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [nums[i+k-1] if all(nums[j]+1 == nums[j+1] for j in xrange(i, i+k-1)) else -1 for i in xrange(len(nums)-k+1)]