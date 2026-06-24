# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-increasing-subsequence
# source_path: LeetCode-Solutions-master/Python/longest-increasing-subsequence.py
# solution_class: Solution2
# submission_id: f34020ee3d77e9d025a2bdc877395d98f3e33a75
# seed: 1627257154

# Time:  O(nlogn)
# Space: O(n)

import bisect

class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = []
        def insert(target):
            left, right = 0, len(LIS) - 1
            # Find the first index "left" which satisfies LIS[left] >= target
            while left <= right:
                mid = left + (right - left) // 2
                if LIS[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            # If not found, append the target.
            if left == len(LIS):
                LIS.append(target)
            else:
                LIS[left] = target

        for num in nums:
            insert(num)

        return len(LIS)