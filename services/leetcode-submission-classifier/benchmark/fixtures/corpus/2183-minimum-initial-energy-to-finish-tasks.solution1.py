# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-initial-energy-to-finish-tasks
# source_path: LeetCode-Solutions-master/Python/minimum-initial-energy-to-finish-tasks.py
# solution_class: Solution
# submission_id: 28995697c9276479eab8531bd1e19232b54ed70c
# seed: 3134588396

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks.sort(key=lambda x: x[1]-x[0])  # sort by waste in asc
        result = 0
        # you can see proof here, https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/discuss/944633/Explanation-on-why-sort-by-difference
        for a, m in tasks:  # we need to pick all the wastes, so greedily to pick the least waste first is always better
            result = max(result+a, m)
        return result