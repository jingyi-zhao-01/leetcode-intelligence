# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: fair-candy-swap
# source_path: LeetCode-Solutions-master/Python/fair-candy-swap.py
# solution_class: Solution
# submission_id: 142f91a7c102d5ca062cc2ca7df07b93a2482971
# seed: 2653573594

# Time:  O(m + n)
# Space: O(m + n)

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        diff = (sum(A)-sum(B))//2
        setA = set(A)
        for b in set(B):
            if diff+b in setA:
                return [diff+b, b]
        return []