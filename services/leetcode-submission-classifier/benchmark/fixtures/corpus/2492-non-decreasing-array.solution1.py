# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: non-decreasing-array
# source_path: LeetCode-Solutions-master/Python/non-decreasing-array.py
# solution_class: Solution
# submission_id: 4033d0220d552c1e249d09e22d56d4f84389fc40
# seed: 3603588528

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        modified, prev = False, nums[0]
        for i in xrange(1, len(nums)):
            if prev > nums[i]:
                if modified:
                    return False
                if i-2 < 0 or nums[i-2] <= nums[i]:
                    prev = nums[i]    # nums[i-1] = nums[i], prev = nums[i]
#               else:
#                   prev = nums[i-1]  # nums[i] = nums[i-1], prev = nums[i]
                modified = True
            else:
                prev = nums[i]
        return True