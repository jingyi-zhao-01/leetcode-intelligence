# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reveal-cards-in-increasing-order
# source_path: LeetCode-Solutions-master/Python/reveal-cards-in-increasing-order.py
# solution_class: Solution
# submission_id: a2c171a24e117a3661d0bcaba3b166e633b574b9
# seed: 2920684159

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        d = collections.deque()
        deck.sort(reverse=True)
        for i in deck:
            if d:
                d.appendleft(d.pop())
            d.appendleft(i)
        return list(d)