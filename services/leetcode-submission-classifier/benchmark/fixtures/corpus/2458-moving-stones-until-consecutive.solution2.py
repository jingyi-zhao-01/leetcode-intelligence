# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: moving-stones-until-consecutive
# source_path: LeetCode-Solutions-master/Python/moving-stones-until-consecutive.py
# solution_class: Solution2
# submission_id: 22f1d34a3f77b4dedf0a6af56818891118dd2727
# seed: 2802750448

# Time:  O(1)
# Space: O(1)

class Solution2(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        stones = [a, b, c]
        stones.sort()
        left, min_moves = 0, float("inf")
        max_moves = (stones[-1]-stones[0]) - (len(stones)-1)
        for right in xrange(len(stones)):
            while stones[right]-stones[left]+1 > len(stones): # find window size <= len(stones)
                left += 1
            min_moves = min(min_moves, len(stones)-(right-left+1))  # move stones not in this window
        return [min_moves, max_moves]