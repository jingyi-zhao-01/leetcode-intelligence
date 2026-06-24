# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-reach-target-array
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-reach-target-array.py
# solution_class: Solution
# submission_id: 89e5f0613f592ad139e795dfb6f65a46773c01ce
# seed: 3977811732

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def minOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        return len(set(nums[i]for i in xrange(len(nums)) if nums[i] != target[i]))