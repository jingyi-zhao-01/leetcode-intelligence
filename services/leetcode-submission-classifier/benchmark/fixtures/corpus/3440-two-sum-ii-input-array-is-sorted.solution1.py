# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: two-sum-ii-input-array-is-sorted
# source_path: LeetCode-Solutions-master/Python/two-sum-ii-input-array-is-sorted.py
# solution_class: Solution
# submission_id: 3f1eb83904597b9ac0a4abdaddad6f86449c1054
# seed: 1817514154

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def twoSum(self, nums, target):
        start, end = 0, len(nums) - 1

        while start != end:
            sum = nums[start] + nums[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return [start + 1, end + 1]