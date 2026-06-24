# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: contains-duplicate-ii
# source_path: LeetCode-Solutions-master/Python/contains-duplicate-ii.py
# solution_class: Solution
# submission_id: 88a4d4d96604e3a38b6256a8dcba7da85cc8e766
# seed: 4289537392

# Time:  O(n)
# Space: O(n)

class Solution(object):
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        lookup = {}
        for i, num in enumerate(nums):
            if num not in lookup:
                lookup[num] = i
            else:
                # If the value occurs before, check the difference.
                if i - lookup[num] <= k:
                    return True
                # Update the index of the value.
                lookup[num] = i
        return False