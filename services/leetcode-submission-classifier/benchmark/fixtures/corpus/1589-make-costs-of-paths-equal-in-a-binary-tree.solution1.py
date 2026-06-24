# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-costs-of-paths-equal-in-a-binary-tree
# source_path: LeetCode-Solutions-master/Python/make-costs-of-paths-equal-in-a-binary-tree.py
# solution_class: Solution
# submission_id: 5e92b4be7c1126d129e9b33dabf19f650e675c29
# seed: 1667851238

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def minIncrements(self, n, cost):
        """
        :type n: int
        :type cost: List[int]
        :rtype: int
        """
        result = 0
        for i in reversed(xrange(n//2)):
            result += abs(cost[2*i+1]-cost[2*i+2])
            cost[i] += max(cost[2*i+1], cost[2*i+2])
        return result