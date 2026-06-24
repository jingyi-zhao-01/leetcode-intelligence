# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: distribute-elements-into-two-arrays-i
# source_path: LeetCode-Solutions-master/Python/distribute-elements-into-two-arrays-i.py
# solution_class: Solution
# submission_id: 7d10b9e33e6fb81e9d744951a12044ae73c0b9fb
# seed: 82567622

# Time:  O(n)
# Space: O(n)

# array

class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a, b = [nums[0]], [nums[1]]
        for i in xrange(2, len(nums)):
            if a[-1] > b[-1]:
                a.append(nums[i])
            else:
                b.append(nums[i])
        return a+b