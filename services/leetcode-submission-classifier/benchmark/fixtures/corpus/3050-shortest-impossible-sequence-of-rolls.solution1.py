# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-impossible-sequence-of-rolls
# source_path: LeetCode-Solutions-master/Python/shortest-impossible-sequence-of-rolls.py
# solution_class: Solution
# submission_id: d6dc3313b321713de3a27267a870ca5beb73991e
# seed: 3917870212

# Time:  O(n)
# Space: O(k)

# constructive algorithms

class Solution(object):
    def shortestSequence(self, rolls, k):
        """
        :type rolls: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        lookup = set()
        for x in rolls:
            lookup.add(x)
            if len(lookup) != k:
                continue
            lookup.clear()
            l += 1
        return l+1