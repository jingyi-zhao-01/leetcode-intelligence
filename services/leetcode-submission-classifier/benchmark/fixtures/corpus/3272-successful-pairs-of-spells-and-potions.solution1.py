# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: successful-pairs-of-spells-and-potions
# source_path: LeetCode-Solutions-master/Python/successful-pairs-of-spells-and-potions.py
# solution_class: Solution
# submission_id: 9553a0fa863d77ff4b69e4ba0f95cfeb24442a0a
# seed: 784505658

# Time:  O(mlogm + nlogm)
# Space: O(1)

# binary search

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        def ceil_divide(a, b):
            return (a+(b-1))//b
            
        potions.sort()
        return [len(potions)-bisect.bisect_left(potions, ceil_divide(success, s)) for s in spells]