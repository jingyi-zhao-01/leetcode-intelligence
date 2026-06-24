# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-increments-on-subarrays-to-form-a-target-array
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-increments-on-subarrays-to-form-a-target-array.py
# solution_class: Solution
# submission_id: a5566a175e09957f6faa0e75ac3b8f0856eccbb4
# seed: 2108631429

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        return sum(max((target[i] if i < len(target) else 0)-(target[i-1] if i-1 >= 0 else 0), 0) for i in xrange(len(target)+1))