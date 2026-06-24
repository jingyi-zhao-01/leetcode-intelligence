# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: ways-to-split-array-into-three-subarrays
# source_path: LeetCode-Solutions-master/Python/ways-to-split-array-into-three-subarrays.py
# solution_class: Solution
# submission_id: 16b699785010f3e52059f773ec605be3d5a655aa
# seed: 2110254108

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7

        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1]+x)

        result = left = right = 0 
        for i in xrange(len(nums)): 
            left = max(left, i+1)
            while left+1 < len(nums) and prefix[i+1] > prefix[left+1]-prefix[i+1]:
                left += 1
            right = max(right, left)
            while right+1 < len(nums) and prefix[right+1]-prefix[i+1] <= prefix[-1]-prefix[right+1]:
                right += 1
            result = (result + (right-left))%MOD
        return result