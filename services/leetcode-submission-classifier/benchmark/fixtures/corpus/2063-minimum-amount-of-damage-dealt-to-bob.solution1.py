# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-amount-of-damage-dealt-to-bob
# source_path: LeetCode-Solutions-master/Python/minimum-amount-of-damage-dealt-to-bob.py
# solution_class: Solution
# submission_id: 24a1bd3d0c3a6ecb658e5b6439cde93bdf428a79
# seed: 1120409626

# Time:  O(nlogn)
# Space: O(n)

# sort, greedy

class Solution(object):
    def minDamage(self, power, damage, health):
        """
        :type power: int
        :type damage: List[int]
        :type health: List[int]
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b
        
        idxs = range(len(health))
        idxs.sort(key=lambda i: float(ceil_divide(health[i], power))/damage[i])
        result = t = 0
        for i in idxs:
            t += ceil_divide(health[i], power)
            result += t*damage[i]
        return result