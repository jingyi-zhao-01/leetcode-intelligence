# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-array-equal-to-target
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-array-equal-to-target.py
# solution_class: Solution
# submission_id: c1ffa552cd7a7f7417b6415b51380edfbc449a30
# seed: 944557403

# Time:  O(n)
# Space: O(1)

# greedy, lc1526

class Solution(object):
    def minimumOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        for i in xrange(len(target)):
            target[i] -= nums[i]
        return sum(max((target[i] if i < len(target) else 0)-(target[i-1] if i-1 >= 0 else 0), 0) for i in xrange(len(target)+1))