# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: contains-duplicate
# source_path: LeetCode-Solutions-master/Python/contains-duplicate.py
# solution_class: Solution
# submission_id: a274b95c9aebe030ac539780f8dec86e7153b8c0
# seed: 1686767870

# Time:  O(n)
# Space: O(n)

class Solution(object):
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))