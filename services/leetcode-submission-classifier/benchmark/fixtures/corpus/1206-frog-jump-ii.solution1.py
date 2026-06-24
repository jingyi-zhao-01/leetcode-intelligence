# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: frog-jump-ii
# source_path: LeetCode-Solutions-master/Python/frog-jump-ii.py
# solution_class: Solution
# submission_id: 89e1a3edc2cdd178d5ff87b832112cbe35c2d372
# seed: 4065752434

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def maxJump(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        return stones[1]-stones[0] if len(stones) == 2 else max(stones[i+2]-stones[i] for i in xrange(len(stones)-2))