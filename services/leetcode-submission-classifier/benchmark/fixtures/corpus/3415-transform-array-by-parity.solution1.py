# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: transform-array-by-parity
# source_path: LeetCode-Solutions-master/Python/transform-array-by-parity.py
# solution_class: Solution
# submission_id: 72d7ea98a0f13cf7a1833f8077d11fe57edcf8c4
# seed: 1907612393

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt = 0
        for x in nums:
            if x%2:
                continue
            nums[cnt] = 0
            cnt += 1
        for i in xrange(cnt, len(nums)):
            nums[i] = 1
        return nums