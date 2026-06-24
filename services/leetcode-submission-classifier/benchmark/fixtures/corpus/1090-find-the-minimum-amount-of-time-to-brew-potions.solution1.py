# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-minimum-amount-of-time-to-brew-potions
# source_path: LeetCode-Solutions-master/Python/find-the-minimum-amount-of-time-to-brew-potions.py
# solution_class: Solution
# submission_id: 0d4d1c36b48315c0478708e8e79ed2e21bc2c938
# seed: 3395459186

# Time:  O(n * m)
# Space: O(1)

# prefix sum, greedy

class Solution(object):
    def minTime(self, skill, mana):
        """
        :type skill: List[int]
        :type mana: List[int]
        :rtype: int
        """
        result = 0
        for i in xrange(1, len(mana)):
            prefix = mx = 0
            for x in skill:
                prefix += x
                mx = max(mx, mana[i-1]*prefix-mana[i]*(prefix-x))
            result += mx
        result += mana[-1]*sum(skill)
        return result