# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-the-array-increasing
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-the-array-increasing.py
# solution_class: Solution
# submission_id: 39a20143224fe26eddf941adce4931580947fb54
# seed: 702043129

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = prev = 0
        for curr in nums:
            if prev < curr:
                prev = curr
                continue
            prev += 1
            result += prev-curr                
        return result