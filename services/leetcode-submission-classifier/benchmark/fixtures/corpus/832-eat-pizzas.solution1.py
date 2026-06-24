# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: eat-pizzas
# source_path: LeetCode-Solutions-master/Python/eat-pizzas.py
# solution_class: Solution
# submission_id: 958d4671054fd44e61e85994a8b42a84a3f3a91e
# seed: 3820422310

# Time:  O(nlogn)
# Space: O(1)

# sort, greedy

class Solution(object):
    def maxWeight(self, pizzas):
        """
        :type pizzas: List[int]
        :rtype: int
        """
        l = len(pizzas)//4
        pizzas.sort(reverse=True)
        return sum(pizzas[i] for i in xrange((l+1)//2))+sum(pizzas[i] for i in xrange((l+1)//2+1, ((l+1)//2+1)+(l//2)*2, 2))