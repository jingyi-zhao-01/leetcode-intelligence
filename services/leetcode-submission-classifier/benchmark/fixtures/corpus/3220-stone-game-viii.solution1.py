# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: stone-game-viii
# source_path: LeetCode-Solutions-master/Python/stone-game-viii.py
# solution_class: Solution
# submission_id: 40b1ea84da75ba4cc8a13ffe0874937d34922ca4
# seed: 2240615682

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i in xrange(len(stones)-1):
            stones[i+1] += stones[i]
        return reduce(lambda curr, i: max(curr, stones[i]-curr), reversed(xrange(1, len(stones)-1)), stones[-1])