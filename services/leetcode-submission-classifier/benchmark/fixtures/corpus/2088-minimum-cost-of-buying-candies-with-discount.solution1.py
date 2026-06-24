# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-of-buying-candies-with-discount
# source_path: LeetCode-Solutions-master/Python/minimum-cost-of-buying-candies-with-discount.py
# solution_class: Solution
# submission_id: 954d2124adee116d68b93439c4bcab80096f550f
# seed: 518266577

# Time:  O(nlogn)
# Space: O(1)

# greedy

class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reverse=True)
        return sum(x for i, x in enumerate(cost) if i%3 != 2)