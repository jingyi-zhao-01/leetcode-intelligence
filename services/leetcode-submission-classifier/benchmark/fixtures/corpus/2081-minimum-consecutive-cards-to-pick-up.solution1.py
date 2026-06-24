# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-consecutive-cards-to-pick-up
# source_path: LeetCode-Solutions-master/Python/minimum-consecutive-cards-to-pick-up.py
# solution_class: Solution
# submission_id: d7a31268d00b642ac7d92ed7c52cb7b89e81c724
# seed: 2029098705

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        lookup = {}
        result = float("inf")
        for i, x in enumerate(cards):
            if x in lookup:
                result = min(result, i-lookup[x]+1)
            lookup[x] = i
        return result if result != float("inf") else -1