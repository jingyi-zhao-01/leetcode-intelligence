# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-maximum-length-of-valid-subsequence-i
# source_path: LeetCode-Solutions-master/Python/find-the-maximum-length-of-valid-subsequence-i.py
# solution_class: Solution2
# submission_id: 905860f946ea615980d5ef12991caf0e09f237c6
# seed: 2296509918

# Time:  O(n)
# Space: O(1)

# dp

class Solution2(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return max(sum(x%2 == 0 for x in nums),
                   sum(x%2 == 1 for x in nums),
                   sum(nums[i]%2 != nums[i+1]%2 for i in xrange(len(nums)-1))+1)