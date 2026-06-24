# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-distance-to-the-target-element
# source_path: LeetCode-Solutions-master/Python/minimum-distance-to-the-target-element.py
# solution_class: Solution
# submission_id: 4ec319f7a275682d876b84288dc74573ac0fd987
# seed: 110759245

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        for i in xrange(len(nums)):
            if (start-i >= 0 and nums[start-i] == target) or \
               (start+i < len(nums) and nums[start+i] == target):
                break
        return i