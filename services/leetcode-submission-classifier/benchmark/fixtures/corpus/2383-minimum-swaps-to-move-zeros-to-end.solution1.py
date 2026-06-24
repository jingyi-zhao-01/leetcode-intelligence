# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-swaps-to-move-zeros-to-end
# source_path: LeetCode-Solutions-master/Python/minimum-swaps-to-move-zeros-to-end.py
# solution_class: Solution
# submission_id: 9b8d2150cb645fa8264fa4fa1b9c875d157119ac
# seed: 3405291506

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums[i] != 0 for i in xrange(len(nums)-nums.count(0), len(nums)))