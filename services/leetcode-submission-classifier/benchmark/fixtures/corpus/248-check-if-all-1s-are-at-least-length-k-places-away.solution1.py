# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-all-1s-are-at-least-length-k-places-away
# source_path: LeetCode-Solutions-master/Python/check-if-all-1s-are-at-least-length-k-places-away.py
# solution_class: Solution
# submission_id: d5345c4f808fc9a05ebd17a3381501f45e65b540
# seed: 3825070332

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prev = -k-1
        for i in xrange(len(nums)):
            if not nums[i]:
                continue
            if i-prev <= k:
                return False
            prev = i
        return True