# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-moves-to-reach-target-score
# source_path: LeetCode-Solutions-master/Python/minimum-moves-to-reach-target-score.py
# solution_class: Solution
# submission_id: b8cc013c0ded8431a9a162c1c571d3e0b4732303
# seed: 4097876246

# Time:  O(logn)
# Space: O(1)

# greedy

class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        result = 0
        while target > 1 and maxDoubles:
            result += 1+target%2
            target //= 2
            maxDoubles -= 1
        return result+(target-1)