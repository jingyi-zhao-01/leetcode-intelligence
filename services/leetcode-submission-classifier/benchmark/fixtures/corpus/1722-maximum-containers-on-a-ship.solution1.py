# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-containers-on-a-ship
# source_path: LeetCode-Solutions-master/Python/maximum-containers-on-a-ship.py
# solution_class: Solution
# submission_id: 8880c17ce7f07c1d04d4c689617d0e418fcd36a1
# seed: 4031571501

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        """
        :type n: int
        :type w: int
        :type maxWeight: int
        :rtype: int
        """
        return min(maxWeight//w, n*n)