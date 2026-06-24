# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: bitwise-or-of-adjacent-elements
# source_path: LeetCode-Solutions-master/Python/bitwise-or-of-adjacent-elements.py
# solution_class: Solution
# submission_id: fc2ee0c85ea44c237043881219104fe0067bb0fb
# seed: 2928641337

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def orArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [nums[i]|nums[i+1] for i in range(len(nums)-1)]