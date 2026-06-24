# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-winner-of-the-circular-game
# source_path: LeetCode-Solutions-master/Python/find-the-winner-of-the-circular-game.py
# solution_class: Solution2
# submission_id: f31f481329cf5272da151b73b34d5be95b35a77e
# seed: 1731386821

# Time:  O(n)
# Space: O(1)

# bottom-up solution

class Solution2(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def f(idx, n, k):
            if n == 1:
                return 0
            return (k+f((idx+k)%n, n-1, k))%n
        
        return f(0, n, k)+1