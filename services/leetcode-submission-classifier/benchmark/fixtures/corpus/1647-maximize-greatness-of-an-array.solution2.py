# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-greatness-of-an-array
# source_path: LeetCode-Solutions-master/Python/maximize-greatness-of-an-array.py
# solution_class: Solution2
# submission_id: be4c46b3260923b844f1570e28fdfa7ecfc34c3b
# seed: 828832582

# Time:  O(n)
# Space: O(n)

# freq table, contructive algorithms

class Solution2(object):
    def maximizeGreatness(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left = 0
        for right in xrange(len(nums)):
            if nums[right] > nums[left]:
                left += 1
        return left