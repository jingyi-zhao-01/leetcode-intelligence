# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-duplicate-number
# source_path: LeetCode-Solutions-master/Python/find-the-duplicate-number.py
# solution_class: Solution3
# submission_id: 8b31926da1c9e287057fb2715287babc58fb9ea4
# seed: 4065383609

# Time:  O(n)
# Space: O(1)

class Solution3(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicate = 0
        # Mark the value as visited by negative.
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
            else:
                duplicate = abs(num)
                break
        # Rollback the value.
        for num in nums:
            if nums[abs(num) - 1] < 0:
                nums[abs(num) - 1] *= -1
            else:
                break
        return duplicate