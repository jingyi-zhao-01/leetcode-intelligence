# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: last-stone-weight-ii
# source_path: LeetCode-Solutions-master/Python/last-stone-weight-ii.py
# solution_class: Solution
# submission_id: 8cc38ea4d269bcff2e3777027a71ca1b89c1a37b
# seed: 2718760744

# Time:  O(2^n)
# Space: O(2^n)

class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        dp = {0}
        for stone in stones:
            dp |= {stone+i for i in dp}
        S = sum(stones)
        return min(abs(i-(S-i)) for i in dp)