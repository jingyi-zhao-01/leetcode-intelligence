# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: replace-elements-in-an-array
# source_path: LeetCode-Solutions-master/Python/replace-elements-in-an-array.py
# solution_class: Solution2
# submission_id: 65d2c7f94578bc25f547474f92ae3dcf3ba52148
# seed: 3929393275

# Time:  O(n + m)
# Space: O(n)

# hash table, optimized from solution2

class Solution2(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        lookup = {x:i for i, x in enumerate(nums)}
        for x, y in operations:
            nums[lookup[x]] = y
            lookup[y] = lookup.pop(x)
        return nums