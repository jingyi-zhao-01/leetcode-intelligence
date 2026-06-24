# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-collect-elements
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-collect-elements.py
# solution_class: Solution
# submission_id: bf2a16c6d72c37e3334238ba6cc2ca8560c14c02
# seed: 1060235234

# Time:  O(n)
# Space: O(k)

# hash table

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lookup = [False]*k
        for i in reversed(xrange(len(nums))):
            if nums[i] > len(lookup) or lookup[nums[i]-1]:
                continue
            lookup[nums[i]-1] = True
            k -= 1
            if not k:
                break
        return len(nums)-i