# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-the-topmost-element-after-k-moves
# source_path: LeetCode-Solutions-master/Python/maximize-the-topmost-element-after-k-moves.py
# solution_class: Solution
# submission_id: ec2ea75e899bca877d2512c871aa82c9567e9fc3
# seed: 447615646

# Time:  O(min(n, k))
# Space: O(1)

# constructive algorithms

class Solution(object):
    def maximumTop(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1 == k%2:
            return -1
        if k <= 1:
            return nums[k]
        return max(nums[i] for i in xrange(min(k+1, len(nums))) if i != k-1)