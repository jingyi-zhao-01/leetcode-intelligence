# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: removing-minimum-and-maximum-from-array
# source_path: LeetCode-Solutions-master/Python/removing-minimum-and-maximum-from-array.py
# solution_class: Solution
# submission_id: 933d89a5b54fb5f750236550f273723b46807092
# seed: 2838492983

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = nums.index(min(nums)), nums.index(max(nums))
        if i > j:
            i, j = j, i
        return min((i+1)+(len(nums)-j), j+1, len(nums)-i)