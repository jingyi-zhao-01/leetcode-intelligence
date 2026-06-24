# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-pivot-index
# source_path: LeetCode-Solutions-master/Python/find-pivot-index.py
# solution_class: Solution
# submission_id: 30895a1c729c66e3bc3df0521b5b7d26a4c752ce
# seed: 1820642893

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == (total-left_sum-num):
                return i
            left_sum += num
        return -1