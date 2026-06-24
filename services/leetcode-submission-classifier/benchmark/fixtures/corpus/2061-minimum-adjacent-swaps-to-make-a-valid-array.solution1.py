# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-adjacent-swaps-to-make-a-valid-array
# source_path: LeetCode-Solutions-master/Python/minimum-adjacent-swaps-to-make-a-valid-array.py
# solution_class: Solution
# submission_id: a8eb8fd84e57ba78d8f2c94ff75ddeb87b3e0f8f
# seed: 4221497186

# Time:  O(n)
# Space: O(1)

# array, greedy

class Solution(object):
    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_idx = min(xrange(len(nums)), key=nums.__getitem__)
        max_idx = max(reversed(xrange(len(nums))), key=nums.__getitem__)
        return ((len(nums)-1)-max_idx)+min_idx-int(max_idx < min_idx)