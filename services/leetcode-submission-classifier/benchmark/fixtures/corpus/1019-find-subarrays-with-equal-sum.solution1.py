# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-subarrays-with-equal-sum
# source_path: LeetCode-Solutions-master/Python/find-subarrays-with-equal-sum.py
# solution_class: Solution
# submission_id: aa1ef06851b74de084d896eaf7cdd8baed0fc819
# seed: 3501415346

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lookup = set()
        for i in xrange(len(nums)-1):
            if nums[i]+nums[i+1] in lookup:
                return True
            lookup.add(nums[i]+nums[i+1])
        return False