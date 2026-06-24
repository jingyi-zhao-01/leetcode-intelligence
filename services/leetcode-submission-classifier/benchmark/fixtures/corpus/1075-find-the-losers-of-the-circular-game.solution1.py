# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-losers-of-the-circular-game
# source_path: LeetCode-Solutions-master/Python/find-the-losers-of-the-circular-game.py
# solution_class: Solution
# submission_id: fc4cc7c50a3ebb80c0f027d09dba606d1e6531a2
# seed: 920126683

# Time:  O(n)
# Space: O(n)

# hash table, simulation

class Solution(object):
    def circularGameLosers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        lookup = [False]*n
        idx = 0
        for i in xrange(n):
            if lookup[idx]:
                break
            lookup[idx] = True
            idx = (idx+(i+1)*k)%n
        return [i+1 for i in xrange(n) if not lookup[i]]