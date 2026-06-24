# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-centered-subarrays
# source_path: LeetCode-Solutions-master/Python/number-of-centered-subarrays.py
# solution_class: Solution
# submission_id: e2f73eec61a5bbf97daa391466e738e4f6e99e8e
# seed: 1290094345

# Time:  O(n^2)
# Space: O(n)

# hash table

class Solution(object):
    def centeredSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in xrange(len(nums)):
            lookup = set()
            total = 0
            for j in xrange(i, len(nums)):
                lookup.add(nums[j])
                total += nums[j]
                if total in lookup:
                    result += 1
        return result