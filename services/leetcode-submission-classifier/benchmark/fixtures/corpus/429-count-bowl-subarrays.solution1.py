# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-bowl-subarrays
# source_path: LeetCode-Solutions-master/Python/count-bowl-subarrays.py
# solution_class: Solution
# submission_id: 4da205654c7bf85905c944a529491247baa99584
# seed: 3854087058

# Time:  O(n)
# Space: O(n)

# mono stack

class Solution(object):
    def bowlSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        stk = []
        for i in xrange(len(nums)):
            while stk and nums[stk[-1]] < nums[i]:
                stk.pop()
                if stk:
                    result += 1
            stk.append(i)
        return result