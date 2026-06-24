# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-deletions-to-make-array-beautiful
# source_path: LeetCode-Solutions-master/Python/minimum-deletions-to-make-array-beautiful.py
# solution_class: Solution
# submission_id: 20790cc59a14ee591f43a28c649341d043d6dd45
# seed: 20956902

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def minDeletion(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in xrange(len(nums)-1):
            result += int(i%2 == result%2 and nums[i] == nums[i+1])
        return result+(len(nums)-result)%2